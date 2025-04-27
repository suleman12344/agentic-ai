import langchain_google_genai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from google_genaiAPI import google_api
model:ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key=google_api,)#creating the model object
def generate_response(prompt):
    response = model.invoke(prompt) #generating the content
    return response.content


cont = "yes"
while cont == "yes":
  prompt = input("Enter prompt:")
  print("prompt is: " + prompt)
  Answer = generate_response(prompt)
  print("Answer is: " + Answer)
  cont = input("Do you want to continue? (yes/no): ")
print("Thank you for using the program!")

