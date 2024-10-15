# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Emoji(Model):
    input_emoji = StringField()
    username = StringField()
    # x_coordinates = IntegerField()
    # y_coordinates = IntegerField()
    # access_code = 0

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'input_emoji': self.input_emoji,
    #         'username': self.username,
    #         'x_coordinates': self.x_coordinates,
    #         'y_coordinates': self.y_coordinates,
    #         'access_code': self.access_code
    #         }

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
    #         'popularity_percentage': self
    #     }