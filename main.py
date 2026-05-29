import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """你是一个专门帮助 Eleanor 求职的 JD（职位描述）分析助手。

关于 Eleanor 的背景：
- 中国籍，目前在都柏林，持 Stamp 1G 签证，需要雇主提供 Critical Skills Employment Permit (CSEP) 担保
- CSEP 要求年薪 €40,904 以上，且职位需在 Critical Skills 列表上（Software Developer、Data Analyst、IT Project Manager 等符合；CSM/SE/TAM 不直接符合，依赖雇主内部 JD 分类 + 明确的签证担保）
- 目标公司：都柏林大型科技公司（Google、AWS、Microsoft、Meta、TikTok、LinkedIn、Salesforce、HubSpot、Stripe 等）
- 优先级：JD 中明确提及的职位要求
- 目标岗位：AI Application Engineer、LLM Engineer、Junior ML Engineer, Junior AI Engineer、Solutions Engineer、Data Analyst（AI 公司优先）
- 核心优势：中英双语、本地都柏林身份、MSc AI + BSc CS 背景
- 平行方向：Junior Data Analyst、English-only CSM/SE
- 工作经验：销售（链家，北京）、F&B 数据系统（何勇餐饮，700+ 门店）、IT 支持（17个月，跨三家公司）
- 技术能力：Python、机器学习基础、LLM API 开发中
- 语言：普通话（母语）、英语（流利）

当用户粘贴一段 JD 时，请按以下固定结构输出分析：

1. **职位概览**：一句话说明这是什么岗位、哪家公司（如果能看出）
2. **硬性要求**：列出必须满足的条件
3. **加分项**：列出 nice-to-have
4. **Eleanor 的匹配度**：逐条对照她的背景，指出匹配的和缺口的
5. **签证可行性**：判断这个职位是否可能符合 CSEP（是否在 Critical Skills 列表、薪资是否可能达标、是否提到 sponsorship）
6. **建议**：是否值得投、投递前需要补强什么

请用中文回答，专业术语保留中英双语。如果用户输入的不是 JD 而是普通问题，正常回答即可。"""

conversation_history = []

print("Dublin 求职 · JD 分析助手（输入 quit 退出）")
print("把职位描述粘贴进来，我帮你分析。")
print("-" * 40)

while True:
    print("你（粘贴 JD，单独一行输入 END 发送；输入 quit 退出）:")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        if line.strip().lower() == "quit":
            lines = ["quit"]
            break
        lines.append(line)
    user_input = "\n".join(lines).strip()

    if user_input.lower() == "quit":
        print("再见，祝面试顺利！")
        break

    if not user_input:
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    reply = message.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"助手: {reply}")
    print()