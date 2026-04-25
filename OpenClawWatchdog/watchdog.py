#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw Watchdog - 跨平台图形界面版
支持：Windows / Mac / Linux
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import os
import sys
import socket
import time
from datetime import datetime

class OpenClawWatchdog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OpenClaw Watchdog")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        # 配置文件路径
        self.config_file = self.get_config_path()
        
        # 默认配置
        self.check_interval = 30
        self.port = 18789
        self.is_running = False
        self.watchdog_thread = None
        
        # 加载配置
        self.load_config()
        
        # 创建界面
        self.create_widgets()
        
        # 更新状态显示
        self.update_status_display()
    
    def get_config_path(self):
        """获取配置文件路径"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, "watchdog_config.txt")
    
    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('CHECK_INTERVAL='):
                            self.check_interval = int(line.split('=')[1])
        except Exception as e:
            print(f"加载配置失败：{e}")
    
    def save_config(self, interval):
        """保存配置文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write(f"# OpenClaw Watchdog Config\n")
                f.write(f"CHECK_INTERVAL={interval}\n")
            self.check_interval = interval
            self.update_status_display()
            messagebox.showinfo("成功", f"已设置为 {interval} 秒")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置失败：{e}")
    
    def update_status_display(self):
        """更新状态显示"""
        self.status_label.config(text=f"当前检查间隔：{self.check_interval} 秒")
    
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_label = ttk.Label(
            main_frame, 
            text="🐕 OpenClaw Watchdog",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # 状态显示框
        status_frame = ttk.LabelFrame(main_frame, text="状态", padding="15")
        status_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.status_label = ttk.Label(
            status_frame,
            text=f"当前检查间隔：{self.check_interval} 秒",
            font=("Arial", 14, "bold"),
            foreground="green"
        )
        self.status_label.pack()
        
        # 快速设置框
        interval_frame = ttk.LabelFrame(main_frame, text="快速设置检查间隔", padding="15")
        interval_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 预设按钮
        button_frame = ttk.Frame(interval_frame)
        button_frame.pack(pady=(0, 10))
        
        ttk.Button(button_frame, text="10 秒", command=lambda: self.save_config(10)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="30 秒", command=lambda: self.save_config(30)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="60 秒", command=lambda: self.save_config(60)).pack(side=tk.LEFT, padx=5)
        
        # 自定义输入
        custom_frame = ttk.Frame(interval_frame)
        custom_frame.pack(fill=tk.X)
        
        ttk.Label(custom_frame, text="自定义:").pack(side=tk.LEFT)
        
        self.custom_var = tk.StringVar()
        custom_entry = ttk.Entry(custom_frame, textvariable=self.custom_var, width=10)
        custom_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            custom_frame, 
            text="设置",
            command=self.set_custom_interval
        ).pack(side=tk.LEFT, padx=5)
        
        # 操作按钮
        action_frame = ttk.LabelFrame(main_frame, text="操作", padding="15")
        action_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.start_button = ttk.Button(
            action_frame,
            text="▶️ 启动看门狗",
            command=self.start_watchdog,
            style="Accent.TButton"
        )
        self.start_button.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(
            action_frame,
            text="📊 查看端口状态",
            command=self.check_port_status
        ).pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(
            action_frame,
            text="⚙️ 打开配置文件",
            command=self.open_config_file
        ).pack(fill=tk.X)
        
        # 退出按钮
        ttk.Button(
            main_frame,
            text="❌ 退出",
            command=self.on_exit
        ).pack(pady=(10, 0))
        
        # 底部说明
        ttk.Label(
            main_frame,
            text="提示：启动后会在后台持续监控端口",
            foreground="gray",
            font=("Arial", 9)
        ).pack(pady=(10, 0))
    
    def set_custom_interval(self):
        """设置自定义间隔"""
        try:
            value = int(self.custom_var.get())
            if value > 0:
                self.save_config(value)
                self.custom_var.set("")
            else:
                messagebox.showwarning("警告", "请输入大于 0 的数字")
        except ValueError:
            messagebox.showwarning("警告", "请输入有效的数字")
    
    def check_port(self):
        """检查端口是否被占用"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex(('127.0.0.1', self.port))
            sock.close()
            return result == 0
        except:
            return False
    
    def start_gateway(self):
        """启动 openclaw gateway"""
        try:
            # 检测系统
            if sys.platform == 'win32':
                # Windows
                subprocess.Popen(
                    ['node', 'F:\\npm-global\\node_modules\\openclaw\\openclaw.mjs', 'gateway'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            else:
                # Mac/Linux
                subprocess.Popen(
                    ['openclaw', 'gateway'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            return True
        except Exception as e:
            print(f"启动 Gateway 失败：{e}")
            return False
    
    def watchdog_loop(self):
        """看门狗主循环"""
        while self.is_running:
            try:
                if not self.check_port():
                    print(f"[{datetime.now()}] 端口未监听，启动 Gateway...")
                    if self.start_gateway():
                        time.sleep(10)  # 等待启动
                        if self.check_port():
                            print(f"[{datetime.now()}] ✓ Gateway 启动成功")
                        else:
                            print(f"[{datetime.now()}] ✗ Gateway 启动失败")
                else:
                    print(f"[{datetime.now()}] ✓ 端口正常")
                
                time.sleep(self.check_interval)
            except Exception as e:
                print(f"看门狗错误：{e}")
                time.sleep(5)
    
    def start_watchdog(self):
        """启动看门狗"""
        if self.is_running:
            messagebox.showwarning("警告", "看门狗已在运行中")
            return
        
        if messagebox.askyesno("确认", f"启动看门狗？\n检查间隔：{self.check_interval}秒"):
            self.is_running = True
            self.start_button.config(text="⏹️ 停止看门狗", command=self.stop_watchdog)
            
            # 启动监控线程
            self.watchdog_thread = threading.Thread(target=self.watchdog_loop, daemon=True)
            self.watchdog_thread.start()
            
            messagebox.showinfo("成功", "看门狗已启动！\n将在后台持续监控端口")
    
    def stop_watchdog(self):
        """停止看门狗"""
        if messagebox.askyesno("确认", "停止看门狗？"):
            self.is_running = False
            self.start_button.config(text="▶️ 启动看门狗", command=self.start_watchdog)
            messagebox.showinfo("提示", "看门狗已停止")
    
    def check_port_status(self):
        """检查端口状态"""
        if self.check_port():
            messagebox.showinfo("端口状态", "✓ Gateway 正在运行\n端口 18789 正在监听")
        else:
            messagebox.showwarning("端口状态", "✗ Gateway 未运行\n端口 18789 未监听")
    
    def open_config_file(self):
        """打开配置文件"""
        try:
            if sys.platform == 'win32':
                os.startfile(self.config_file)
            elif sys.platform == 'darwin':
                subprocess.run(['open', self.config_file])
            else:
                subprocess.run(['xdg-open', self.config_file])
        except Exception as e:
            # 如果打开失败，尝试用文本编辑器打开
            try:
                import webbrowser
                webbrowser.open(self.config_file)
            except:
                messagebox.showerror("错误", f"无法打开配置文件：{e}")
    
    def on_exit(self):
        """退出程序"""
        if self.is_running:
            if messagebox.askyesno("确认", "看门狗正在运行，确定要退出吗？"):
                self.is_running = False
                self.root.quit()
        else:
            self.root.quit()
    
    def run(self):
        """运行程序"""
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        
        # 自定义按钮样式
        style.configure('Accent.TButton', 
                       background='#38ef7d',
                       foreground='black',
                       font=('Arial', 12, 'bold'))
        
        self.root.mainloop()

if __name__ == "__main__":
    app = OpenClawWatchdog()
    app.run()
