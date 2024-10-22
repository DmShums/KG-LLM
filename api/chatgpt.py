from openai import OpenAI

class Server:
    def __init__(self):
        self.client = OpenAI(api_key="your-api-key")
        self.chat_context = []
    
    def add_system_context(self, message):
        self.chat_context.append({"role":"system", "content":message})

    def ask_question(self, message):
        self.chat_context.append({"role":"user", "content":message})
        completion = openai.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=self.chat_context
        )
        response = completion.choices[0].message.content
        self.add_system_context(response)
        return response



if __name__ == '__main__':
    openai = Server()
    print(openai.ask_question("What is Linux?"))
    print(openai.ask_question("What is asked in previous question?"))
