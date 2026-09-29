from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ans_query():                             
    data = request.get_json()                 
    question = data.get("message", "")        

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Act like a helpful personal assistant"},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=512
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply}), 200

@app.route("/summarize", methods=["POST"])
def summarize_email():                        
    data = request.get_json()                
    email_text = data.get("email", "")       
    prompt = f"Summarize the following email in 2-3 sentences: {email_text}"

    response = client.chat.completions.create( 
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Act like an expert email assistant"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512
    )

    summary = response.choices[0].message.content.strip()
    return jsonify({"summary": summary}), 200

if __name__ == "__main__":
    app.run(debug=True)

