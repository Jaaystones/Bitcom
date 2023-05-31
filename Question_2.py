from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Retrieve the list of local governments from the database
cursor.execute("SELECT local_government_id, local_government_name FROM local_governments WHERE state_id=?", (25,))
local_governments = cursor.fetchall()




@app.route('/local_government_result', methods=['GET'])
def local_government_result():
    # Get the local government ID from the request URL
    local_government_id = request.args.get('local_government_id')

    # Retrieve the summed total result from the database
    cursor.execute("SELECT SUM(party_a_votes), SUM(party_b_votes), SUM(party_c_votes) FROM polling_unit_results WHERE local_government_id=?", (local_government_id,))
    result = cursor.fetchone()

    # Render the template with the result data
    return render_template('local_government_result.html', result=result)
  return render_template('local_government_result.html', summed_result=summed_result, local_governments=local_governments)


  
  
  
if __name__ == '__main__':
    app.run()
