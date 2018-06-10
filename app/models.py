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


class Professors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    score = db.Column()
    department = db.Column()
    field = db.Column()
    key_words = db.Column()
    pt_abstractt = db.Column()

    def __repr__(self):
        return '<Professor {}>'.format(self.name)
