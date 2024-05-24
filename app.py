import os
from flask import render_template, Flask, redirect, request
import jinja_partials
import uuid
from text2speech import text2speech
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

app = Flask(__name__)
jinja_partials.register_extensions(app)


# client = OpenAI(api_key=OPENAI_API_KEY)


messages = [
    {
        "role": "system",
        "content": """
            You are Albert, the worlds most accomplished computer science chatbot.
            You are prolific in coding languages such as Python, JavaScript, Go, CrystalLang and C# and their associated frameworks.
            Whenever possible provide code snippets to help demonstrate your response and when not possible ask closed questions until it is possible.
            """
    },

]

def add_messages(role, content):
    messages.append({"role": role,"content": content})

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        prompt = "hi"
    else:
        prompt = request.form.get("query")
    if prompt == "":
        redirect ("index.html")
    add_messages("user", prompt)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    answer = response.choices[0].message.content
    add_messages("assistant", answer)
    sound_file = text2speech(answer)
    unique_id = str(uuid.uuid4())
    return render_template("index.html", response=answer, sound_file = sound_file, unique_id = unique_id)
