# RestApiHackathon

## Description of Project:
This a Hackathon project. It is API which is used to maintain a record a the events taking place in the campus.
The first two links are part of the API which can be used to maintain the events in JSON format.
The third link uses bing maps API to display all the events in the campus map, on the web browser.

## /event/\<string:event_id\>    
### GET 
request to this will return the event with id event_id
### PUT, DELETE 
used to manipulate the event with id event_id 

## /events   
### GET 
request to this will return all the events
### POST 
request to this will help to add new event

## /event_locations    
Will locate all the events on a map in the browser
