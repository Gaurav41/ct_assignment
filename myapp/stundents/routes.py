from flask import Blueprint, abort, jsonify,request
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from myapp.models import Student, Course
from myapp import db

student = Blueprint("student",__name__)

@student.route("/student",methods=['POST'])
@jwt_required()
def add_student():
    try:
        name = request.json.get("name")
        email = request.json.get("email")
        phone = request.json.get("phone")

        # validation

        if not (name and email and phone):
            return jsonify({"error":"All field are mandatory"}),400
        
        student = Student.query.filter(or_(Student.phone==phone, Student.email==email)).first()
        if student:
            return jsonify({"message":"student with same name or email already exist"}),209
        
        student = Student(name=name,email=email,phone=phone)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message":"Student added"}),201
    except Exception as e:
        print(e)
        abort(500)

@student.route("/students",methods=['GET'])
@jwt_required()
def get_students():
    students = Student.query.all()
    result = []
    for student in students:
        # courses = []
        # courses_mapping = Student_course_mapping.query.filter_by(student_id=student.id).all()
        # for c in courses_mapping:
        #     course = Course.query.get_or_404(int(c.course_id))
        #     courses.append({"id":course.id,"course":course.name})
        courses = []
        for course in student.courses:
            courses.append({'id': course.id, 
                            'name': course.name, 
                            'professor_name': course.professor_name, 
                            'description': course.description
                            })
        result.append({
            "id":student.id,
            "name":student.name,
            "email": student.email,
            "phone":student.phone,
            "courses":courses 
        })

    return jsonify({"students":result}),200

@student.route("/student/<int:id>",methods=['GET'])
@jwt_required()
def get_student_by_id(id):
    student = Student.query.get_or_404(int(id))
    result = {
            "id":student.id,
            "name":student.name,
            "email": student.email,
            "phone":student.phone 
        }
    return jsonify({"student":result}),200

@student.route('/students/<int:id>/courses', methods=['GET'])
@jwt_required()
def get_student_courses(id):
    student = Student.query.get(id)
    if student:
        courses = []
        for course in student.courses:
            courses.append({'id': course.id, 
                            'name': course.name, 
                            'professor_name': course.professor_name, 
                            'description': course.description
                            })
        result= {'id': student.id, 
                 'name': student.name, 
                 'email': student.email, 
                 'phone': student.phone,        
                'courses': courses
                }
        return jsonify({"student":result})
    else:
        return jsonify({'error': 'Student not found'}), 404

@student.route('/students/<int:student_id>/assign_course', methods=['POST'])
@jwt_required()
def assign_course_to_student(student_id):
    student = Student.query.get(student_id)

    if not student:
        return jsonify({'message': 'Student not found'}), 404

    course_ids = request.json.get('course_ids', [])

    for course_id in course_ids:
        course = Course.query.get(course_id)
        if course:
            student.courses.append(course)
        else:
            return jsonify({'message': f'Course with id {course_id} not found'}), 404

    db.session.commit()
    return jsonify({'message': 'Coursess assigned successfuly'}), 200


@student.route("/student/<int:id>",methods=['DELETE'])
@jwt_required()
def delete_student(id):
    student = Student.query.get_or_404(int(id))
    if student:
        db.session.delete(student)
        db.session.commit()
    return jsonify({}),204




# @student.route("/test_students",methods=['GET'])
# @jwt_required()
# def courses_and_students():
#     try:
#         # course = Course.query.get_or_404(int(id))
#         students = Student.query.all()
#         result = []
#         for student in students:
#             courses = []
#             courses_mapping = Student_course_mapping.query.filter_by(student_id=student.id).all()
#             for c in courses_mapping:

#                 course = Course.query.get_or_404(int(c.course_id))
#                 courses.append({"id":course.id,"course":course.name})


#             result.append({
#                 "id":student.id,
#                 "name":student.name,
#                 "email": student.email,
#                 "phone":student.phone,
#                 "courses":courses 
#             })
#         return jsonify({"students":result}),200
#     except Exception as e:
#         raise e
#         # abort(500)    
    
    
