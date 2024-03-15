from apps import app, db
from apps.model import *    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()