# 🐕 OpenClaw Watchdog

> 跨平台图形界面看门狗程序 - 自动监控端口，防止服务自杀


## 📖 简介

OpenClaw Watchdog 是一个图形界面的端口监控工具，用于自动检测和重启 openclaw gateway 服务。当检测到 18789 端口未运行时，会自动启动 gateway，确保服务持续可用。

**特点：**

- 🖥️ 图形界面，操作简单
- ⏱️ 可自定义检查间隔
- 🔄 自动重试机制
- 🌍 跨平台支持（Windows/Mac/Linux）
- 🚀 一键启动，后台运行

***

## 🎯 两个版本

本项目提供两个版本，根据需求选择：

### 1. HTA 版（Windows 专用）

- ✅ **优点**：无需安装任何依赖
- ✅ **适合**：只要 Windows 系统就能用
- ❌ **限制**：仅支持 Windows

### 2. Python 版（跨平台）⭐ 推荐

- ✅ **优点**：跨平台、界面美观、功能完整
- ✅ **适合**：Windows/Mac/Linux 用户
- ⚠️ **要求**：需要 Python 3.6+

***

## 🚀 快速开始

### Windows 用户

#### 方法 1：HTA 版（无需 Python）

```bash
双击运行：run.bat 或 app.hta
```

#### 方法 2：Python 版（推荐）

```bash
双击运行：启动-Python 版.bat
```

### Mac / Linux 用户

```bash
# 1. 安装依赖
# Mac:
brew install python3 python-tk

# Linux (Ubuntu/Debian):
sudo apt install python3 python3-tk

# 2. 启动程序
cd /path/to/OpenClawWatchdog
python3 watchdog.py
# 或
./start.sh
```

***

## 📋 功能特性

### 主界面功能

- ✅ **状态显示** - 实时显示当前检查间隔
- ✅ **快速设置** - 预设 10 秒/30 秒/60 秒
- ✅ **自定义间隔** - 手动输入任意秒数
- ✅ **启动监控** - 一键启动看门狗
- ✅ **端口检测** - 查看 18789 端口状态
- ✅ **配置管理** - 快速打开配置文件
- ✅ **优雅退出** - 确认对话框防止误操作

### 后台监控功能

- ✅ **自动检测** - 按设定间隔检查端口
- ✅ **自动启动** - 端口未监听时自动启动 gateway
- ✅ **启动验证** - 启动后验证是否成功
- ✅ **失败重试** - 启动失败下次继续尝试
- ✅ **日志输出** - 实时打印运行日志

***

## 📁 文件说明

### HTA 版本文件

```
OpenClawWatchdog/
├── app.hta              # HTA 图形界面程序
├── run.bat              # HTA 启动器
├── kanmengou.bat        # 看门狗主程序
├── watchdog_config.txt  # 配置文件
└── README.txt           # HTA 版说明
```

### Python 版本文件

```
OpenClawWatchdog/
├── watchdog.py          # Python 主程序 ⭐
├── start.py             # Python 启动器
├── start.sh             # Shell 启动器 (Mac/Linux)
├── 启动-Python 版.bat   # Windows 启动器
├── watchdog_config.txt  # 配置文件
└── README-Python.txt    # Python 版说明
```

***

## 💻 界面预览

```
┌─────────────────────────────────┐
│  🐕 OpenClaw Watchdog           │
├─────────────────────────────────┤
│  状态                           │
│  当前检查间隔：30 秒             │
│                                 │
│  快速设置检查间隔                │
│  [10 秒] [30 秒] [60 秒]         │
│  自定义：[____秒] [设置]        │
│                                 │
│  操作                           │
│  [▶️ 启动看门狗]  [停止看门狗]  │
│  [📊 查看端口状态]              │
│  [⚙️ 打开配置文件]              │
│  [❌ 退出]                      │
└─────────────────────────────────┘
```

***

## ⚙️ 配置说明

### 配置文件

`watchdog_config.txt` - 存储检查间隔设置

```ini
# OpenClaw Watchdog Config
CHECK_INTERVAL=30
```

### 可配置项

| 参数               | 说明      | 默认值 | 范围     |
| ---------------- | ------- | --- | ------ |
| `CHECK_INTERVAL` | 检查间隔（秒） | 30  | 1-3600 |

### 预设值

- **10 秒** - 频繁检查，快速响应
- **30 秒** - 默认设置，平衡性能
- **60 秒** - 节省资源，低频检查

***

## 📖 使用教程

### 第一次使用

1. **启动程序**
   - Windows：双击 `启动-Python 版.bat`
   - Mac/Linux：运行 `python3 watchdog.py`
2. **设置检查间隔**
   - 点击预设按钮（10 秒/30 秒/60 秒）
   - 或输入自定义秒数，点击"设置"
3. **启动看门狗**
   - 点击"▶️ 启动看门狗"
   - 确认对话框点"Yes"
4. **完成！**
   - 程序会在后台持续监控
   - 可以关闭界面，看门狗独立运行

### 日常使用

- **查看状态**：点击"📊 查看端口状态"
- **修改间隔**：重新设置即可，下次启动生效
- **停止监控**：点击"⏹️ 停止看门狗"
- **编辑配置**：点击"⚙️ 打开配置文件"

***

## 🔧 故障排除

### HTA 版问题

**Q: 双击没反应**

- 检查文件是否存在：`F:\OpenClawWatchdog\app.hta`
- 右键 app.hta → 属性 → 解除锁定 → 确定

**Q: 窗口闪退**

- 正常现象，GUI 窗口会单独弹出
- 检查任务栏是否有新窗口

### Python 版问题

**Q: 提示找不到 Python**

```bash
# 检查 Python 是否安装
python --version

# 未安装请访问：https://www.python.org/
```

**Q: tkinter 错误**

```bash
# Mac 安装 tkinter:
brew install python-tk

# Linux 安装 tkinter:
sudo apt install python3-tk

# Windows: 重新安装 Python，勾选 tcl/tk 支持
```

**Q: 无法启动 gateway**

- 检查 Node.js 是否安装：`node --version`
- 检查 openclaw 是否安装：`openclaw --version`
- 确认 openclaw 路径正确

### 通用问题

**Q: 一直提示端口未监听**

- 检查 openclaw 是否正确安装
- 检查 18789 端口是否被占用
- 查看日志输出，确认错误信息

**Q: 看门狗不工作**

- 确认已点击"启动看门狗"
- 检查是否有错误提示
- 查看控制台日志输出

***

## 🛠️ 高级用法

### 修改默认端口

编辑 `kanmengou.bat` 或 `watchdog.py`，找到端口定义：

```python
# watchdog.py 第 18 行左右
self.port = 18789  # 修改为你需要的端口
```

### 修改 Gateway 启动命令

**Windows (kanmengou.bat):**

```batch
start /B cmd /c "node F:\npm-global\node_modules\openclaw\openclaw.mjs gateway"
```

**Mac/Linux (watchdog.py):**

```python
subprocess.Popen(['openclaw', 'gateway'])
```

### 开机自启动

**Windows:**

1. 创建快捷方式
2. 放入启动文件夹：`shell:startup`

**Mac:**

```bash
# 添加到登录项
osascript -e 'tell application "System Events" to make login item at end with properties {path:"/path/to/watchdog.py", hidden:false}'
```

**Linux:**

```bash
# 添加到 crontab
@reboot cd /path/to && python3 watchdog.py
```

***

## 📊 版本对比

| 特性       | HTA 版   | Python 版          |
| -------- | ------- | ----------------- |
| **系统支持** | Windows | Windows/Mac/Linux |
| **依赖要求** | 无       | Python 3.6+       
***

- 🆓 免费开源


## 📝 更新日志

### v2.0 - 2024

- ✅ 新增 Python 跨平台版本
- ✅ 支持 Mac/Linux 系统
- ✅ 现代化 Tkinter 界面
- ✅ 优化启动流程

### v1.0 - 2024

- ✅ 初始版本（HTA）
- ✅ Windows 平台支持
- ✅ 图形界面监控

***

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- Bug 报告
- 功能建议
- 代码贡献
- 文档改进

***

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
## 🙏 致谢

感谢所有贡献者和使用者！

***

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star！**

Made with ❤️ by \[Your Name]

</div>
