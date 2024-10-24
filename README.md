# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
The "Mood of the Day" API is a collaborative platform inspired by Reddit r/place, allowing users to express their daily moods through emojis. Friends can participate together, contributing their own emojis to create a shared canva of collective feelings. Access to the API is completely private, as friends can only join through a unique access code, ensuring that mood sharing remains within trusted circles. By tracking and showcasing moods through visualisation, this API promotes emotional well-being and enhances communication among users and their friends or family.

**Simple Instruction:**
1. User MUST create a canva first (at least one, multiple canvas are also allowed) before starting to add emojis
2. User can add emojis to a specific canva, and collaborate with friends, family to form an art piece
3. If users accidentally create an unwanted canva or emoji, they can also delete it. 
3. User can view all the emojis added to a canva or all the canvas that the user has created, but access code will be needed to ensure privacy

**Important Notice**
- For each canva, each user can only add in ONE new emoji during Morning (4:00 AM to 11:59 AM), Afternoon (12:00 PM to 5:59 PM), and Evening (6:00 PM to 3:59 AM)
- Please note that the maximum canva size is 4x4 (meaning that ONLY 16 emojis are allowed for each canva)
- The editing access of the canva will be locked after 24 hours of the `created_time`, as each canva should represent the mood of the day. 
- Please remember the access code for each canva or else the user can not access the canva anymore

### Model
---
#### Emoji Model
***Field:***

|Field   	|Data Type   	|Description   	|Example|
|---	|---	|---	|---	|
|emoji   	|Str   	|Stores the emoji that user enters   	|😀
|username   |Str    |Stores the username of the user that enters the emoji|Gloria
|x_coordinates |Int |Stores the x_coordinates of the emoji on the canva|1
|y_coordinates |Int |Stores the y_coordinates of the emoji on the canva|2
|canva      |ForeignKey |Stores the canva object that belongs to this emoji object, which two databases are linked together|<Canva: id: 2, like:2, view:32, created_time:2024-10-22 19:52:12.198770, popularity_percent: 6.25>
|input_time |Str |Stores the time that the user added the emoji to the database| 2024-10-20 04:21:55.161606
|time_period |Str |Based on the `input_time`, allocates it into "Morning", "Afternoon", "Evening"|Morning

Please note that the x and y coordinates of the emoji is automatically allocated, which the user is not allowed to change its position

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|emoji_json_response |self    |Return the object in json response format, simular to a dictonary
|setting_position |self, access_code |Automatically sets the position (x and y coordinates) of the emoji based on the position of the last emoji inputed of the specific canva
|allocate_time_period |self |Based on the `input_time`, allocates the time period into "Morning", "Afternoon", "Evening"
|change |self, input_emoji |Allows the user to change their input for the emoji during the same time period ONLY

#### Canva Model
***Field:***

|Field   	|Data Type   	|Description   	|Example
|---	|---	|---	|---	|
|view   |Int    |Stores the number of views of that specific canva|0
|like |Int |Stores the number of likes of that specific canva|0
|popularity_percentage |Float |Stores the percentage of popularity of the canva|50.0
|created_time |Str |Stores the created time of the canva|2024-10-20 04:21:55.161606

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|canva_json_response |self    |Return the object in json response format, simular to a dictonary
|check_twentyfourhour_time_entry |self |Checks if the `created_time` is more than 24 hours compared with the current time
|check_time_period_entry |self, input_username|Checks if a specific user has already edit the canva in a time period (E.g. Morning, Afternoon or Evening)
|increase_like |self    |Increases number of `like` of the specific canva
|add_view_and_calculating_popularity |self |Increases number of `view` of the specific canva and calculates the `popularity_percentage` by simply dividing `like` by `view`

Please note that the ID of the canva is refered as access code of the canva in the frontend

### Endpoints
---

***Access Code Format Guide***

For endpoints that ALLOWS multiple access code to be inputed, please do remember that the format to input the access code is crutial, or else it would cause an error. Essentially, user must place `,` (commas) between each access code, or else it will not recognise it as individual integers, causing error to happen. 

*Examples*
```
✅:
access_code = 1,2,5,6
access_code = 1
access_code = 9,1
access_code = 1    ,      2   , 3

❌:
access_code = 1`2`2
access_code = 1\2\3
access_code = 1 2 3
```

***`GET` Request:***
#### 1. View previous emojis: 
Returns all the emojis of a specific canva

**GET Request: `/all/emojis`**
|Payload  	|Data Type   	|Description   	|   	|   	|
|---	        |---	    |---	        |---	|---	|
|access_code   	|Int   	    |To view all the emojis that are inputed in a specific canva, user needs to input the access code of the desired canva   	

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/emoji 
Payload: access_code=2

{
  "Emojis": [
    {
      "id": 3,
      "emoji": "🙃",
      "username": "Gloria",
      "x_coordinates": 0,
      "y_coordinates": 0,
      "access_code": 2,
      "input_time": "2024-10-22 23:19:58.354520",
      "time_period": "Evening"
    },
    {
      "id": 4,
      "emoji": "🥺",
      "username": "Amanda",
      "x_coordinates": 1,
      "y_coordinates": 0,
      "access_code": 2,
      "input_time": "2024-10-22 23:20:02.826174",
      "time_period": "Evening"
    },
    {
      "id": 5,
      "emoji": "😳",
      "username": "Joyce",
      "x_coordinates": 2,
      "y_coordinates": 0,
      "access_code": 2,
      "input_time": "2024-10-22 23:20:08.282238",
      "time_period": "Evening"
    }
  ]
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|No emojis exist in the canva currently   	|Unable to return the emojis because there isn't any emojis stored in the canva. To solve this, add emojis to the canva that user wants to view   	|   	|
|Access code does not exist   	|The access code is not found, check if the access code is typed correctly    	|   	|

#### 2. View previous canvas: 
Returns all the canva that the user has access with

**GET Request: `/all/canva`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Str   	|To view all the canvas that user has access with, user need to input all of the access code.   	|    	|   	|

*Please note that the format of inputing the access code is crutial, else it would cause an error (May refer back to **Access Code Format Guide** on top). 


Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/canva 
Payload: access_code=2,3,4

{
  "Canvas": [
    {
      "id": 2,
      "like": 0,
      "view": 19,
      "created_time": "2024-10-22 19:52:12.198770",
      "popularity_percentage": 0,
      "access_code": 2
    },
    {
      "id": 3,
      "like": 0,
      "view": 18,
      "created_time": "2024-10-22 19:52:12.759492",
      "popularity_percentage": 0,
      "access_code": 3
    },
    {
      "id": 4,
      "like": 0,
      "view": 15,
      "created_time": "2024-10-22 19:52:13.316877",
      "popularity_percentage": 0,
      "access_code": 4
    }
  ]
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|None of the canvas exist   	|All the access codes that the user has inputed are not found, user should check all the access code and ensure that they are correct   	|   	|

#### 3. View previous canvas with highest popularity: 
Returns the top 5 canvas with the highest popularity

**GET Request: `/all/canva/popularity`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Str  	|To view the canvas with highest popularity percentage (top 5 only), user needs to all the access codes   	|    	|   	|

*Please note that the format of inputing the access code is crutial, else it would cause an error (May refer back to **Access Code Format Guide** on top). 

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/canva/popularity 
Payload: access_code=1,2,3

{
  "Canvas": [
    {
      "id": 1,
      "like": 2,
      "view": 5,
      "created_time": "2024-10-21 04:30:24.806533",
      "popularity_percentage": 40,
      "access_code": 1
    },
    {
      "id": 2,
      "like": 1,
      "view": 4,
      "created_time": "2024-10-21 04:30:27.804994",
      "popularity_percentage": 25,
      "access_code": 2
    },
    {
      "id": 3,
      "like": 0,
      "view": 3,
      "created_time": "2024-10-21 04:30:29.510287",
      "popularity_percentage": 0,
      "access_code": 3
    }
  ]
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|No canvas exist currently or access code not found   	|The access codes that the user has inputed are not found or typed incorrecly. To solve that, user should check all the access codes that user has inputed   	|   	|

#### 4. View most recent canvas: 
Returns the top 5 most recent canvas

**GET Request: `/all/canvas/recent`**
|Payload  	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Str   	|To view the canvas that are most recent (top 5), user needs to all the access codes   	|    	|   	|

*Please note that the format of inputing the access code is crutial, else it would cause an error (May refer back to **Access Code Format Guide** on top). 

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/canva/recent 
Payload: access_code=1,2,4

{
  "Canvas": [
    {
      "id": 4,
      "like": 0,
      "view": 4,
      "created_time": "2024-10-23 21:57:54.655358+00:00",
      "popularity_percentage": 0,
      "access_code": 4
    },
    {
      "id": 3,
      "like": 0,
      "view": 4,
      "created_time": "2024-10-23 21:57:53.866276+00:00",
      "popularity_percentage": 0,
      "access_code": 3
    },
    {
      "id": 1,
      "like": 0,
      "view": 5,
      "created_time": "2024-10-23 21:57:52.573614+00:00",
      "popularity_percentage": 0,
      "access_code": 1
    }
  ]
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|No canvas exist currently or access code not found   	|The access codes that the user has inputed are not found or typed incorrecly. To solve that, user should check all the access codes that user has inputed   	|   	|
---
***`POST` Request:***
#### 1. Create a canva: 
User can create mutiple canva with different group of people, for example friends and family 

**POST Request: `/new/canva`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|None   |None   |None
*No parameter needed for this endpoint

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/new/canva
Payload: None

{
  "Canva": {
    "id": 3,
    "like": 0,
    "view": 1,
    "created_time": "2024-10-21T14:30:29.510",
    "popularity_percentage": 0,
    "access_code": 3
  }
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|None |None|   	|

#### 2. Add an emoji to the canva: 
Adding a new emoji to the canva, to represent the current mood of a user

**POST Request: `/new/emoji`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To access a specific canva, user need to first input the access code of that canva   	|    	|   	|
emoji           |Str    |User needs to input the emoji that represents the current mood (E.g. 🥹)
username        |Str    |User also need to input the username in order to record down which emoji belongs to which user

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/new/emoji
Payload: access_code=1, emoji=😇, username=Gloria

{
  "Emoji": {
    "id": 1,
    "emoji": "😇",
    "username": "Gloria",
    "x_coordinates": 0,
    "y_coordinates": 0,
    "access_code": 1
  }
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|After 24 hours, the canva will be saved and no longer editable|The canva that the user wants to edit is more than 24 hours, thus the user can not edit the canva anymore. User can make a new canva in order to add emojis   	|
|The user has already input an emoji during this time period, please wait for the next time period|Users are not allowed to input an emoji during the same period, if it is different users and returns this error, it is indicating that the username of the two users are the same, thus one of the user should use a different username to avoid this error. 
|The canva size has reached to its maximum|Each canva can only have 16 emojis added, to add more emojis, user can create another canva
|Access code does not exist|The access code is not found, user might enter the wrong access code, double-check if the access code is inputed correctly. 

#### 3. Add likes to a specific canva: 
Through this endpoint, user can add likes to a specific canva

**POST Request: `/likes`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|User needs to enter the access code of the canva that they want to like

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/likes
Payload: access_code=1

{
  "Canva": {
    "id": 1,
    "like": 3,
    "view": 6,
    "created_time": "2024-10-21 04:30:24.806533",
    "popularity_percentage": 50,
    "access_code": 1
  }
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|Access code does not exist|The access code is not found, user might enter the wrong access code, double-check if the access code is inputed correctly. 

#### 4. Updating an emoji during same time period: 
User can update the emoji based on their current mood, as long as it is still within the same time period

**POST Request: `update/emoji`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|User needs to enter the access code of the canva that they want to access
|id |Int |Users need to enter the id of the emoji that they would like to change
|change_emoji|Str|Input the emoji that user would like to replace into

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/update/emoji
Payload: access_code=3, change_emoji=🙃, id=15

{
  "Emoji": {
    "id": 16,
    "emoji": "🙃",
    "username": "cc",
    "x_coordinates": 3,
    "y_coordinates": 3,
    "access_code": 1,
    "input_time": "2024-10-23T22:17:52.092Z",
    "time_period": "Evening"
  }
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|Access code does not exist|The access code is not found, user might enter the wrong access code, double-check if the access code is inputed correctly. 
|Failed to change emoji, can only change in same time period|Users can only update the emoji that is in the same time period, if it is during different time period, user should use the `new/emoji` endpoint.
|Emoji not found|The emoji is not found, meaning that the id of a certain emoji doesn't exist, user should check if the id of the emoji is inputed correctly.

#### 5. Delete a canva:
Users can delete a canva that is undesired

**POST Request: `delete/canva`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|User needs to enter the access code of the canva that they want to delete

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/delete/canva
Payload: access_code=3

{
  "Sucess": "User has already deleted the canva"
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|Unsucessful, No canva exist|The access code is not found, thus it is impossible to delete the canva, user might enter the wrong access code, double-check if the access code is inputed correctly. 

#### 6. Delete an emoji:
Users can delete an emoji that is undesired in a specific canva

**POST Request: `delete/emoji`**
|Payload   	|Data Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|User needs to enter the access code of the canva that the emoji is belonged to
|id |Int |Input the ID of the emoji that needs to be deleted

*Example:* 
```
Post Request: http://127.0.0.1:5000/moodboard/delete/emoji
Payload: access_code=3, id=15

{
  "Success": "Emoji has been deleted"
}
```
#### Error Messages ####
|Error Message   	|Meaning and Method to Solve   	|   	|
|---	|---	|---	|
|Access code does not exist|The access code is not found, thus it is impossible to find the emoji that is in the canva, user might enter the wrong access code, double-check if the access code is inputed correctly. 
|Emoji not found or does not belong to this canvas|The id of the emoji is not found or the emoji does not belong to the canva, user should check if the id of the emoji is inputed correctly.

## Setup
1. Open Terminal
2. Enter `poetry shell`
3. Enter `banjo --debug`
    - Should return `Starting development server at http://127.0.0.1:5000/`
    - If user wants to quit the server, press `CONTROL-C`
4. Open HTTPie
5. Type in `http://127.0.0.1:5000/moodboard/` as Base URl, and add the endpoint based on user's perference
    - Please look through the detailed instruction on top, with the guide to use each endpoint

### Contents
---

Here's what is included:
- `\app`
    - `models.py` - `Canva` model and `Emoji` model 
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



