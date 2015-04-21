from flask import Flask
app = Flask(__name__)
# You're going to want to disable this during production.
# This enables the runtime debugger and error pages.
# additionally makes changes reload the python process.
app.debug = True


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()