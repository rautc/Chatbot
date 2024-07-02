import json
from fuzzywuzzy import process

class SocialWebsiteChatbot:
    def __init__(self, responses_file='chatbot_responses.json'):
        with open(responses_file, 'r') as f:
            
            self.responses = json.load(f)

    def get_response(self, user_input):
        """Returns a response based on user input."""
        user_input = user_input.lower().strip()
        corrected_input = self.correct_spelling(user_input)
        return self.responses.get(corrected_input, "I'm sorry, I don't understand that question. Can you please rephrase?")

    def correct_spelling(self, user_input):
        """Corrects spelling mistakes in user input."""
        options = list(self.responses.keys())
        corrected_input, _ = process.extractOne(user_input, options)
        return corrected_input

def main():
    chatbot = SocialWebsiteChatbot()
    
    print("Welcome to the Social Website Chatbot! Ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()