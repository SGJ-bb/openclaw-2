#!/bin/bash
# OpenClaw Watchdog - Mac/Linux 启动脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "OpenClaw Watchdog"
echo "================="
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "错误：需要 Python 3"
    echo "请安装：brew install python3 (Mac) 或 sudo apt install python3 (Linux)"
    read -p "按回车键退出..."
    exit 1
fi

# 检查 tkinter
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "错误：需要 tkinter"
    echo "请安装：brew install python-tk (Mac) 或 sudo apt install python3-tk (Linux)"
    read -p "按回车键退出..."
    exit 1
fi

# 启动程序
echo "正在启动..."
cd "$SCRIPT_DIR"
python3 watchdog.py
