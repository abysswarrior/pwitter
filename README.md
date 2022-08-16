<p align="center">
  <img src="icon.png"><br/>

  <img src="https://img.shields.io/badge/license-GPL--3-blue?logo=gnu">
  <img src="https://img.shields.io/badge/python-%3E=3.8-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/os-linux-blue?logo=linux&logoColor=white">
  <img src= "https://img.shields.io/badge/crawler-selenium-blue?logo=selenium&logoColor=white"><br/>
  <img src= "https://img.shields.io/badge/document-swagger-green?logo=swagger&logoColor=white">
  <img src="https://img.shields.io/badge/web-Django-green?logo=django&logoColor=white"><br/>
  <img src= "https://img.shields.io/badge/deployment-heroku-purple?logo=heroku&logoColor=white"><br/>
</p>

# About Pwitter
**Pwitter** is a free and open-source clone of twitter, created by the _Django_.

# Live Demo

You can see the deployed version of project [here](https://pwitter.herokuapp.com/)

# Requirements

```markdown
- python version 3.9 or upper
- django version 4 or upper
```

# Run Locally

now follow these steps :

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

## License

[GPLV3](https://choosealicense.com/licenses/agpl-3.0/)