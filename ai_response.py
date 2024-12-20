import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=api_key)

def generate_reply(user_query, sentiment):
    prompt = f""" A customer left a {sentiment} review: "{user_query}"
        Generate a professional and polite response. 
        Do not mention the sentiment or unnecessary details in the response. 
        Ensure the response is clear, respectful, and within 50 words. 
        Use varied wording each time for uniqueness.
        mention company name in the response by sincerely note,'Uber Inc' after a 
        line break. Don't mention the company name text in the output.
        """
    model = genai.GenerativeModel("models/gemini-pro",
                                  generation_config=genai.GenerationConfig(max_output_tokens=50,
                                  temperature=0.5))
    chat = model.generate_content(prompt)
    return chat.text

if __name__ == "__main__":
    print(generate_reply("Travel is not good","negative"))