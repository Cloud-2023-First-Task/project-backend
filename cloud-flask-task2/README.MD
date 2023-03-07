# Simple Flask App


- Instalation of Flask and running a simple app with 2 endpoints (try it on ubuntu):

  ```
  # First we need to make virtual environment
  $ python3 -m venv venv

  # Second we need to activate it
  $ . venv/bin/activate
  $ pip install -r requirements.txt

  # PyLint run:
  $ pylint flasktask2
  
  # App run:
  $ flask --app flasktask2 run
  
  # Check if it's working:
  # Put that in your net browser:
  $ http://127.0.0.1:5000/
  # Then try second endpoint:
  $ http://127.0.0.1:5000/hello
  ```
