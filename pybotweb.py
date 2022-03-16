from bottle import route, run, template # 関数をインポート
from datetime import datetime # datetimeをインポート

@route('/hello')
def hello():
    now = datetime.now() # 現在時刻を取得
    return template('Hello World! {{now}}', now=now) # template関数の利用

run(host='localhost', port=8080, debug=True)
