from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from flask import session, redirect, url_for, flash
from functools import wraps
from repository import UserRepository
from db_connection import get_db_session



# Password Hashing

def hash_password(password):
    return generate_password_hash(password)

def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def authenticate_user(username, password):
    user_repo = UserRepository(get_db_session)
    user = user_repo.get_user(username)
    if user and check_password_hash(user.hashed_password, password):
        # User is authenticated
        pass
    else:
        # User authentication failed
        pass


# Session Management

def log_in_user(user_id):
    session['user_id'] = user_id  # Stores the user's ID in the session

def log_out_user():
    session.pop('user_id', None)  # Removes the user's ID from the session
    
# Access Control

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to be logged in to view this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

