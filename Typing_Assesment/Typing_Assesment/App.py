from flask import Flask, render_template, request, jsonify, session
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from repository import UserRepository, AssessmentRepository
 # Replace with your actual module name
from db_connection import get_db_session
from openai_client import OpenAI




app = Flask(__name__)
app.secret_key = 'FLASK_SECRET_KEY'  # Replace with a real secret key
app.permanent_session_lifetime = timedelta(minutes=5)  # Adjust as needed for your timer

# Initialize your data repositories
user_repo = UserRepository(get_db_session)
assessment_repo = AssessmentRepository(get_db_session)



@app.route('/')
def index():
    return render_template('index.html')  # Your main typing test page





@app.route('/generate-paragraph', methods=['GET'])
def generate_paragraph():
    try:
        openai_client = OpenAI('OPENAI_API_KEY')  # Ensure this is your actual API key
        paragraph = openai_client.generate_paragraph()
        return jsonify(paragraph=paragraph)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify(paragraph="An error occurred while generating the paragraph.")


@app.route('/submit-results', methods=['POST'])
def submit_results():
    user_input = request.form['user_input']
    original_text = request.form['original_text']
    time_taken = float(request.form['time_taken'])  # Time taken in seconds


    # Calculate WPM and accuracy
    wpm = calculate_wpm(user_input, time_taken)
    accuracy = calculate_accuracy(user_input, original_text)
    
    with get_db_session() as db_session:
        # Now db_session is a SQLAlchemy session you can use to interact with your database
        user_repo = UserRepository(db_session)
        assessment_repo = AssessmentRepository(db_session)

    # Save results to the database
    user_id = session.get('user_id')  # Assuming the user's ID is stored in session
    assessment_result = assessment_repo.create_assessment_result(user_id, wpm, accuracy)
    
    # Commit any changes you made
    db_session.commit()

    # Respond with the new result and the updated total
    return jsonify(success=True, wpm=wpm, accuracy=accuracy)

def calculate_wpm(typed_text, time_seconds):
    words = typed_text.split()
    num_words = len(words)
    minutes = time_seconds / 60
    return round(num_words / minutes, 2)

def calculate_accuracy(typed_text, original_text):
    # Logic to calculate the accuracy of typed_text compared to original_text
    # This can be as simple or complex as needed for your use case
    pass



@app.route('/generate-alphanumeric-data', methods=['GET'])
def generate_alphanumeric_data():
    # Logic to generate random alphanumeric data for the assessment
    # Replace this with actual data generation logic or integration with OpenAI
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "zip_code": "12345",
        "company": "Acme Corp",
        "position": "Developer"
    }
    return jsonify(data=data)

@app.route('/submit-alphanumeric-results', methods=['POST'])
def submit_alphanumeric_results():
    # Extract the input data and the original data
    user_input = request.json['user_input']
    original_data = request.json['original_data']
    time_taken = float(request.json['time_taken'])  # Time taken in seconds

    # Calculate WPM and accuracy for each field
    results = {}
    for field in original_data:
        typed_text = user_input.get(field, "")
        original_text = original_data[field]
        wpm = calculate_wpm(typed_text, time_taken)
        accuracy = calculate_accuracy(typed_text, original_text)
        results[field] = {
            "wpm": wpm,
            "accuracy": accuracy
        }
    
    # You might want to aggregate the results here
    # Save results to the database and respond with the result
    # ...

    return jsonify(success=True, results=results)

# ... existing functions ...

# You might need to update calculate_wpm and calculate_accuracy to handle
# alphanumeric inputs properly, including handling the case where the user
# has not completed the assessment when the time runs out.




if __name__ == '__main__':
    app.run(debug=True)
