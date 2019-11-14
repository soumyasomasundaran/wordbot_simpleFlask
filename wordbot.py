from flask import Flask,render_template,request
from PyDictionary import PyDictionary
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/solution.html')
def solution():
    dictionary = PyDictionary()
    command=request.args.get('command')
    if command=='hello':
        word = "hello there! How are you"
    elif (command.split()[0])=='meaning':
        word = dictionary.meaning(command.split()[1])
        print (word)
    elif (command.split()[0])=='synonym':
        word = dictionary.synonym(command.split()[1])
        print(word)
    elif (command.split()[0])=='antonym':
        word = dictionary.antonym(command.split()[1])
        print(word)
    elif (command.split()[0])=='bye':
        Word= "Thank you! Bye"
    return render_template('solution.html', word=word)


if __name__=='__main__':
    app.run(debug=True)
