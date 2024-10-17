# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Emoji

@route_get(BASE_URL + 'all')
def all_emojis(args):
    emojis_list = []
    for emoji in Emoji.objects.all():
        emojis_list.append(emoji.json_response())
    if emojis_list != []:
        return {'Emojis': emojis_list}
    elif emojis_list == []:
        return {'Error': 'No emojis exist currently'}

@route_post(BASE_URL + 'new', args={'emoji':str, 'username': str})
def new_emoji(args):
    new_emoji = Emoji(
        emoji = args['emoji'],
        username = args['username'],
        )
    new_emoji.setting_position()
    new_emoji.save()
    if new_emoji.setting_position() == True:
        return {'Emoji': new_emoji.json_response()}
    
    elif new_emoji.setting_position == False:
        return {'Error': 'The canva size has reached to its maximum'}

