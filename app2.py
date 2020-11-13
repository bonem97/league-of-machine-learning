from flask import Flask, render_template, redirect, jsonify
from flask_cors import CORS, cross_origin



app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'

@app.route("/data/<username>")
def testinput(username):
    print(username)
    import riot_api_2
    uservalue = riot_api_2.ten_minute_data(username)
    print(uservalue)
    return jsonify(uservalue)

if __name__ == "__main__":
    app.run()