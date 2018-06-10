from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    project_description = db.Column(db.String(1000))
    key_words = db.Column(db.String(1000))
    project_title = db.Column(db.String(1000))

    def __repr__(self):
        return '<Project {}>'.format(self.project_title)
