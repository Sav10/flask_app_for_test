from flask import Flask, render_template, request
MyApp = Flask(__name__)

var_01 = "this is my first var"

@MyApp.route("/")
def hello():
	return render_template('index.html', title = 'Home')

@MyApp.route("/about")
def about():
	return render_template('about.html', title = 'About', my_first_var = var_01)


@MyApp.route("/contact")
def contact():
	return render_template('contact.html', title = 'Contact')

if __name__ == "__main__":
	MyApp.run(debug=True)
