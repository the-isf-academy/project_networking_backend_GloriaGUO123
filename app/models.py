# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey
from datetime import datetime, time

class Canva(Model): 
    like = IntegerField()
    view = IntegerField()
    created_time = StringField()
    popularity_percentage = FloatField()

    def __str__(self):
        return f"id: {self.id}, like:{self.like}, view:{self.view}, created_time:{self.created_time}"

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
        self.like += 1
        self.save()

    def add_view_and_calculating_popularity(self):
        #Combining add_view with calculating popularity, as they work together 
        self.view +=1
        popularity = (self.like / self.view) * 100
        self.popularity_percentage = round(popularity, 2)
        self.save()

    # def check_twentyfourhour_time_entry(self):

    # def check_time_period_entry(self):

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
        # Ask about this line of code
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
        #converting string object into datetime format
        # datetime_object = datetime.strptime(self.input_time, '%Y-%m-%d %H:%M:%S.%f')
        #extract the time part from the datetime object
        extracted_input_time = self.input_time.time()
        #Morning: 4:00 AM to 11:59 AM
        if time(4, 0) <= extracted_input_time < time(12, 0):
            self.time_period = "morning"
        #Afternoon: 12:00 PM to 5:59 PM
        elif time(12, 0) <= extracted_input_time < time(18, 0):
            self.time_period = "afternoon"
        #Evening: 6:00 PM to 3:59 AM
        else:
            self.time_period = "evening"
        self.save()
    