import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=api_key)

def generate_reply(user_query, sentiment):
    prompt = f""" A customer left a {sentiment} review: "{user_query}"
        strict rules : (Generate a professional and polite response. 
        Do not mention the sentiment which left by user any where in the response or unnecessary details in the response.

        Ensure the response is clear, respectful, and within 50 words. 

        Use varied wording each time for uniqueness.compulsory use emojis to replicate user sentiment.
        your response should based on cab service.
        
        Don't mention 'input' word in the response.

        mention company name in the response by sincerely note,'Uber Inc' after a 
        line break. Don't mention the company name text in the output.)

        week rules : (strict rules + creative response only for neutral sentiment.)
        """
    model = genai.GenerativeModel("models/gemini-pro",
                                  generation_config=genai.GenerationConfig(max_output_tokens=50,
                                  temperature=0.5))
    chat = model.generate_content(prompt)
    return chat.text
