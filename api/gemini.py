import vertexai
from vertexai.generative_models import GenerativeModel, Part

class Server:
    def __init__(self): 
        PROJECT_ID = "project-name"
        vertexai.init(project=PROJECT_ID, location="us-central1")
        self.system_context = []
        self.model = GenerativeModel("gemini-1.5-flash-002")
        self.chat_context = []
    
    def add_system_context(self, message):
        self.system_context.append(message)
        self.model = GenerativeModel("gemini-1.5-flash-002", system_instruction=self.system_context)   
    def add_user_context(self, message):
        self.chat_context.append(vertexai.generative_models.Content(role="user", parts=[Part.from_text(f"{message}")]))
    def add_model_context(self, message):
        self.chat_context.append(vertexai.generative_models.Content(role="model", parts=[Part.from_text(f"{message}")]))
    def ask_question(self, message, add_context=False):
        chat = self.model.start_chat(history=self.chat_context)
        response = chat.send_message(f"{message}")
        if add_context:
            self.add_context(message, "user")
            self.add_context(response.text, "model")
        return response.text



if __name__ == '__main__':
    gemini = Server()
    gemini.add_system_context("Answer as a Megatron")
    print(gemini.ask_question("What is Linux?"))
    print(gemini.ask_question("What is asked in previous question?"))