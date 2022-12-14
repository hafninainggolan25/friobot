from process import preparation, generate_response
from flask import Flask, render_template, request
from nltk.stem import WordNetLemmatizer

# download nltk



#Start Chatbot
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    print(user_input)
    result = generate_response(user_input)
    print(result)
    return result

if __name__ == "__main__":
    app.run(debug=True)