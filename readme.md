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

5 get all the events
-------------------
GET /events/

6 get all the genres
--------------------
GET /genres/

7 add a new event
---------------
POST /caregiver/{caregive_id}/events/

with request.body (json-format):

{"event_type": "{event_type_name}"}

8 filter  the events
-------------------
GET /events/

with GET paramerters :

start_date : YYYY-MM-DD
end_date : YYYY-MM-DD
caregivers: {caregiver_name_1},{caregiver_name_2},..


Things left out
-----------------------------

1. Authentication
2. TimeZone handling
3. Validation of the filtering parameters
4. database views for each caregiver and month
5. Database indexes from improving performance
6. Language settings and config



