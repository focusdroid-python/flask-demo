# coding:utf-8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap




app = Flask(__name__, template_folder='../templates',static_folder="",static_url_path="")

@app.route('/')
def index():
    data = {
        "name": "focus",
        "age": 30,
        "my_dict": {"city": "xian"}
    }
    # return render_template("index.html", name="focusdroid", age=18)
    return render_template("index.html", **data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

bootstrap = Bootstrap(app)