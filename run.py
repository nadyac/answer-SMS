from flask import Flask, request, redirect
import twilio.twiml
import os
 
app = Flask(__name__)

questions_answers = {
    "What is data?": "Facts about a real-world object",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    
    inSMS = request.values.get('Body', None)
    if inSMS in questions_answers:
        message = questions_answers[inSMS] + ", is the answer!"
    else:
        message = "You're a Monkey and I won't answer your question. Thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
    
    
    return str(resp)
 
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=8080, debug=True)