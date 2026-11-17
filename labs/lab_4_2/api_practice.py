from openai import OpenAI,NotFoundError , APIConnectionError
user_prompt = input("Ask Qwen a question: ")
try :
 client = OpenAI(
    base_url="http://localhost:11434/v1",
   # base_url="http://localhost:11435/v1", #to check the api connection error 
    api_key="ollama"
 )
 response = client.chat.completions.create(
    model="qwen2.5:3b",
    #model="model-that-does-not-exist", #to check the model not found error
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }

    ],
    max_tokens=100
 )
 print(response.choices[0].message.content)
 print (response.choices[0].finish_reason )
 print(response.usage)
except NotFoundError:
 print ("model does not exist. Run 'ollama list' to check installed models.")
except APIConnectionError:
 print ("Cannot connect to Ollama. Make sure the local server is running")

