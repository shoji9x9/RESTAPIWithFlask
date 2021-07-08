"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, jsonify
import my_func

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def get_json():
    num = request.args.get("number")

    if num is None:
        message = 'クエリパラメーターnumberを追加し再リクエストして下さい。'
    else:
        num = int(num)
        divisors = my_func.make_divisors(num)
        dict_list = []
        for i, d in enumerate(divisors):
            x = dict(id=i+1, value=d)
            dict_list.append(x)
        message = jsonify(dict_list)

    return message

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
