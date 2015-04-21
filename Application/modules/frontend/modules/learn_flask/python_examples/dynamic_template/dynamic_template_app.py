from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello():
	# Lets do a calculation which the template takes the result of
	my_text_variable = "Hello World"
	my_integer_variable = 99 * 100

    return render_template('my_template.html', 
    	my_integer_variable=my_integer_variable, 
    	my_text_variable=my_text_variable)

if __name__ == "__main__":
    app.run()