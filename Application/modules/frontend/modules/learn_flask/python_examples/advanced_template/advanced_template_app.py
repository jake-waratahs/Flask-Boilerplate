from flask import Flask, render_template
app = Flask(__name__)
# You're going to want to disable this during production.
# This enables the runtime debugger and error pages.
# additionally makes changes reload the python process.
app.debug = True


@app.route("/")
def hello():

    lowercase_text = "hello world, i am lower case at the moment"
    list_data = [
        (0, 'Item 1', 'A small description about me'),
        (1, 'Item 2', 'A small description about me'),
        (2, 'Item 3', 'A small description about me'),
        (3, 'Item 4', 'A small description about me'),
    ]

    should_show_secret = False


    return render_template('my_template.html', 
        list_data=list_data, 
        should_show_secret=should_show_secret,
        lowercase_text=lowercase_text,
        )

if __name__ == "__main__":
    app.run()