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
    Hello World. Take a look at the user page for this user: 
    <a href="{link}">Profile Page</a>
    """.format(
        # We use the function name of the other controller to reference it.
        # Because this endpoint takes arguments, we need to specify what
        # value to give the arguments
        link=url_for('profile_page', user_id=200)
    )

@app.route("/user/<int:user_id>/")
def profile_page(user_id):
    return """
    This is the profile page for user with ID: {user_id}
    <a href="{link}">Other Page</a>
    """.format(
        link=url_for('hello'),
        user_id=user_id
    )

if __name__ == "__main__":
    app.run()