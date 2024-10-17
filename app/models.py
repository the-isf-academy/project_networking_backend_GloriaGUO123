# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Emoji(Model):
    emoji = StringField()
    username = StringField()
    x_coordinates = IntegerField()
    y_coordinates = IntegerField()

    # Ask about the difference between _str__ and json_response
    # ask about self.save()
    def __str__(self):
        return f"{self.emoji} created by {self.username}"

    def json_response(self):
        return {
            'id': self.id,
            'emoji': self.emoji,
            'username': self.username,
            'x_coordinates': self.x_coordinates,
            'y_coordinates': self.y_coordinates,
            }
    
    def setting_position(self):
        last_emoji = Emoji.objects.last()
        # The size of the canva is 10x10
        if last_emoji.x_coordinates < 10:
            # Keeps adding to the value of the x coordinate until reaches 10
            self.x_coordinates = last_emoji.x_coordinates + 1
            self.y_coordinates = last_emoji.y_coordinates
            # return True
        elif last_emoji.x_coordinates >= 10:
            # Moves to the next column (y coordinate), as the x has reaches the maximum of 10
            self.x_coordinates = 0
            self.y_coordinates = last_emoji.y_coordinates +1
            # return True
        # Fix Return True Abstraction
        # elif last_emoji.y_coordinates >= 10:
        # # Reaches the maximum size of the canva (10x10)
        #     return False


class Canva(Model): 
    like = IntegerField()
    emojis = ForeignKey(Emoji)
    view = IntegerField()
    created_time = StringField()
    popularity_percentage = FloatField()
    time_period = StringField()
    creator = StringField()

    def __str__(self):
        return f"List of emojis: {self.emojis}"

    def json_response(self):
        return {
            'id': self.id,
            'emojis':self.emojis,
            'like': self.like,
            'created_time': self.created_time,
            'popularity_percentage': self.popularity_percentage
        }

    def checking_accesscode(self, access_code):
        for canva in Canva.objects.all():
            if access_code == canva.id:
                return True
            elif access_code != canva.id:
                return False

    