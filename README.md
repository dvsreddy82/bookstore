# bookstore
bookstore

python -V //To find the version of Python that you are using

sudo easy_install pip //For installing pip

pip install virtualenvwrapper // Install all the dependencies including virtualenv

source /ur/bin/virtualenvwrapper.sh // On Linux machines

which python // gives you the location

mkvirtualenv bookstore-django // Making a directory

pip install django==1.8 // Downloading and installing Django

cd Development/ django-admin startproject bookstore

./manage.py migrate // Migration

./manage.py runserver // server info

To make migrations for store table

./manage.py makemigrations store

Create super user

./manage.py createsuperuser

To make migrations for store table

./manage.py makemigrations store

Create super user

./manage.py createsuperuser

To get the count of the Model count = Book.objects.all().count()

Django packages

https://djangopackages.org/packages

#####To show migrations

./manage.py showmigrations

