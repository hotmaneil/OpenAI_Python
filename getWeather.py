import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

# 讀取環境變數
apiKey = os.getenv("API_KEY")

client = OpenAI(api_key=apiKey)

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. 台灣桃園"
            }
        },
        "required": [
            "location"
        ],
        "additionalProperties": False
    }
}]

response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "今天台灣桃園市蘆竹區的天氣概況?"}],
    tools=tools
)

print(response.output)

# 其它免費範例


def get_weather(latitude, longitude):
    '''依照經緯度取得天氣資訊'''
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# result = get_weather(25.019408465082407, 121.3891475683989)
# print('result', result)
