from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return bot_response

def get_bot_response(message):
    message = message.lower()
    if 'hello' in message or 'hi' in message:
        return "Hello! How can I assist you today?"
    elif 'how are you' in message:
        return "I'm just a computer program, but thanks for asking!"
    elif 'bye' in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

if __name__ == '__main__':
    app.run(debug=True)
