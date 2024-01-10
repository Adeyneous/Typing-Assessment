from sqlalchemy.orm import Session
from .models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, username, email, hashed_password):
        new_user = User(username=username, email=email, hashed_password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def update_user(self, user_id, **kwargs):
        user = self.session.query(User).filter_by(id=user_id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    

# Assuming User and AssessmentResult are SQLAlchemy models you've defined

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_user(self, username, hashed_password):
        # Logic to add a new user
        pass

    def get_user(self, username):
        # Logic to fetch a user by username
        pass

    # Add other necessary user-related data access functions here

class AssessmentRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_assessment_result(self, user_id, wpm, accuracy):
        # Logic to add a new assessment result
        pass

    def get_assessment_results(self, user_id):
        # Logic to fetch all assessment results for a user
        pass

    # Add other necessary assessment-related data access functions here

    



  
