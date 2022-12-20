from flask import Flask, render_template, request
import sqlite3

app = Flask(name)

@app.route('/do-master-data')
def do_master_data():

# Connect to database
conn = sqlite3.connect('do_master.db')
cursor = conn.cursor()

# Fetch DO Master data from database
cursor.execute("SELECT * FROM do_master")
do_master_data = cursor.fetchall()

# Close connection to database
conn.close()

# Render DO Master data on page #1.0 with server-side pagination and search enabled
return render_template('do_master_data.html', do_master_data=do_master_data)

# Define route to display DO Master data on page #1.1

@app.route('/do-master-data-inline-edit')
def do_master_data_inline_edit():

# Connect to database
conn = sqlite3.connect('do_master.db')
cursor = conn.cursor()

# Fetch DO Master data from database
cursor.execute("SELECT * FROM do_master")
do_master_data = cursor.fetchall()

# Close connection to database
conn.close()

# Render DO Master data on page #1.1 with inline edit enabled for Enabled fields
return render_template('do_master_data_inline_edit.html', do_master_data=do_master_data)

@app.route('/do-master-data-inline-edit/update', methods=['POST'])
def do_master_data_inline_edit_update():

# Connect to database
conn = sqlite3.connect('do_master.db')
cursor = conn.cursor()

# Get updated values for Enabled fields from request
enabled = request.form['enabled']
do_master_id = request.form['do_master_id']

# Update DO Master data in database
cursor.execute("UPDATE do_master SET enabled=? WHERE do_master_id=?", (enabled, do_master_id))
conn.commit()

# Close connection to database
conn.close()

# Return success message
return 'Success'

@app.route('/add-do-master-data')
def add_do_master_data():

# Render modal/page for adding DO Master data on page #2
return render_template('add_do_master_data.html')

@app.route('/add-do-master-data/submit', methods=['POST'])
def add_do_master_data_submit():

# Connect to database

conn = sqlite3.connect('do_master.db')
cursor = conn.cursor()

# Get DO Master data from form submission
do_number = request.