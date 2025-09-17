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
Tone: {tone}
Length: {length} (e.g., short, medium, long; approximate word count: short ~10-20 words, medium ~20-40 words, long ~40-60 words)
Social Media Platform: {social_media_platform}
Emojis: Yes, include relevant emojis naturally within the text or at the start/end.
Hashtags: Yes, include 1-2 relevant and trending hashtags at the end of the caption.

Instructions:

Create a caption that reflects the provided tone and matches the post description or idea.

Ensure the caption is engaging, conversational, and suitable for social media platforms.

Incorporate the specified emojis naturally within the text or at the start/end.

Include the specified and trending 1-2 hashtags at the end of the caption.

Match the approximate length as specified.

Avoid overly formal language, difficult words and ensure the caption feels authentic and relatable.

If the tone is friendly, use a warm, approachable, and upbeat style, encouraging audience interaction (e.g., questions or calls to action like "Share below!" or "Let's chat!").

Don't mention the instructions in the caption and avoid these formats (e.g., "Don't forget to like and share!" is acceptable, but not "As per instructions..., Here's an engaging social media caption for your post:...").

For funny tones, give it funny touch.
Don't use difficult vocabulary -> starightforward

Example Output (Friendly Tone):

☕️ Rise and grind! There's nothing like the aroma of freshly brewed coffee to kickstart your day. What's your go-to coffee order? Share in the comments! #CoffeeLovers #MorningBrew #CaffeineFix""")
    
    return response.text.strip()