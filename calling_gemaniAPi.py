import google.generativeai as genai #importing the generativeai module from google

genai.configure(api_key='AIzaSyDdr3GClp39yAfFMfTsRRyDkqb5u83XhXI') #configuring the api key getting from the google ai studio

model = genai.GenerativeModel("gemini-2.0-flash-exp") #creating the model object
response = model.generate_content("welcome me, I am learning Agentic Ai") #generating the content

print("simple response____________________________________________________")
print(response.text)



#Image generation using generativeai module

import PIL.Image #importing the PIL module
img = PIL.Image.open("images/download.jpg")
#img.show()

prompt ="""analyse the image and export all the text and explain that text in the image"""

image_response = model.generate_content([prompt,img])
print("image response____________________________________________________")
print(image_response.text)


#chat history
chat = model.start_chat(history = [])
print("chat response____________________________________________________")
chat_response = chat.send_message("Hello, how are you?")
print(chat_response.text)

chat_response = chat.send_message("how can you explain yourself?")
print(chat_response.text)

print(chat.history)
print("temperature response____________________________________________________")



#temperature model setting
model1 = genai.GenerativeModel("gemini-1.5-flash",generation_config=genai.GenerationConfig(max_output_tokens=200,temperature=0.1))

response = model1.generate_content("how can i greet you?")
print(response.text)



