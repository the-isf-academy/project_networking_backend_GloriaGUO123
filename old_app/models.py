# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Emoji(Model):
    emoji = StringField()
    username = StringField()
    x_coordinates = IntegerField()
    y_coordinates = IntegerField()
    

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'emoji': self.emoji,
    #         'username': self.username,
    #         'x_coordinates': self.x_coordinates,
    #         'y_coordinates': self.y_coordinates,
    #         }
    
    # def setting_position(self):
    #     last_emoji = Emoji.objects.last()
    #     # The size of the canva is 10x10
    #     if last_emoji.x_coordinates < 10:
    #         # Keeps adding to the value of the x coordinate until reaches 10
    #         self.x_coordinates = last_emoji.x_coordinates + 1
    #         self.y_coordinates = last_emoji.y_coordinates
    #     elif last_emoji.x_coordinates >= 10:
    #         # Moves to the next column (y coordinate), as the x has reaches the maximum of 10
    #         self.x_coordinates = 0
    #         self.y_coordinates = last_emoji.y_coordinates +1
    #     elif last_emoji.y_coordinates >= 10:
    #     # Reaches the maximum size of the canva (10x10)
    #         return False


class Canva(Model): 
    like = IntegerField()
    emojis = ForeignKey(Emoji)
    # view = IntegerField()
    # created_time = StringField()
    # popularity_percentage = FloatField()
    # time_period = StringField()
    # creator = StringField()

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'like': self.like,
    #         'created_time': self.created_time,
    #         'popularity_percentage': self.popularity_percentage
    #     }