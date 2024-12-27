import google.generativeai as genai   # Required library
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ['GOOGLE_API_KEY']   # Gemini API

genai.configure(api_key=api_key)

def generate_reply(user_query, sentiment):
    prompt = f"""
A customer left a {sentiment} review: 
"{user_query}"

Strict Rules:
1. Generate a professional and polite response tailored to the customer's input.  
2. Do not mention the sentiment of the review anywhere in the response.  
3. Keep the response concise, respectful, and clear, within 50 words.  
4. Use emojis naturally to reflect the customer's sentiment or experience.  
5. Avoid using the word "input" in the response.  
6. End with a sincerely note mentioning the company name, 'Uber Inc', on a new line (do not explicitly include the words "Uber Inc" in the body of the response).  

Creative Guidelines for Neutral Feedback:
1. Follow all strict rules.  
2. Add a touch of creativity and warmth to the response for a more engaging tone.  
"""
    model = genai.GenerativeModel("models/gemini-pro",
                                  generation_config=genai.GenerationConfig(max_output_tokens=50,
                                  temperature=0.5))
    chat = model.generate_content(prompt)   # Generate response with pre set rules (prompt)
    return chat.text
