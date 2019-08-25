# health care events project

1 install required libraries
-----------------------------
>pip install -r requirements.txt

2 run the database migrations
----------------------------------

>./manage.py migrate

3 create super user
-------------------
>./manage.py createsuperuser

4 start the server and login
-----------------------------
>./manage.py runserver

* login at:
http://127.0.0.1:8000/admin/

* add some caregivers

* add some events types

* open the schema.yaml file in a swagger editor and make queries to test the application

* run test with :
 
 `./manage.py test `



Things left out
-----------------------------

1. Authentication
2. TimeZone handling
3. Validation of the filtering parameters
4. database views on event per  caregiver and  month
5. Database indexes for  performance improvement
6. Language settings and config
7. patch the date handling in the tests



