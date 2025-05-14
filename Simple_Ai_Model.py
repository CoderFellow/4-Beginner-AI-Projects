def chatbot_start():

# store's the chatbot's responses
     chatbot_response={"hi":"Hello","hello": "High there","how are you?":"I'm doing well, thank you for asking"}

# processes the user's input
     while True:
     # takes the user's input
          user_input=input("Say hi (chatbot is waiting): ").lower()
          
          if user_input.startswith("hello"):
               print("Hi there!")
          
          elif user_input.startswith("Hi"):
               print("Hello!")
          
          elif "how" in user_input and "are" in user_input:
               print("I'm doing well, thank you for asking!")
          
          elif user_input in chatbot_response:
               print(chatbot_response[user_input])
               if user_input=="bye":
                    print("Goodbye")
                    break
          else:
               print("Sorry, I'm still under development : (")

if __name__=="__main__":
     chatbot_start()