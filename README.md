# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
The "Mood of the Day" API is a collaborative platform inspired by Reddit r/place, allowing users to express their daily moods through emojis. Friends can participate together, contributing their own emojis to create a shared canva of collective feelings. Access to the API is completely private, as friends can only join through a unique access code, ensuring that mood sharing remains within trusted circles. By tracking and showcasing moods, this API promotes emotional well-being and enhances communication among users and their friends or family.

**Simple Instruction:**
1. User will need to create a canva first (at least one, multiple canvas are also allowed)
2. User can add emojis to a specific canva, and collaborate with friends, family to form a art piece
3. User can view all the emojis added to a canva or all the canvas that the user has created, but access code will be needed to ensure privacy

**Important Notice**
- For each canva, each user can only add in ONE new emoji during Morning (4:00 AM to 11:59 AM), Afternoon (12:00 PM to 5:59 PM), and Evening (6:00 PM to 3:59 AM)
- Please note that the maximum canva size is 4x4 (meaning that ONLY 16 emojis are allowed for each canva)
- The editing access of the canva will be locked after 24 hours of the `created_time` 
- Please remember the access code for each canva or else the user can not access the canva anymore

### Model
---
#### Emoji Model
***Field:***

|Field   	|Type   	|Description   	|Example|
|---	|---	|---	|---	|
|emoji   	|Str   	|Stores the emoji that user enters   	|😀
|username   |Str    |Stores the username of the user that enters the emoji|Gloria
|x_coordinates |Int |Stores the x_coordinates of the emoji on the canva|1
|y_coordinates |Int |Stores the y_coordinates of the emoji on the canva|2
|canva      |ForeignKey |Stores the canva object that belongs to this emoji object, which two databases are linked together|To access the id of the canva, simply type emoji.canva.id

Please note that the x and y coordinates of the emoji is automatically allocated, which the user is not allowed to change its position

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|emoji_json_response |self    |Return the object in json response format, simular to a dictonary
|setting_position |self, access_code |Automatically sets the position (x and y coordinates) of the emoji based on the position of the last emoji inputed of the specific canva

#### Canva Model
***Field:***

|Field   	|Type   	|Description   	|Example
|---	|---	|---	|---	|
|view   |Int    |Stores the number of views of that specific canva|0
|like |Int |Stores the number of likes of that specific canva|0
|popularity_percentage |Float |Stores the percentage of popularity of the canva|50.0
|created_time |Str |Stores the created time of the canva|2024-10-20 04:21:55.161606
|time_period  |Str |Sorts each edit time of the canva into "Morning", "Afternoon" and "Evening"|

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|canva_json_response |self    |Return the object in json response format, simular to a dictonary
|check_twentyfourhour_time_entry |self |Checks if the last editing time of the user is more than 24 hours
|check_time_period_entry |self |Checks if a specific user has already edit the canva in a time period (E.g. Morning, Afternoon or Evening)
|allocate_time_period|self |Based on the last editing time, it allocates it into either "Morning", "Afternoon" and "Evening"
|increase_like |self    |Increases number of `like` of the specific canva
|add_view_and_calculating_popularity |self |Increases number of `view` of the specific canva and calculates the `popularity_percentage` by simply dividing `like` by `view`

Please note that the ID of the canva is refered as access code in the frontend

### Endpoints
---

***`GET` Request:***
#### 1. View previous emojis: 
Returns all the emojis of a specific canva

**GET Request: `/all/emojis`**
|Payload  	|Type   	|Description   	|   	|   	|
|---	        |---	    |---	        |---	|---	|
|access_code   	|Int   	    |To view all the emojis that are inputed in a specific canva, user needs to input the access code of the desired canva   	

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/emoji 
Payload: access_code=1

{
  "Emojis": [
    {
      "id": 1,
      "emoji": "🙃",
      "username": "Gloria",
      "x_coordinates": 0,
      "y_coordinates": 0,
      "access_code": 1
    },
    {
      "id": 2,
      "emoji": "😌",
      "username": "Adrianne",
      "x_coordinates": 1,
      "y_coordinates": 0,
      "access_code": 1
    },
    {
      "id": 3,
      "emoji": "😚",
      "username": "Amanda",
      "x_coordinates": 2,
      "y_coordinates": 0,
      "access_code": 1
    },
  ]
}
```

#### 2. View previous canvas: 
Returns all the canva that the user has access with

**GET Request: `/all/canva`**
|Payload   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view all the canvas that user has acess with, user need to input all of the acess code.   	|    	|   	|

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/canva 
Payload: access_code=1,2,3

{
  "Canvas": [
    {
      "id": 1,
      "like": 0,
      "view": 2,
      "created_time": "2024-10-21 04:30:24.806533",
      "popularity_percentage": 0,
      "access_code": 1
    },
    {
      "id": 2,
      "like": 0,
      "view": 2,
      "created_time": "2024-10-21 04:30:27.804994",
      "popularity_percentage": 0,
      "access_code": 2
    },
    {
      "id": 3,
      "like": 0,
      "view": 2,
      "created_time": "2024-10-21 04:30:29.510287",
      "popularity_percentage": 0,
      "access_code": 3
    }
  ]
}

```

#### 3. View previous canvas with highest popularity: 
Returns the top 5 canvas with the highest popularity

**GET Request: `/all/canva/popularity`**
|Payload   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view the canvas with highest popularity percentage (top 5 only), user needs to all the access codes   	|    	|   	|

*Example:* 
```
Get Request: http://127.0.0.1:5000/moodboard/all/canva 
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

#### 4. View most recent canvas: 
Returns the top 5 most recent canvas

**GET Request: `/all/canvas/recent`**
|Payload  	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view the canvas that are most recent (top 5), user needs to all the access codes   	|    	|   	|
---
***`POST` Request:***
#### 1. Create a canva: 
User can create mutiple canva with different group of people, for example friends and family 

**POST Request: `/new/canva`**
|Payload   	|Type   	|Description   	|   	|   	|
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
    "created_time": "2024-10-21T04:30:29.510",
    "popularity_percentage": 0,
    "access_code": 3
  }
}
```

#### 2. Add an emoji to the canva: 
Adding a new emoji to the canva, to represent the current mood of a user

**POST Request: `/new/emoji`**
|Payload   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To acess a specific canva, user need to first input the access code of that canva   	|    	|   	|
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

#### 3. Add likes to a specific canva: 
Through this endpoint, user can add likes to a specific canva

**POST Request: `/likes`**
|Payload   	|Type   	|Description   	|   	|   	|
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



