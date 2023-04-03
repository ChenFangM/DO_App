from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/tedxsd") 
def tedx():
    # return render_template('tedxsd.html') 
    return render_template('t.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(host='0.0.0.0')
