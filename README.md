# Todowo
An application to manage dailty tasks

to run it locally install python form https://python.org (make sure to add it to PATH)
after installing python create virtual enviironment using 
```python -m venv environment_name```

after creating your virtual environment we will install DJANGO but first we need to activate you virtual environment
in the command line run
```cd environment_name\Scripts``` <br>
```activate```

now the environment will be activated and we can install django
```pip install Django==3.0.8```
after it is installed open cmd inside project folder
```python manage.py createsuperuser``` (enter the details that it will ask)<br>
```python manage.py makemigration``` <br>
```python manage.py migrate```<br>
```python manage.py runserver```
now you can open your browser and run "127.0.0.1:8000" or "localhost:8000"
