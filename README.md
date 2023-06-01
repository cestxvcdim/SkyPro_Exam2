# SkyPro <img src="https://github.com/cestxvcdim/skypro_static/blob/main/icons/skypro_logo.png" width="35">

## Exam at the end of second semester

---

### About project:

- It is simple application on `Flask` with based `API` *(CRUD)*
- Application runs from `Docker` container <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" width="25">
- Realize `CI/CD` logic and deploy at server with `GitHub Actions`

---

### Requirements:

```python
aniso8601==9.0.1
attrs==23.1.0
blinker==1.6.2
click==8.1.3
exceptiongroup==1.1.1
Flask==2.3.2
flask-restx==1.1.0
Flask-SQLAlchemy==3.0.3
iniconfig==2.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.17.3
MarkupSafe==2.1.2
marshmallow==3.19.0
packaging==23.1
pluggy==1.0.0
psycopg2-binary==2.9.6
PyJWT==2.7.0
pyrsistent==0.19.3
pytest==7.3.1
pytz==2023.3
SQLAlchemy==2.0.15
tomli==2.0.1
typing_extensions==4.6.1
Werkzeug==2.3.4
```

---

### How to use:

---

#### You can use `vvladimirov.space` address and send your requests on this site, or you can do it from your local machine

---

1) Copy this project on your local machine `git clone https://github.com/cestxvcdim/SkyPro_Exam2.git`
2) Write in a terminal this command `docker-compose up --build -d`
3) Open an application, which can send **GET/POST/PUT/DELETE** methods, f.e `Postman` and write in the browse page this address `http://localhost/`
4) Write your request and push "SEND" button
5) Receive a response in `JSON` format from the application

---

### Examples:

#### Request: GET http://localhost/notes

#### Response:

```json
[
    {
        "id": 1, 
        "subject": "Coding", 
        "lecture_date": "01.01.2023",
        "full_name": "Ivan Fufaev",
        "class_number": 200
    }, 
    {
        "id": 2, 
        "subject": "Mathematics", 
        "lecture_date": "31.12.2023",
        "full_name": "Nikolay Ivanov",
        "class_number": 303
    }, 
    {
        "id": 3, 
        "subject": "Physics", 
        "lecture_date": "18.05.2023",
        "full_name": "George Soloviev",
        "class_number": 100
    }
]
```

#### Request: GET http://localhost/notes/2

#### Response:

```json
{
    "id": 2, 
    "subject": "Mathematics", 
    "lecture_date": "31.12.2023",
    "full_name": "Nikolay Ivanov",
    "class_number": 303
}
```

#### Request: POST http://localhost/notes

```json
{
    "subject": "English", 
    "lecture_date": "21.10.2023",
    "full_name": "Ksenya Golovina",
    "class_number": 17
}
```

#### Response:

```json
{
    "id": 4,
    "subject": "English", 
    "lecture_date": "21.10.2023",
    "full_name": "Ksenya Golovina",
    "class_number": 17
}
```

#### Request: PUT http://localhost/notes/3

```json
{
    "subject": "New subject", 
    "lecture_date": "09.04.2023",
    "full_name": "New teacher",
    "class_number": 15
}
```

#### Response: 

```json
{
    "id": 3,
    "subject": "New subject", 
    "lecture_date": "09.04.2023",
    "full_name": "New teacher",
    "class_number": 15
}
```

#### Request: DELETE http://localhost/notes/2

#### Response:

```json
{
    "message": "Lecture has deleted successfully"
}
```
---

## Virtual machine supported by _Yandex Cloud_<img src="https://github.com/cestxvcdim/skypro_static/blob/main/icons/yandex_logo.png" width="45">
