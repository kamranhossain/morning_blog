# Build GraphQL API with Django
Serving Graphql APIs with Django application


Requirements
------------
1.  Python 3+
2.  Django
3.  graphene_django

Installation on Development Machine
-----------------------------------


To run the app on your local machine, you need Python 3+, installed on your computer. If you using pipenv than follow 2nd 1 to 7 steps

1.  Clone the repo from git and got to repo folder

```shell
git clone https://github.com/kamranhossain/morning_blog.git
cd morning_blog
```

2.  Create and activate virtualenv:

        python3 -m venv venv
        . venv/bin/activate

3.   Read requirments file:
      
        pip install -r requirments.txt


4.  Migrate
        ```shell
        python manage.py migrate
        ```


5.   Load data from fixtures 
        ```shell
        python manage.py loaddata blogs
        ```


6.    Run server 
        ```shell
        python manage.py runserver
        ```
        Go to http://127.0.0.1:8000/ in web browser

7.    Test graphql-queries
        http://127.0.0.1:8000/graphql

