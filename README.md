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
**Pwitter** is a free and open-source clone of twitter, created by the _Django_.

# Live Demo

You can see the deployed version of project [here](http://pwitter.promethe.dev/) or [here](http://pwitter-promethe.fandogh.cloud/)

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

# Deploy on Fandogh

[fandogh.cloud](https://www.fandogh.cloud/) is a fantastic PaaS that allows you to 
deploy project easily. You just need to make your project dockerized.

To deploy project follow these commands :

**Step 1 :** initiate the image
```shell
$ fandogh image init --name=pwitter
```

**Step 2 :** publish the image to fandogh registry
```shell
$ fandogh image publish --version v0.1 
```

**Step 3 :** deploy the image. Done!
```shell
$ fandogh service deploy --version v0.1 --name pwitter -p 8000 --hosts pwitter.promethe.dev
```

> To use `--host` option you should first verify your domain in fangogh  

# Why ?

I create this project to challenge my backend Skills :)

# License

[GPLV3](https://choosealicense.com/licenses/agpl-3.0/)
