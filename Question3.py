from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

@app.route('/store_polling_unit_result', methods=['GET', 'POST'])
def store_polling_unit_result():
    if request.method == 'POST':
        # Retrieve the form data
        polling_unit_id = request.form.get('polling_unit_id')
        party_a_votes = request.form.get('party_a_votes')
        party_b_votes = request.form.get('party_b_votes')
        party_c_votes = request.form.get('party_c_votes')
        # Add more fields as needed

        # Store the results in the database
        cursor.execute("INSERT INTO polling_unit_results (polling_unit_id, party_a_votes, party_b_votes, party_c_votes) VALUES (?, ?, ?, ?)", (polling_unit_id, party_a_votes, party_b_votes, party_c_votes))
        # Commit the changes to the database
        conn.commit()

        # Redirect to a success page or any other desired page
        return redirect('/success')
    
    # Render the template with the form
    return render_template('store_polling_unit_result.html')

  
if __name__ == '__main__':
    app.run()
