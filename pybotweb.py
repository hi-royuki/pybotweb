from bottle import route, run, template, request # 関数をインポート
from pybot import pybot
@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text="") # template関数の利用

@route('/hello', method='POST')
def do_hello():
    input_text = request.forms.input_text
    output_text = pybot(input)
    return template('pybot_template', input_text=input_text, output_text=output_text)

run(host='localhost', port=8080, debug=True)
