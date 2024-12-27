from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection

app = Flask(__name__)

# Root route: Redirect to home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for patient registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone']
        address = request.form['address']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO patients (name, age, gender, phone, address) VALUES (%s, %s, %s, %s, %s)',
            (name, age, gender, phone, address)
        )
        conn.commit()

        # Get the patient_id of the newly inserted patient
        cursor.execute('SELECT id FROM patients WHERE name = %s AND phone = %s', (name, phone))
        patient_id = cursor.fetchone()[0]

        # Add the patient to the queue automatically
        cursor.execute('INSERT INTO queue (patient_id, status) VALUES (%s, "Waiting")', (patient_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('queue'))

    return render_template('register.html')

# Route to display the patient queue
@app.route('/queue')
def queue():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT q.token_id, p.name, q.status FROM queue q JOIN patients p ON q.patient_id = p.id'
    )
    patients_queue = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('queue.html', patients=patients_queue)

# Route to add patients to queue
@app.route('/add_to_queue/<int:patient_id>')
def add_to_queue(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the patient exists in the patients table
    cursor.execute('SELECT * FROM patients WHERE id = %s', (patient_id,))
    patient = cursor.fetchone()

    if patient:
        # Check if the patient is already in the queue
        cursor.execute('SELECT * FROM queue WHERE patient_id = %s AND status = "Waiting"', (patient_id,))
        existing_patient = cursor.fetchone()

        if not existing_patient:
            # Insert the patient into the queue
            cursor.execute('INSERT INTO queue (patient_id, status) VALUES (%s, "Waiting")', (patient_id,))
            conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('queue'))

# Route to handle patient consultation (GET request for form)
@app.route('/consult/<int:token_id>', methods=['GET'])
def consult(token_id):
    # Retrieve the patient's details from the queue
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT p.name, q.token_id FROM queue q JOIN patients p ON q.patient_id = p.id WHERE q.token_id = %s',
        (token_id,)
    )
    patient = cursor.fetchone()
    cursor.close()
    conn.close()

    if patient:
        return render_template('consultation.html', token_id=token_id, patient_name=patient[0])
    else:
        return "Patient not found", 404

# Route to handle patient consultation (POST request to submit data)
@app.route('/consult/<int:token_id>', methods=['POST'])
def consult_patient(token_id):
    # Get the time components from the form
    hours = int(request.form['hours'])
    minutes = int(request.form['minutes'])
    am_pm = request.form['am_pm']
    diagnosis = request.form['diagnosis']

    # Convert to 24-hour format
    if am_pm == 'PM' and hours != 12:
        hours += 12
    if am_pm == 'AM' and hours == 12:
        hours = 0

    # Format time as HH:MM:SS
    consultation_time = f"{hours:02}:{minutes:02}:00"

    conn = get_db_connection()
    cursor = conn.cursor()

    # Update queue status and add consultation details
    cursor.execute(
        '''
        UPDATE queue
        SET status = 'Consulted', consultation_time = %s, diagnosis = %s
        WHERE token_id = %s
        ''',
        (consultation_time, diagnosis, token_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('queue'))

if __name__ == '__main__':
    app.run(debug=True)
