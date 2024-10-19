# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField, ForeignKey

class Canva(Model): 
    like = IntegerField()
    view = IntegerField()
    created_time = StringField()
    popularity_percentage = FloatField()
    time_period = StringField()

    def __str__(self):
        return f"id: {self.id}"

    def canva_json_response(self):
        return {
            'id': self.id,
            # 'emojis':self.emojis,
            'like': self.like,
            'created_time': self.created_time,
            'popularity_percentage': self.popularity_percentage,
            'access_code': self.id
        }

class Emoji(Model):
    emoji = StringField()
    username = StringField()
    x_coordinates = IntegerField()
    y_coordinates = IntegerField()
    canva = ForeignKey(Canva, related_name='emojis')

    def __str__(self):
        return f"canva: {self.canva}, emoji: {self.emoji},username: {self.username},x: {self.x_coordinates}, y: {self.y_coordinates} "

    def emoji_json_response(self):
        return {
            'id': self.id,
            'emoji': self.emoji,
            'username': self.username,
            'x_coordinates': self.x_coordinates,
            'y_coordinates': self.y_coordinates,
            'access_code': self.canva.id
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
    