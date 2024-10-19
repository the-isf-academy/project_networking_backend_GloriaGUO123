# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Canva(Model): 
    like = IntegerField()
    # view = IntegerField()
    # created_time = StringField()
    # popularity_percentage = FloatField()
    # time_period = StringField()
    # creator = StringField()

    def __str__(self):
        return f"id: {self.id}"

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'emojis':self.emojis,
    #         'like': self.like,
    #         'created_time': self.created_time,
    #         'popularity_percentage': self.popularity_percentage
    #     }

    # def checking_accesscode(self, access_code):
    #     if access_code == self.id:
    #         return True
    #     elif access_code != self.id:
    #         return False

class Emoji(Model):
    emoji = StringField()
    # username = StringField()
    # x_coordinates = IntegerField()
    # y_coordinates = IntegerField()
    canva = ForeignKey(Canva, related_name='emojis')

    def __str__(self):
        return f"canva: {self.canva} "

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'emoji': self.emoji,
    #         'username': self.username,
    #         'x_coordinates': self.x_coordinates,
    #         'y_coordinates': self.y_coordinates,
    #         }
    
    #need to check
    # def setting_position(self):
    #     last_emoji = Emoji.objects.last()
    #     # The size of the canva is 10x10
    #     if last_emoji:
    #         if last_emoji.x_coordinates < 10:
    #             # Keeps adding to the value of the x coordinate until reaches 10
    #             self.x_coordinates = last_emoji.x_coordinates + 1
    #             self.y_coordinates = last_emoji.y_coordinates
    #             # return True
    #         elif last_emoji.x_coordinates >= 10:
    #             # Moves to the next column (y coordinate), as the x has reaches the maximum of 10
    #             self.x_coordinates = 0
    #             self.y_coordinates = last_emoji.y_coordinates +1
    #             # return True
    #         elif last_emoji.y_coordinates >= 10:
    #         # Reaches the maximum size of the canva (10x10)
    #             return False
    #     else:
    #         # if the emoji is the first one
    #         self.x_coordinates = 0
    #         self.y_coordinates = 0
    