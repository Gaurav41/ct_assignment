1. register user
POST:  http://127.0.0.1:5000/api/auth/register
Payload: {
    "username":"gaurav",
    "email": "gaurav@gmail.com",
    "password": "123"
}

2. login
POST: http://127.0.0.1:5000/api/auth/login
Payload: {
    "username":"gaurav",
    "password": "123"
}
Response:
{
    "message": "login successfull",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
}

Use this token for all below requests

Courses
1. Add Courses
    POST: http://127.0.0.1:5000/api/course

    Payload: {
    "course_name":"python",
    "professor_name":"prof_1",
    "description":"some description"
    }

    Response:
    {
        "message": "course added"
    }

2. get all courses
GET: http://127.0.0.1:5000/api/courses

3. Get course by   (only course)
GET http://127.0.0.1:5000/api/course/2

3. Get course by and associated students
    GET http://127.0.0.1:5000/api/course/<'course_id'>/
    eg:
    http://127.0.0.1:5000/api/course/1/students

4. delete Course by id
DELETE http://127.0.0.1:5000/api/course/2

5. Assign course to student
POST: http://127.0.0.1:5000/api/students/<'stu_id'>/assign_course

    eg:
http://127.0.0.1:5000/api/students/1/assign_course

Payload: {
    "course_ids":[1,2]
}

assign course 1,2 to student whose 1

Students
1. Add Students
POST: http://127.0.0.1:5000/api/student

    Payload: {
    "name":"gauravpingale",
    "email": "ak@gmail.com",
    "phone": 9767916589
    }

2. Get students (with courses)
 GET: http://127.0.0.1:5000/api/students

    Payload: {
    "students": [
        {
            "courses": [
                {
                    "description": "some description",
                    "id": 1,
                    "name": "python",
                    "professor_name": "prof_1"
                }
            ],
            "email": "ak@gmail.com",
            "id": 1,
            "name": "gauravpingale",
            "phone": 9767916589
        }
    ]
}

