<p align="center">
  <img src="icon.png"><br/>

  <img src="https://img.shields.io/badge/license-GPL--3-blue?logo=gnu">
  <img src="https://img.shields.io/badge/python-%3E=3.9-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/os-linux-blue?logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/web-Django-green?logo=django&logoColor=white"><br/>
  <img src= "https://img.shields.io/badge/deployment-heroku-purple?logo=heroku&logoColor=white">
  <img src="https://badges.frapsoft.com/os/v3/open-source.svg?v=103"><br/>
</p>

# About Pwitter

Hey folks! Welcome to **"Pwitter"**  a super cool open-source full-stack web app I cooked up using
Django. If you're into social media (who isn't, right?), imagine a Twitter-like playground where you can share your
thoughts, connect with awesome people, and just have a blast. This project is not just about code; it's about showing
off some skills, learning together, and building something that brings people closer.

# Features

- [x] Based on **Django 4**
- [x] **login** / **logout**, **register** and forget password
- [x] custom authentication methods
- [x] User can **create**, **edit** and **delete** own posts
- [x] **Follow** / **Unfollow** other users
- [x] **like** posts
- [x] **comment** and **reply** on posts
- [x] personal **profile** for each user
- [x] **search** mechanism

# Requirements

```markdown
- python version > 3.9
- django version 4
```

# Run Locally

**Step 1 :** create a new virtualenv and install requirements.

```shell
$ pip install -r requirements.txt
```

**Notice :** if you get psycopg2 `pg_config` error use this command

```shell
$ sudo apt-get install libpq-dev
```

**Step 2 :** run django and reach whole project in [http://localhost:8000/](http://localhost:8000/).

```shell
$ python manage.py runserver
```

# Screenshots

### Home Page

![home](screenshot/home.png)

### Post Details

![post](screenshot/post.png)

### Profile

![profile](screenshot/profile.png)

### Login

![login](screenshot/login.png)

### Register

![register](screenshot/register.png)

# License

[GPLV3](https://choosealicense.com/licenses/agpl-3.0/)
