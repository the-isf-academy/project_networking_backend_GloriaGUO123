# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Canva(Model): 
    like = IntegerField()
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

class Emoji(Model):
    input_emoji = StringField()
    # username = StringField()
    # x_coordinates = IntegerField()
    # y_coordinates = IntegerField()
    acess_code = ForeignKey(Canva)

    # def json_response(self):
    #     return {
    #         'id': self.id,
    #         'emoji': self.emoji,
    #         'username': self.username,
    #         'x_coordinates': self.x_coordinates,
    #         'y_coordinates': self.y_coordinates,
    #         'acess_code': self.acess_code
    #     }

