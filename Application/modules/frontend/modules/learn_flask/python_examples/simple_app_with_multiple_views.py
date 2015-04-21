from flask import Flask
app = Flask(__name__)
# You're going to want to disable this during production.
# This enables the runtime debugger and error pages.
# additionally makes changes reload the python process.
app.debug = True

from flask import url_for

@app.route("/")
def hello():
    # Render some HTMl and insert a variable using Python's format string method.
    return """
    Hello World. Take a look at the other page with a stupid path: 
    <a href="{link}">Other Page</a>
    """.format(
        # We use the function name of the other controller to reference it.
        link=url_for('stupid_path')
    )

@app.route("/my-super-awesome-long-path-that-will-change-in-the-future")
def stupid_path():
    return """
    Hello World. Take a look at the other page here: 
    <a href="{link}">Other Page</a>
    """.format(
        link=url_for('hello')
    )

if __name__ == "__main__":
    app.run()