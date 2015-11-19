from flask import Flask, render_template
MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	return render_template('index.html')

@MyApp.route("/about")
def about():
	return render_template('about.html')


@MyApp.route("/contact")
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	MyApp.run(debug=True)
