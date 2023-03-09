from flask import *
import json
import datetime
import openai
import os

# openai.api_key = os.environ["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"]
# openai.api_key = "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"
openai.api_key = ""


app = Flask(__name__)
app.config["Debug"] = True


def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

# def index():
#     return '''
#         <form action="/output" method="get">
#             <label for="user-input">Enter a string:</label>
#             <input type="text" id="user-input" name="user-input" />
#             <button type="submit">Submit</button>
#         </form>
#     '''



@app.route('/output', methods=['GET'])
def output():
    userInput = request.args.get('user-input')
    prompt = f"Generate a program to {userInput}."
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    program = response.choices[0].text.strip()
    # return f"You entered: {userInput}"
    return f"You entered: {program}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)



app.run()