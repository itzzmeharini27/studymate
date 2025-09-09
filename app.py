from flask import Flask,render_template,request,jsonify
app=Flask(__name__ )
@app.route('/')
def home():
 return render_template('index.html') 
@app.route('/ask',methods=['POST'])
def ask():
    user_message=request.json.get('message')
    if 'hello' in user_message.lower():
        bot_response="Hi! ?How can i help you study today?"
    elif 'exam' in user_message.lower():
            bot_response="Don't worry! make a study plan,and take small breaks."
    else:
                bot_response="i am here to help you. ask me anything!"
                return jsonify({'response':bot_response})
    if __name__=='__main__':
                app.run(debug=True)
