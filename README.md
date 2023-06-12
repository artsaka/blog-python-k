

# Blog Web App

The Blog web application project is built with Django as the backend and Bootstrap as the frontend.

## Installation Instructions

If you are interested in working on this project or developing your own version of it, carefully follow the instructions outlined below;

1. Make sure to install [` Python 3 `](https://www.python.org/downloads/), [` pip `](https://pip.pypa.io/en/stable/cli/pip_install/) and [` pipenv `](https://docs.python-guide.org/dev/virtualenvs/) or [pipenv-guide](https://realpython.com/pipenv-guide/)
2. Create an application folder
   
    ```bash
        $ mkdir djangoblog
        $ cd djangoblog
    ```
3. Create a virtual environment to isolate the development of the app
    ```bash
        $ pipenv shell        
    ``` 
4. Install the project dependencies from `requirements.txt`
    ```
        $ pipenv install -r requirements.txt
    ```
5. Clone the repository and enter to the development folder
   
    ```bash
        $ git clone https://github.com/artsaka/blog-python-k.git
        $ cd myproject
    ```

## How to run  the project?

Make sure you are in `env` and then do the following each at a time.

```bash
(env)$ python manage.py createsuperuser
(env)$ python manage.py makemigrations
(env)$ python manage.py makemigrations myblogs
(env)$ python manage.py makemigrations users
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

## Features

### Blog list View
List all blog posts with title, tag, number of views, author, date of create the posts, image and clickable to read the whole post.

### Recent Posts
List two posts which are created recently with title at hero panel.

### category list
List all the categories related to the posts with variety of athors.

### Pagination
Display a certain number of posts on each page.

### Blog Detail View
To view the complete blog post when clicked on the Title.

### Login/Register
Users can Login/Register to the Blog App.

### Create Blog Post
Users can create blog posts from the after login to the App.

## Tech Stacks

* **Language:**  Python 3.7
* **Framework:** Django 4.2.1

