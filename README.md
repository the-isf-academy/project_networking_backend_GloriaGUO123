# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
The "Mood of the Day" API is a collaborative platform inspired by Reddit r/place, allowing users to express their daily moods through emojis. Friends can participate together, contributing their own emojis to create a shared canva of collective feelings. Access to the API is completely private, as friends can only join through a unique access code, ensuring that mood sharing remains within trusted circles. By tracking and showcasing moods, this API promotes emotional well-being and enhances communication among users and their friends or family.

### Model
---
#### Emoji Model
***Field:***

|Field   	|Type   	|Description   	|
|---	|---	|---	|
|emoji   	|Str   	|Stores the emoji that user enters   	|
|username   |Str    |Stores the username of the user that enters the emoji
|x_coordinates |Int |Stores the x_coordinates of the emoji on the canva
|y_coordinates |Int |Stores the y_coordinates of the emoji on the canva

Please note that the x and y coordinates of the emoji is automatically allocated, which the user is not allowed to change its position

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|json_response |self    |Return the object in json response format, simular to a dictonary
|setting_position |self |Automatically sets the position (x and y coordinates) of the emoji

#### Canva Model
***Field:***

|Field   	|Type   	|Description   	|
|---	|---	|---	|
|emojis   	|ForeignKey   	|Stores all emojis that user enters into this specific canva   	|
|creator |Str |Stores the creator of the canva
|view   |Int    |Stores the number of views of that specific canva
|like |Int |Stores the number of likes of that specific canva
|popularity_percentage |Float |Stores the percentage of popularity of the canva
|created_time |Str |Stores the created time of the canva
|time_period  |Str |Sorts each edit time of the canva into "morning", "afternoon" and "evening"

|Method   	|Parameter   	|Description   	|
|---	|---	|---	|
|str   	|self   	|Returns the object in a readable and informal, string representation 	|
|json_response |self    |Return the object in json response format, simular to a dictonary
|checking_accesscode |access_code |Checks if the user's input of the access code matches with any id of the canva
|check_time_entry |self |Checks if the last editing time of the user is more than 24 hours
|check_time_period |self |Checks if a specific user has already edit the canva in a time period (E.g. morning, afternoon or evening)
|allocate_time_period|input_time |Based on the editing time, it allocates it into either "morning", "afternoon" and "evening"


Please note that the ID of the canva is refered as access code in the frontend

### Endpoints
---

***`GET` Request:***
#### 1. View previous emojis: 
Returns all the emojis of a specific canva

**GET Request: `/all/emojis`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	        |---	    |---	        |---	|---	|
|access_code   	|Int   	    |To view all the emojis that are inputed in a canva, user needs to input the access code of the desired canva   	

#### 2. View previous canvas: 
Returns all the canva that the user has access with

**GET Request: `/all/canva`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view all the canvas that user has acess with, user need to input all of the acess code.   	|    	|   	|

#### 3. View previous canvas with highest popularity: 
Returns the top 10 canvas with the highest popularity

**GET Request: `/all/canvas/likes`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view the canvas with most popularity, user needs to all the access codes   	|    	|   	|

#### 4. View most recent canvas: 
Returns the top 10 most recent canvas

**GET Request: `/all/canvas/likes`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To view the canvas that are most recent, user needs to all the access codes   	|    	|   	|
---
***`POST` Request:***
#### 1. Add an emoji to the canva: 
Adding a new emoji to the canva, to represent the current mood of a user

**POST Request: `/new`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|To acess a specific canva, user need to first input the access code of that canva   	|    	|   	|
emoji           |Str    |User needs to input the emoji that represents the current mood (E.g. 🥹)
username        |Str    |User also need to input the username in order to record down which emoji belongs to which user

#### 2. Add likes to a specific canva: 
Adding a new emoji to the canva, to represent the current mood of a user

**POST Request: `/likes`**
|Parameter   	|Type   	|Description   	|   	|   	|
|---	|---	|---	|---	|---	|
|access_code   	|Int   	|User needs to enter the access code of the canva that they want to like


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



