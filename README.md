## HomeSlice

A landing page with for your links.

Built with [Django](https://www.djangoproject.com/).

This was a project built to more familiarize myself with Django specifically [Class-based views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/), [testing](https://docs.djangoproject.com/en/3.1/topics/testing/tools/), and custimized user accounts.

### Installation

Clone this repo

```sh
git clone https://github.com/joefearnley/homeslice.git

cd homeslice
```

#### Create and activate virtual environment
```sh
python3 -m venv homeslice-venv
source homeslice-venv/bin/activate
```

#### Install the python requirement
```sh
pip install -r requirements.txt
```

#### Run the database migrations
```sh
python manage.py migrate 
```

#### Create a [Django adming user](https://docs.djangoproject.com/en/5.2/intro/tutorial02/#creating-an-admin-user)
```sh
python manage.py createsuperuser
```

#### Run the Django server
```sh
python manage.py runserver
```

#### Open the app in the browser

http://127.0.0.1:8000


### Deployment


### TODO
