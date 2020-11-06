import os
from flask import Flask, jsonify, render_template
import psycopg2


con = psycopg2.connect(
        database= "league_of_ML",
        user = "postgres",
        password = "erjufoc9")

cur = con.cursor()

cur.execute("select * from league")

rows = cur.fetchall()

cur.execute("Select * FROM league LIMIT 0")
colnames = [desc[0] for desc in cur.description]


con.close()
con.close()

app = Flask(__name__)



@app.route("/")
def home():
    return 'hi'


@app.route("/api/")
def api():
    list1 = []
    for r in rows:
        newdict = {}
        for i in range(len(colnames)):
            newdict[colnames[i]] = r[i]
        list1.append(newdict)


    return jsonify(list1)


if __name__ == "__main__":
    app.run(debug=True)
