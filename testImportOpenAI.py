from openai import OpenAI
import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

# 讀取環境變數
apiKey = os.getenv("API_KEY")

client = OpenAI(api_key=apiKey)

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "腰的骨頭有點痛怎麼辦?"}]
)

print(response.choices[0].message.content)
