from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

@app.route('/polling_unit_result', methods=['GET'])
def polling_unit_result():
    # Get the polling unit ID from the request URL
    polling_unit_id = request.args.get('polling_unit_id')

    # Retrieve the result from the database
    cursor.execute("SELECT * FROM polling_unit_results WHERE polling_unit_id=?", (polling_unit_id,))
    result = cursor.fetchone()

    # Render the template with the result data
    return render_template('polling_unit_result.html', result=result)

if __name__ == '__main__':
    app.run()
