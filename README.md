# TODO List project backend

Based on the django-restframework to realize the RESTful-API.

This project is running with link: [http://paladnix.top:8000/task/](http://paladnix.top:8000/task/). You can visite it by the command : 

`curl -X GET -H 'Accept: application/json; indent=2' 'http://paladnix.top:8000/task/'`
to get all task detail in the database.

`curl -X GET -H 'Accept: application/json; indent=2' 'http://paladnix.top:8000/task/{id}/'`
to get exact the {id}'s detail.

`curl -X POST -H 'Content-Type: application/json;' -d '{Data with json format}' 'http://paladnix.top:8000/task/'`
to create a new task in the database.

`curl -X PUT -H 'Content-Type: application/json;' -d '{Data with json format}' 'http://paladnix.top:8000/task/{id}/'`
to update the exact {id}'s task detail. Tips: the `username` and `description` is necessary to put. 

`curl -X DELETE -H 'Content-Type: application/json;' -d '{Data with json format}' 'http://paladnix.top:8000/task/{id}/'`
to delete the {id}'s detail in the database.

# other

Considering that it's the begining that I am learning the django-restframework, I'm unfamiliar with the authentication of each API. So it's public for all to request. 
I will learn more to make it better.

Thanks.

                                    -- Paladnix

