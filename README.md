This is the assignment project for API design in Django and Python
In this project there is design of APIs of a Django application with User(Member) and ActivityPeriod models.

There are two custom commands:
1. populate_members: for populating member_info_tabel in database with dummy data
2. populate_activity_periods: for populating activity_periods_info_table in database with dummy data

APIs design process went through these steps:
1. Creation of models (Member and ActivityPeriod). There is one to many relationship between Member and ActivityPeriod as one member can have many activity periods.
Django ORM is there to communicate between MySQL database and the above mentioned django models.

2. Creation of serializer classes (ActivityPeriodSerializer, MemberSerializer)
This step is crucial as here python native data types along with ORM querysets are being converted into json format which is most popular API format.

3. Creation of Class Based Views (MemberCRUDViewSet and ActivityPeriodCRUDViewSet) based on rest_framework viewsets.

4. Creation of urls

5. Making APIs secure through Jason Web Token (JWT) authentication (This I have kept optional).

6. Testing of urls (using Postman tool and HTTPie to test apis in terminal)

7. Adding source code on GitHub repository

8. Deployment of PythonAnyWhere