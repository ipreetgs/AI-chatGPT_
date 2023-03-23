from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.String(256), nullable=False)
    output_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Program {self.id}>'
