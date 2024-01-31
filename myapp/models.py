from myapp import db


from myapp import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    


enrollment = db.Table('enrollment',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    courses = db.relationship('Course', secondary=enrollment, back_populates='students')


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True, nullable=False)
    professor_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    students = db.relationship('Student', secondary=enrollment, back_populates='courses')


# class Student_course_mapping(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
#     course_id = db.Column(db.Integer, db.ForeignKey('course.id'))







