#!/usr/bin/env python3
# OpenClaw Watchdog Launcher
# 跨平台启动脚本

import subprocess
import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    watchdog_script = os.path.join(script_dir, "watchdog.py")
    
    if not os.path.exists(watchdog_script):
        print("错误：找不到 watchdog.py")
        sys.exit(1)
    
    # 运行 Python GUI 程序
    try:
        subprocess.run([sys.executable, watchdog_script])
    except Exception as e:
        print(f"启动失败：{e}")
        input("按回车键退出...")

if __name__ == "__main__":
    main()
