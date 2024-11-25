# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey
from datetime import datetime, time, timedelta, timezone
from helper import allocating_time_period

class Canva(Model): 
    like = IntegerField()
    view = IntegerField()
    created_time = StringField()
    popularity_percentage = FloatField()

    def __str__(self):
        return f"id: {self.id}, like:{self.like}, view:{self.view}, created_time:{self.created_time}, popularity_percent: {self.popularity_percentage}"

    def canva_json_response(self):
        return {
            'id': self.id,
            'like': self.like,
            'view': self.view,
            'created_time': self.created_time,
            'popularity_percentage': self.popularity_percentage,
            'access_code': self.id
        }
    
    def increase_like(self):
        #increases the like of the canva
        self.like += 1
        self.save()

    def add_view_and_calculating_popularity(self):
        #Combining add_view with calculating popularity, as they work together 
        self.view +=1
        #calculates the popularity percentage by diving like by view
        popularity = (self.like / self.view) * 100
        self.popularity_percentage = round(popularity, 2)
        self.save()

    def check_twentyfourhour_time_entry(self):
        #convert the current time to HK time
        current_time = datetime.now(timezone.utc) +timedelta(hours=8)
        # Convert create_time into a datetime object
        created_time_datetime_object = datetime.strptime(self.created_time, '%Y-%m-%d %H:%M:%S.%f%z')
        time_difference = current_time - created_time_datetime_object
        # Check if the time difference is less than 24 hours
        return time_difference < timedelta(hours=24)

    def check_time_period_entry(self, input_username):
        #convert the current time to HK time
        current_time = datetime.now(timezone.utc) +timedelta(hours=8)
        current_time = current_time.time()
        #allocates a time period to the current time
        current_time_period = allocating_time_period(current_time)
        # Checks if a specific user has already added an Emoji in the current time period
        for emoji in Emoji.objects.filter(canva=self, username=input_username):
            if emoji.time_period == current_time_period:
                return False
        return True

class Emoji(Model):
    emoji = StringField()
    username = StringField()
    x_coordinates = IntegerField()
    y_coordinates = IntegerField()
    canva = ForeignKey(Canva, related_name='emojis')
    input_time = StringField()
    time_period = StringField()

    def __str__(self):
        return f"canva: {self.canva}, emoji: {self.emoji},username: {self.username},x: {self.x_coordinates}, y: {self.y_coordinates}, time_period: {self.time_period} "

    def emoji_json_response(self):
        return {
            'id': self.id,
            'emoji': self.emoji,
            'username': self.username,
            'x_coordinates': self.x_coordinates,
            'y_coordinates': self.y_coordinates,
            'access_code': self.canva.id,
            'input_time': self.input_time,
            'time_period': self.time_period
            }
    
    def setting_position(self, access_code):
        # The size of the canva is 4x4
            last_emoji = Emoji.objects.filter(canva=access_code).last()
            if last_emoji:
                if last_emoji.x_coordinates <3:
                    # Keeps adding to the value of the x coordinate until reaches 3
                    self.x_coordinates = last_emoji.x_coordinates + 1
                    self.y_coordinates = last_emoji.y_coordinates
                elif last_emoji.x_coordinates >=3:
                    # Moves to the next column (y coordinate), as the x has reaches the maximum of 3
                    self.x_coordinates = 0
                    self.y_coordinates = last_emoji.y_coordinates +1
            else:
                # If no emojis exist, initialize position
                self.x_coordinates = 0
                self.y_coordinates = 0
            if self.y_coordinates >=4:
                return False  # Indicate failure
            # Check if the new position is still within the canvas limits
            return True  # Indicate success
    
    def allocate_time_period(self):
        #extract the time part from the datetime object
        extracted_input_time = self.input_time.time()
        self.time_period = allocating_time_period(extracted_input_time)

    def change(self,input_emoji):
        #convert the current time to HK time
        current_time = datetime.now(timezone.utc)+timedelta(hours=8)
        current_time = current_time.time()
        time_period = allocating_time_period(current_time)
        #checks if the self.time period is same as time_period then it will update the emoji
        if self.time_period == time_period:
            self.emoji = input_emoji
            self.input_time = datetime.now(timezone.utc) +timedelta(hours=8)
            self.save()
            return True
        else:
            return False