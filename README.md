<h1 align="center"> UTMarketplace </h1>

## Motivation
UTMarketplace is an online marketplace centralizing upon school related supplies (such as textbooks) that caters to students at the University of Toronto. Students may create listings
to sell items, view existing listings, and contact sellers to make an offer.

Unique from existing platforms such as Facebook Marketplace and Kijiji that serve a broad range of clients, UTMarketplace places its focus on student's at UofT, simplifying 
the process of buying and selling educational related items while allowing student's to save money on such items.

UTMarketplace is a web-based application.

## Tools and Dependencies Used
### Frontend
- HTML5
- CSS3
- Javascript

### Backend
- Python 3.8.10
- Django 4.0.1
- SQLite (Alongside Django's ORM)

## Installation
After cloning the repository:

Create and activate the virtual environment: 

* On OS X / Linux:
```bash 
$ python3 -m venv env
$ source env/bin/activate  
``` 

* On Windows:
```
py -m venv env
env\Scripts\activate.bat
```


Install required dependencies:
```
pip install -r requirements.txt
```

Apply Migrations:
* On OS X / Linux
```bash
$ cd src/UTMarketplace
$ python3 manage.py migrate
```
* On Windows:
```
cd src\UTMarketplace
py manage.py migrate
```

Start the application (by default, the server will be listening on port 8000):
* On OS X / Linux
```bash
$ python3 manage.py runserver
```

* On Windows
```
py manage.py runserver
```

Navigate to localhost:8000/login to use the application.
