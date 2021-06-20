# Django-pizza
You may download and install the MongoDB database server from the official MongoDB website.

Check the version of MongoDB installed on your machine with the following command:
```
mongo --version
```
To use the mongo shell, start the service with the following command:
```
mongo
```

Create and switch to a new database with the following command:
```
use pizza_database
```

To Run on Localhost:

Have ```Python``` and ```pip``` installed on your local machine

Running the Django project:

Create an isolated environment for the project with virtualenv.
You can install virtualenv with the following command:
```
sudo pip install virtualenv
```

Clone the project from GitHub

Navigate to the cloned project directory:
```
cd django_mongodb_project
```

Create a virtual environment for the project:
```
virtualenv venv
```
Then, activate it:
Ubuntu - ```source venv/bin/activate```
Windows - ```.\venv\Scripts\activate```

```
cd pizza_app
```
Install by:
```
pip install -r requirements.txt
```
Finally, cd into the notes_app folder and run the project:
```
python manage.py runserver
```
Go to http://localhost:8000/ to see if the app is running.

API endpoints :
/admin - Used for admins purpose
/add is used to add new pizz to list. It shows empty page as it redirects it to the index(homepage) to add to the list.
