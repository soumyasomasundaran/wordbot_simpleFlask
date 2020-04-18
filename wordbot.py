from flask import Flask, render_template, request, jsonify
import look
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', )


@app.route('/solution', methods=['POST'])
def solution():
    word = ''
    command = request.form['command']
    if command == 'hello':
        word = "hello there! How are you"
    elif (command.split()[0]) == 'meaning':
        word = look.meaning(command.split()[1])
    elif (command.split()[0]) == 'synonym':
        word = look.synonym(command.split()[1])
    elif (command.split()[0]) == 'antonym':
        word = look.antonym(command.split()[1])
    elif (command.split()[0]) == 'bye':
        word = "Thank you! Bye"

    if word:
        word = str(word)
        return jsonify({'name': word})
    else:
        return jsonify({'error': 'Wrong command!'})


if __name__ == '__main__':
    app.run(debug=True)
