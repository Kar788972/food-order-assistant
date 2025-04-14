
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Dict
import openai

app = FastAPI()

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

class OrderPrompt(BaseModel):
    prompt: str

@app.post("/order")
async def process_order(data: OrderPrompt):
    # Use GPT to parse the prompt
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Extract order details as JSON with fields: items (name, quantity), location, and delivery_time."},
            {"role": "user", "content": data.prompt}
        ]
    )
    parsed_response = completion.choices[0].message['content']

    # Simulate menu results (mocked)
    mock_results = [
        {"platform": "Deliveroo", "restaurant": "Pizza Bros", "item": "Cheese Pizza", "price": 45, "rating": 4.7, "eta": "35 mins"},
        {"platform": "Talabat", "restaurant": "Italian Pie", "item": "Cheese Pizza", "price": 42, "rating": 4.3, "eta": "40 mins"},
        {"platform": "Careem", "restaurant": "Napoli Express", "item": "Cheese Pizza", "price": 47, "rating": 4.8, "eta": "30 mins"},
    ]

    # Rank results by price, then rating
    ranked_results = sorted(mock_results, key=lambda x: (x['price'], -x['rating']))

    return {
        "parsed_order": parsed_response,
        "top_options": ranked_results[:3]
    }
