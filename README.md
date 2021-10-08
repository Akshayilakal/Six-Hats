# Six-Hats
## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Clone code

Please use below command to clone the code the local machine.

`git clone https://github.com/Akshayilakal/Six-Hats.git`

Navigate to root directory

`cd Six-Hats/App1`

Create virtual environment, install pipenv if not present

`pip3 install pipenv`

`pipenv shell`

Install dependencies

`pipenv install`

Run the server

`./manage.py runserver`

This code contains sqlite3 database instance, So no need to run migrations.

### API Documentation

#### Create User

URL: http://localhost:8000/user/  
Method: POST  
Body: {  
      "username": "username",  
      "password": "password",  
      "email": "username@example.com",  
      "mobile": 9876543210  
    }  

#### Update User
Note: username shouldn't change.

URL: http://localhost:8000/user/  
Method: PUT  
Body: {  
      "username": "username",  
      "password": "password",  
      "email": "username@example.com",  
      "mobile": 9876543210  
    }  

#### Delete User

URL: http://localhost:8000/user/  
Method: DELETE  
Body: {  
      "username": "username"  
    } 

#### Get user with pagination
Note: pagination is set for 5 records

URL: http://localhost:8000/user/?page=1  
Method: GET  
Response: [  
    {  
        "username": "akshaya4",  
        "password": "admin123",  
        "email": "akshay@example.com",  
        "mobile": 9876543214  
    },  
    {  
        "username": "akshaya5",  
        "password": "admin123",  
        "email": "akshay@example.com",  
        "mobile": 9876543215  
    },  
    {   
        "username": "akshaya6 ,  
        "password": "admin123",  
        "email": "akshay@example.com",  
        "mobile": 9876543216  
    },  
    {  
        "username": "akshaya7",  
        "password": "admin123",  
        "email": "akshay@example.com",  
        "mobile": 9876543217  
    },  
    {  
        "username": "akshaya8",  
        "password": "admin123",  
        "email": "akshay@example.com",  
        "mobile": 9876543218  
    }  
]  
