# Resume

## About

The project is set on Docker for development server and set configurations for Heroku for production server.

Django is used for backend, Postgres is used for database. Also Celery can be implemented easily.

Some features:

* Django Management Command


* **Docker** for continuous development server


* **/\<slug>/** : (_views.special_links_) When entered name of images that are added to 'ImageSettings' to url, image returns in max screen size(javascript makes it) to user with layout of page(all meta and head).


* 404, 403, 500 pages are set.


* **ParameterMiddleware:** receive people who come with reference of other users with get parameter of 'ref'
    and saves it into the session. Thus, if user visit other pages of website, all get parameters and 'ref' will stay
    end of the url all the time, on all different links.


* **custom_storage:** There are 3 type of storages in purpose. Uploaded documents, images(from ImageSettings model) and all other media are uploads different locations. 3 type of storage managements are set for development and production separately.


* **template_filters:** has several functions to manage parameters in html templates.

## Installation

To start project,

1. First create a docker.env file from env.txt. Change&enter required parameters.


2. Start postgres at background:

    `docker-compose up -d --build postgres_resume`


3. Start app on terminal and track errors, to make continuous development:

   `docker-compose up --build app_resume`

## Django Management Command

A Django management command is created as colorful with user-friendly progressbar and the functionality is just for example.

To run:

   `docker-compose exec app_resume python manage.py clear_models`

![Django Command Screenshot](https://github.com/berkaymizrak/Resume-Django-Web-App/blob/main/screenshot_command.png?raw=true)


