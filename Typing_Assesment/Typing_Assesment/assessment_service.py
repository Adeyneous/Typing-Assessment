from repository import UserRepository, AssessmentRepository
from db_connection import get_db_session



# Handling Assessment 

def record_assessment_result(user_id, wpm, accuracy):
    assessment_repo = AssessmentRepository(get_db_session)
    assessment_repo.create_assessment_result(user_id, wpm, accuracy)
    # Additional logic to handle the assessment result

def email_assessment_results_to_admin(user_id):
    # Logic to fetch assessment results and email them to the admin
    pass
