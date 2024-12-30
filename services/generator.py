import openai
from typing import List, Dict, Any, Optional
import os


class ChatService:
    def _init_(self, 
                model_name= "gpt-3.5-turbo", 
                temperature=0.7, 
                max_tokens=2048,
                system_prompt= "You are a helful assistant."
            ):

        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.messages = [{
            "role": "system",
            "content": system_prompt
        }]

    def update_messages(self ,role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_response(self,prompt: str):
        try:
            self.update_messages("user", prompt)
            response= openai.chat.completions.create(
                model= self.model_name,
                messages= self.messages,
                temperature= self.temperature,
                max_tokens= self.max_tokens
            )
            self.update_messages("assistant", response.choices[0].message.content)
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            print(f"An error occured: {e}")


chat_service = ChatService(system_prompt="You are a school teacher whose name is Walter White who teaches chemistry.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_service.get_response(user_input)
    print(f"ASSISTANT: {response}")
