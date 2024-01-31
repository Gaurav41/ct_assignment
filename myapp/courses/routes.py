from flask import Blueprint, abort, jsonify,request
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from myapp.models import Student, Course
from myapp import db

course = Blueprint("course",__name__)

@course.route("/course",methods=['POST'])
@jwt_required()
def add_course():
    try:
        name = request.json.get("course_name")
        professor_name = request.json.get("professor_name")
        description = request.json.get("description")

        # validation

        if not (name and professor_name and description):
            return jsonify({"error":"All field are mandatory"}),400
        
        course = Course.query.filter_by(name=name).first()
        if course:
            return jsonify({"message":"course with same name or email already exist"}),209
        
        course = Course(name=name,professor_name=professor_name,description=description)
        db.session.add(course)
        db.session.commit()
        return jsonify({"message":"course added"}),201
    except Exception as e:
        print(e)
        abort(500)


@course.route("/courses",methods=['GET'])
@jwt_required()
def get_courses():
    all_courses = Course.query.all()
    result = []
    for course in all_courses:
        # students = []
        # courses_mapping = Student_course_mapping.query.filter_by(course_id=course.id).all()
        # for s in courses_mapping:
        #     student = Student.query.get_or_404(int(s.student_id))
        #     students.append({"id":student.id,"course":student.name})
        students = [{'id': student.id, 'name': student.name, 'email': student.email, 'phone': student.phone} for student in course.students]

        result.append({
            "id":course.id,
            "course_name":course.name,
            "professor_name": course.professor_name,
            "description":course.description,
            "student":students
        })

    return jsonify({"courses":result}),200


@course.route("/course/<int:course_id>/students",methods=['GET'])
@jwt_required()
def get_course_students(course_id):
    course = Course.query.get(course_id)
    if course:
        students = [{'id': student.id, 'name': student.name, 'email': student.email, 'phone': student.phone} for student in course.students]
        result={
            "id":course.id,
            "course_name":course.name,
            "professor_name": course.professor_name,
            "description":course.description,
            "students":students 
        }
        return jsonify({"courses":result}),200
    else:
        return jsonify({'message': 'Course not found'}), 404
    

@course.route("/course/<int:id>",methods=['GET'])
@jwt_required()
def get_course_by_id(id):
    course = Course.query.get_or_404(int(id))
    result = {
            "id":course.id,
            "name":course.name,
            "professor_name": course.professor_name,
            "description":course.description, 
        }
    return jsonify({"course":result}),200


@course.route("/course/<int:id>",methods=['DELETE'])
@jwt_required()
def delete_course(id):
    course = Course.query.get_or_404(int(id))
    if course:
        db.session.delete(course)
        db.session.commit()

    return jsonify({}),204


# @course.route("/test_students",methods=['GET'])
# @jwt_required()
# def courses_and_students():
    try:
        # course = Course.query.get_or_404(int(id))
        students = Student.query.all()
        result = []
        for student in students:
            courses = []
            courses_mapping = Student_course_mapping.query.filter_by(student_id=student.id).all()
            for c in courses_mapping:

                course = Course.query.get_or_404(int(c.course_id))
                courses.append({"id":course.id,"course":course.name})


            result.append({
                "id":student.id,
                "name":student.name,
                "email": student.email,
                "phone":student.phone,
                "courses":courses 
            })
        return jsonify({"students":result}),200
    except Exception as e:
        raise e
        # abort(500)    