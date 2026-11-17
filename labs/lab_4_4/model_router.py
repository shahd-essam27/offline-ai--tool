import os 
from openai import OpenAI ,APIConnectionError
from dotenv import load_dotenv
from google import genai
Provider="hosted"
LOCAL_MODEL = "qwen2.5:3b"
HOSTED_MODEL = "gemini-3.8-flash"
#HOSTED_MODEL = " not gemini-3.8-flash" # to check the try and except in the hosted condition 
def normalized_output (provider,model,message):
   return{
    "provider": provider,
    "model": model,
    "answer": message
}
def route_request(prompt, Provider):
    if Provider == "local" :
      try:
        client = OpenAI(
            base_url="http://localhost:11434/v1", 
            api_key="ollama"
         )
        response = client.chat.completions.create(
            model=LOCAL_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            #max_tokens=100SSS
         )
        return (normalized_output("local",LOCAL_MODEL,response.choices[0].message.content))
      except APIConnectionError :
         return("Cannot connect to Ollama. Make sure the Ollama server is running on port 11434.")
    elif Provider == "hosted" :
        load_dotenv() 
        api_key = os.getenv("GEMINI_API_KEY")
        #api_key = os.getenv("NOt _GEMINI_API_KEY")
        if api_key:
          try: 
           client=genai.Client(api_key=api_key)
           response = client.models.generate_content(
            model=HOSTED_MODEL,
            contents=prompt
        )
           return(normalized_output("hosted",HOSTED_MODEL,response.text))
    # Network / DNS / SSL Connection Errors
          except ConnectionError as e:
             return("Failed to connect to Host API.")
          except Exception as e:
             print("Error type:", type(e).__name__)
             print("HTTP status:", getattr(e, "code", "Not available"))
             return("Gemini request failed. Check the model ID, credentials, quota, or connection.")
        else :
           return("key not found please create a key and if you have one make sure it's reachable ")
    else :
        return ("INVALID MODE")
#WE  USE PROVIDER FLAG AS THE SECOND ARG FOR ROUTE REQUEST FUN
#print(route_request("Explain what GGUF is.", Provider))
#TEST IF WE USE MODE AS THE SECOND ARG FOR ROUTE REQUEST FUNC
#print(route_request("Explain GGUF in exactly three sentences. Include its purpose, one advantage, and one limitation.",Provider= "local"))
print(route_request("Explain GGUF in exactly three sentences. Include its purpose, one advantage, and one limitation.", Provider="hosted"))