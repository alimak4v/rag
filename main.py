from openai import OpenAI
from beauty_code import rainbow
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_BASE_URL"))

conversation_history = [{"role": "system", "content": """You are a highly intelligent, thoughtful, and analytical AI assistant. You communicate in a direct, clear, and conversational style. Your goal is to provide the shortest, most efficient path to the user's solution.
                                                        CRITICAL RULES:
                                                        1. NO FILLER WORDS: Never start your response with filler phrases like "Certainly!", "Absolutely!", "I'd be happy to help with that!", or "Sure thing!". Dive straight into the answer.
                                                        2. CONCISENESS FIRST: Provide a concise, direct answer first. If more elaboration is needed, offer it logically afterwards.
                                                        3. ONE DECISIVE RECOMMENDATION: Provide one clear, decisive recommendation instead of listing multiple options unless the user specifically asks for choices.
                                                        4. STRUCTURE: Use bullet points, numbered lists, and bold text for key terms to make your output highly readable and scannable. 
                                                        5. FORMATTING: Use Markdown formatting naturally. Do not use emojis unless explicitly requested.
                                                        6. LONE RULE ADHERENCE: Strictly follow the user's instructions. If information is missing, ask for clarification.
                                                        ."""}]

hi = r"""
████   ███   ███       ████  █     █   █  ████   
█░░░█ █ ░░█ █ ░░░      █░░░█ █░    █░  █░█ ░░░░  
████░░█████░█░ ██░████ ████░░█░░   █░░ █░░███░░░ 
█░░█░ █░░░█░█░░ █░ ░░░░█░░░░ █░░   █░░ █░░ ░░█   
█░░░█░█░░░█░░███ ░░ ░░░█░░░░░█████  ███ ░████░░  
 ░░  ░ ░░  ░░ ░░░ ░     ░░    ░░░░░  ░░░ ░░░░░ ░ 
  ░   ░ ░   ░  ░░░       ░     ░░░░░  ░░░  ░░░░  
"""

print(rainbow(hi))

while True:
    question = input(">>> ")
    conversation_history.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=conversation_history,
        stream=True
    )
    answer = ""
    for token in response:
        now = token.choices[0].delta.content
        if now != "":
            answer += now
            print(now, end="", flush=True)
    print()
    conversation_history.append({"role": "assistant", "content": answer})
