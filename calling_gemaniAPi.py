import google.generativeai as genai #importing the generativeai module from google

genai.configure(api_key='AIzaSyDdr3GClp39yAfFMfTsRRyDkqb5u83XhXI') #configuring the api key getting from the google ai studio

model = genai.GenerativeModel("gemini-1.5-flash") #creating the model object
response = model.generate_content("welcome me, I am learning Agentic Ai") #generating the content
print(response.text)