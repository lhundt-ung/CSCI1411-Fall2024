import openai
import os

api_key = ""
openai.organization = ""
openai.api_key = api_key

def askChatGPT(question):

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": question}
    ]
  )
  
  aiResponse = response["choices"][0]["message"]["content"]
  #print(aiResponse)
  return aiResponse

def main():
    # Without Loop
    #question = input("How can I help you? Press q to quit: ")
    #askChatGPT(question)

    # Loop
    x = 0
    while x == 0:
      question = input("How can I help you? Press q to quit: ")
      if question == "q":
        x = 1
        break

      answer = askChatGPT(question)

      print("=================")
      print("CHATGPT: ", answer)
      print("=================")


if __name__ == "__main__":
    main()


