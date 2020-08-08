# User Activity

## Introduction:-
This app stores the information of user and there work activities. we can store the data using custom management command. One API is provided to                    get all the user data and their respective activities list in the form of JSON.

## Requirements:
  - Python 3.6
  - Django 3.1
  - DRF 3.11.1

## Custom Management Commad:- 
  - command: python manage.py populatedbdata  --path  "path of json file"
  - Json file should be formatted like shown below:
      
      ![json](https://user-images.githubusercontent.com/31935438/89707884-fdcf6680-d98f-11ea-934d-1b1618c3d357.png)
  
  

## Models
  - User -  Defines the details about user like real name and timezone
  - Activity Periods - explains about the each activity of every user. It take two attributes one is "start time" and second is "end time". One more attributes                            exists which define the relation(Many to One) with User model.
  
  
## Hosting:
  - this django app hosted on PythonAnywhere
  - The below API will give the list of user with their all activities
      - http://vidya.pythonanywhere.com/api/useractivity/
  - The output of this API will like this-
    
       - ![apioutput](https://user-images.githubusercontent.com/31935438/89708049-797de300-d991-11ea-9dda-2548ac234479.png)

