from flask import Flask, render_template
app = Flask(__name__)
# You're going to want to disable this during production.
# This enables the runtime debugger and error pages.
# additionally makes changes reload the python process.
app.debug = True

from flask import request
# This example requires the request variable.


@app.route("/", methods=["GET","POST"]) # We have to tell flask we want this view 
                                        # to listen for POST and GET
def hello():
    # Define the right password.
    correct_password = "1337HAXOR"
    # Set the initial state for "Should show secret"
    should_show_secret = False

    if request.method == "POST" and request.form.get("password") == correct_password:
        # The user POSTED the form AND the field "password" was 
        # set and it is the right password. 
        # Show the secret content to the user
        should_show_secret = True


    return render_template('my_template.html', 
        should_show_secret=should_show_secret,
        )

if __name__ == "__main__":
    app.run()