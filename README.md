# Claude Chat

一个基于 Anthropic API 的命令行对话程序。支持连续多轮对话，Claude 能记住上下文。

## 功能

- 命令行交互，实时输入输出
- 多轮对话（保留对话历史）
- 输入 quit 退出

## 环境要求

- Python 3.8+
- anthropic SDK

## 安装

    pip install anthropic

## 配置

将 Anthropic API key 设置为环境变量（Windows PowerShell）：

    setx ANTHROPIC_API_KEY "your-api-key-here"

## 运行

    python test.py

## 使用的模型

claude-haiku-4-5