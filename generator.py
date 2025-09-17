from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("GEMINI_API_KEY")

def generate_captions(description, tone, length, social_media_platform):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= f"""
Generate a social media caption based on the following inputs:

Post Description/Idea: {description}
Tone: {tone} (e.g., friendly, funny, inspirational, professional)
Length: {length} (e.g., short: 10-20 words, medium: 20-40 words, long: 40-60 words)
Social Media Platform: {social_media_platform} (e.g., Instagram, Twitter, LinkedIn, TikTok)
Emojis: Include 1-3 relevant emojis that enhance the tone and message, placed naturally within or at the start/end of the caption.
Hashtags: Include 1-3 relevant, trending hashtags at the end of the caption, tailored to the platform and topic.

Instructions:

Craft a caption that captures the essence of the post description/idea and aligns with the specified tone.
Ensure the caption is engaging, conversational, and optimized for the specified social media platform (e.g., concise for Twitter, visual and trendy for Instagram, professional for LinkedIn).
Use simple, relatable language that feels authentic and avoids overly formal or complex words.
For a friendly tone, use a warm, approachable style with a call-to-action (e.g., "What’s your favorite? Tell us!" or "Drop a comment!").
For a funny tone, incorporate light humor, puns, or playful phrasing relevant to the description.
For an inspirational tone, use uplifting and motivating language to inspire the audience.
For a professional tone, keep it polished and concise, suitable for a business audience.
Match the specified length as closely as possible while keeping the caption natural and fluid.
Place emojis strategically to emphasize the tone or message without overloading the caption.
Include 1-3 hashtags that are relevant to the topic and trending on the specified platform, placed at the end.
Avoid generic phrases like "Like and share!" or mentioning the instructions in the output.
Ensure the caption feels unique, engaging, and encourages audience interaction where appropriate.

Example Outputs:

Friendly Tone (Instagram, Medium Length):
☀️ Nothing beats a sunny day and a good book! What’s your favorite way to unwind outdoors? Drop it below! #SummerVibes #BookLovers
Funny Tone (Twitter, Short Length):
Me: I’ll just have one cookie 🍪. Also me: eats the whole jar 😅 Who else? #CookieMonster #Relatable
Inspirational Tone (LinkedIn, Long Length):
Every small step forward counts. Keep pushing, stay focused, and believe in your journey. You’ve got this! 💪 #CareerGrowth #MotivationMonday
""")
    
    return response.text.strip()
