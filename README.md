## Application Setup
1. Install Python (3.12) 
2. Clone this repo, cd to ct_assignment
3. Create and activate virtual environment
    
    Run below commands in cmd/terminal:

    `python -m venv vevn`

    `venv\Scripts\activate`

4. Install required packages

    `pip install -r requirements.txt`

5. Run Flask App

    `python app.py`

6. Application will start running on http://127.0.0.1:5000,
    
## Setup database

    Run following commands in cmd to setup sqlite database
    >`flask shell`
    it will open flask shell
    To create all tables, run
    >`from myapp import db`
    >'db.create_all()`

## API's

#### 1. Auth
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

Use this token for all below requests, send the token in authorisation header as Bearer token


#### 2. Courses
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

#### 1. Students
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

3. Get student with ID (without course)
GET: http://127.0.0.1:5000/api/student/1

4. Get Student with ID with enrolled courses
GET: http://127.0.0.1:5000/api/students/<'student_id'>/courses

        Response: {
            "courses": {
                "course_name": "python",
                "description": "some description",
                "id": 1,
                "professor_name": "prof_1",
                "students": [
                    {
                        "email": "ak@gmail.com",
                        "id": 1,
                        "name": "gauravpingale",
                        "phone": 9767916589
                    }
                ]
            }
        }   


