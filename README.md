# Claude Chat

A command-line chat program built on the Anthropic API. It supports multi-turn conversations, with Claude remembering the context.
> 一个基于 Anthropic API 的命令行对话程序。支持连续多轮对话，Claude 能记住上下文。

## Features 功能

- Command-line interaction with real-time input and output
> 命令行交互，实时输入输出
- Multi-turn conversation (keeps chat history)
> 多轮对话（保留对话历史）
- Type `quit` to exit
> 输入 quit 退出

## Requirements 环境要求

- Python 3.8+
- anthropic SDK

## Installation 安装

    pip install anthropic

## Configuration 配置

Set your Anthropic API key as an environment variable (Windows PowerShell):
> 将 Anthropic API key 设置为环境变量（Windows PowerShell）：

    setx ANTHROPIC_API_KEY "your-api-key-here"

## Usage 运行

    python test.py

## Model 使用的模型

claude-haiku-4-5