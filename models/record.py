from database.db import db

class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # income / expense
    category = db.Column(db.String(50))
    date = db.Column(db.String(20))
    notes = db.Column(db.String(255))