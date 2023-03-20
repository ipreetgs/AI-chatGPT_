from flask import *
import json
import datetime
import openai
import os

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

# openai.api_key = "sk-**********"
#openai.api_key_path='apikey'
openai.api_key=os.environ.get('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError('API_KEY environment variable is not set')

# openai.api_key_path = '/Apikey.txt'

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
    # return f"You entered: {program}"
    return render_template('output.html', program=program)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)



app.run()