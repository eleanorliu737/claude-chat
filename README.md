# Dublin Job Hunt · JD Analyzer

A command-line assistant that analyzes job descriptions for a specific job seeker's situation, built on the Anthropic API.
> 一个基于 Anthropic API 的命令行助手，针对特定求职者的处境分析职位描述（JD）。

## Problem 解决什么问题

Job seekers read many JDs but struggle to quickly judge fit — especially with constraints like visa sponsorship. This tool analyzes a pasted JD against a fixed structure and the user's real background.
> 求职者每天看大量 JD，但很难快速判断匹配度——尤其是有签证担保这类硬约束时。这个工具把粘贴进来的 JD 按固定结构、结合用户真实背景做分析。

## Who it's for 给谁用

Built for a Dublin-based job seeker targeting Mandarin-facing CSM/SE/TAM roles, who needs Critical Skills Employment Permit (CSEP) sponsorship.
> 为一位在都柏林、目标是 Mandarin-facing CSM/SE/TAM 岗位、需要 CSEP 签证担保的求职者定制。

## What it does 功能

Given a pasted JD, it outputs a structured analysis:
> 粘贴一段 JD，输出结构化分析：

- Role overview / 职位概览
- Hard requirements / 硬性要求
- Nice-to-haves / 加分项
- Candidate fit (matches and gaps) / 匹配度（匹配项与缺口）
- Visa feasibility (CSEP check) / 签证可行性（CSEP 判断）
- Recommendation / 建议

## How it works 技术说明

The candidate's background and visa constraints are encoded in a system prompt, so the model analyzes every JD against the same context and returns a consistent structure instead of free-form text.
> 求职者的背景和签证约束写在 system prompt 里，因此模型每次都基于相同上下文分析 JD，返回固定结构而非自由发挥的文本。

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

    python main.py

## Model 使用的模型

claude-haiku-4-5