from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "吃香蕉可以預防抽筋嗎"}]
)

print(response.choices[0].message.content)
