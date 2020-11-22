<h1>Welcome to news-site project</h1>

This is my web pet project should follow next requirements: 

Create basic news site, which should have post premoderation before post publication. Administrator can approve post or decline post. Approve post is published.

By default there are three groups:

    - Admin (They can make post without premoderation)
    - Editors (without premoderation)
    - Users (with premoderation)


<h1>How to run it</h1>

1. Clone this repository.
2. install all requirements with command `pip install -r requirements.txt`
3. run command `python manage.py populate` to prepopulate data
4. run `python manage.py runserver` to start application

<h2>via Docker</h2>

`docker-compose up -d` to start an application

`docker-compose down` to stop an application