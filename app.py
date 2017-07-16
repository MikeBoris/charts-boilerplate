from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def main(name):
	title = name
	return render_template('index.html', name=name, title=title)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)