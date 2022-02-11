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
- Bootstrap v5.1.3
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
$ cd src
$ python3 manage.py makemigrations
$ python3 manage.py migrate --run-syncdb
```
* On Windows:
```
cd UTMarketplace
> py manage.py makemigrations
> py manage.py migrate --run-syncdb
```

Start the application (by default, the server will be listening on port 8000):
* On OS X / Linux
```bash
$ python3 manage.py runserver
```

* On Windows
```
> py manage.py runserver
```

Navigate to localhost:8000/login to use the application.
After usage:
To stop the server, press CTRL + C. Type ```deactivate``` to shutdown the virtual environment.

## Contribution
This repository is devised of two central branches:
1. ```main```
This branch is composed of fully developed features that have been tested and integrated with existing features. After a set of features in the ```DEV``` branch has been fully tested, it may be merged into the ```main``` branch at the end of a sprint, to have a working product. Prior to merging into main, all commits must be subject to a Pull Request that must be reviewed by at least 2 other developers.

2. ```DEV```
This branch is used to store features that have been developed, but not yet tested or fully integrated in. All merges from feature branches are subject to Pull Requests that must be reviewed by at least 2 other developers.

# Feature Development
Features are developed in the following manner:
* Create a branch off ```DEV``` with the naming convention: FEATURE/feature_name
* During feature development, commits must be frequent and should not be large in size. Commit messages must be detailed.

