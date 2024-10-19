# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Emoji, Canva
from time import time

@route_get(BASE_URL + 'all/emoji', args = {'access_code':int})
def all_emoji(args):
    if Canva.objects.filter(id=args['access_code']).exists() == True:
        emojis_list = []
        user_canva = Canva.objects.get(id=args['access_code'])
        for emoji in user_canva.emojis.all():
            emojis_list.append(emoji.emoji_json_response())
        if emojis_list != []:
            return {'Emojis': emojis_list}
        elif emojis_list == []:
            return {'Error': 'No emojis exist in the canva currently'}
    elif Canva.objects.filter(id=args['access_code']).exists() == False:
        return {'Error': 'Access code does not exit'}

# # Try to see how to accept multiple values in one parameter
# @route_get(BASE_URL + 'all/canva', args = {'access_code':int})
# def all_canvas(args):
#     canvas_list = []
#     for canva in Canva.objects.filter(id=args['access_code']):
#         canva.calculating_popularity()
#         canvas_list.append(canva.canva_json_response())
#     if canvas_list != []:
#         return {'Canvas': canvas_list}
#     elif canvas_list == []:
#         return {'Error': 'No canvas exist currently'}

@route_get(BASE_URL + 'all/canva')
def all_canvas(args):
    canvas_list = []
    for canva in Canva.objects.all():
        canva.calculating_popularity()
        canvas_list.append(canva.canva_json_response())
    if canvas_list != []:
        return {'Canvas': canvas_list}
    elif canvas_list == []:
        return {'Error': 'No canvas exist currently'}

@route_get(BASE_URL + 'all/canva/popularity')
def all_canvas_most_popularity(args):
    canvas_list = []
    for canva in Canva.objects.order_by('-popularity_percentage')[:5]:
        canva.calculating_popularity()
        canvas_list.append(canva.canva_json_response())
    if canvas_list != []:
        return {'Canvas': canvas_list}
    elif canvas_list == []:
        return {'Error': 'No canvas exist currently'}

@route_post(BASE_URL + 'new/emoji', args={'emoji':str, 'username': str, 'access_code':int})
def new_emoji(args):
    #Ask how to fix the error, when the canva does not exit
    if Canva.objects.filter(id=args['access_code']).exists() == True:
        selected_canva = Canva.objects.get(id=args['access_code'])
        new_emoji = Emoji(
            emoji = args['emoji'],
            username = args['username'],
            canva = selected_canva
            )
        new_emoji.setting_position(args['access_code'])
        if new_emoji.setting_position(args['access_code']) == True:
            new_emoji.save()
            return {'Emoji': new_emoji.emoji_json_response()}
        elif new_emoji.setting_position(args['access_code']) == False:
            return {'Error': 'The canva size has reached to its maximum'}
    elif Canva.objects.filter(id=args['access_code']).exists() == False:
        return {'Error': 'Access code does not exit'}

@route_post(BASE_URL + 'new/canva', args = {'current_time': str})
def new_canva(args):
    new_canva = Canva(
        like = 0,
        view = 0,
        created_time = args['current_time'],
        popularity_percentage = 0,
        time_period = ''
    )
    new_canva.calculating_popularity()
    new_canva.save()
    return {'Canva': new_canva.canva_json_response()}

@route_post(BASE_URL + 'likes', args = {'access_code':int})
def like_canva(args):
    if Canva.objects.filter(id=args['access_code']).exists():
        chosen_canva = Canva.objects.get(id=args['access_code'])
        # Why can't I chain them together
        chosen_canva.increase_like()
        chosen_canva.calculating_popularity()
        return {'Canva':chosen_canva.canva_json_response()}
    else: 
        return {'Error': "No canva exist"}
