import anthropic

client = anthropic.Anthropic()

conversation_history = []

print("和 Claude 对话（输入 quit 退出）")
print("-" * 30)

while True:
    user_input = input("你: ").strip()
    
    if user_input.lower() == "quit":
        print("再见！")
        break
    
    if not user_input:
        continue
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=conversation_history
    )
    
    reply = message.content[0].text
    
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    print(f"Claude: {reply}")
    print()