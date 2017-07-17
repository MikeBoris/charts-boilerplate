from flask import Flask
from flask import render_template
import sqlite3
import pandas as pd
import numpy as np

app = Flask(__name__)

DATABASE = 'data/TEST_DB.db'

query = """
select * from fruit;
"""

@app.route('/<name>')
def charts(name):
	cnxn = sqlite3.connect(DATABASE)
	df = pd.read_sql_query(query, cnxn)
	data = df.to_json(orient='index')
	title = name
	return render_template('index.html', name=name, title=title, data=data)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)