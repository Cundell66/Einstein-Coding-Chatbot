from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def execute(prompt):
  completion = client.chat.completions.create(
      model="llama3-70b-8192",
      messages=[
          {
              "role": "user",
              "content": prompt
          },
      ],
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      stream=True,
      stop=None,
  )

  response = ''
  for chunk in completion:
      response += chunk.choices[0].delta.content or ""
  
  return response

if __name__ == "__main__":
  print(execute("Tell a joke"))