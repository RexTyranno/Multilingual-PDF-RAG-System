import openai
from typing import List, Dict, Any, Optional
import os


class ChatService:
    def _init_(self, 
                model_name="gpt-3.5-turbo",
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

    def update_messages(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_response(self,prompt: str, retriever):
        try:
            context= retriever.get_relevant_context(prompt)
            base_prompt = f"""This is the context: {context} and answer the user query based on this only. 
            If there is no relevant answer present here, answer that you don't know. 
            Here is the user query: {prompt}."""
            self.update_messages("user", base_prompt)
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

