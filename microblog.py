from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """Creates shell context with db instance and models"""
    return {'db': db, 'User': User, 'Post': Post}
