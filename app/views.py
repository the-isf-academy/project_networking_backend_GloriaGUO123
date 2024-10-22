# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Emoji, Canva
from datetime import datetime

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
#         canva.add_view_and_calculating_popularity()
#         canvas_list.append(canva.canva_json_response())
#     if canvas_list != []:
#         return {'Canvas': canvas_list}
#     elif canvas_list == []:
#         return {'Error': 'No canvas exist currently'}

@route_get(BASE_URL + 'all/canva')
def all_canvas(args):
    canvas_list = []
    for canva in Canva.objects.all():
        canva.add_view_and_calculating_popularity()
        canvas_list.append(canva.canva_json_response())
    if canvas_list != []:
        return {'Canvas': canvas_list}
    elif canvas_list == []:
        return {'Error': 'No canvas exist currently'}

@route_get(BASE_URL + 'all/canva/popularity')
def all_canvas_most_popularity(args):
    canvas_list = []
    # Only returns the top 5 most popular canva based on the percentage of popularity
    for canva in Canva.objects.order_by('-popularity_percentage')[:5]:
        canva.add_view_and_calculating_popularity()
        canvas_list.append(canva.canva_json_response())
    if canvas_list != []:
        return {'Canvas': canvas_list}
    elif canvas_list == []:
        return {'Error': 'No canvas exist currently'}

@route_get(BASE_URL + 'all/canva/recent')
def all_canvas_most_recent(args):
    canvas_list = []
    # Only returns the top 5 most popular canva based on the created time
    for canva in Canva.objects.order_by('-created_time')[:5]:
        canva.add_view_and_calculating_popularity()
        canvas_list.append(canva.canva_json_response())
    if canvas_list != []:
        return {'Canvas': canvas_list}
    elif canvas_list == []:
        return {'Error': 'No canvas exist currently'}

@route_post(BASE_URL + 'new/emoji', args={'emoji':str, 'username': str, 'access_code':int})
def new_emoji(args):
    if Canva.objects.filter(id=args['access_code']).exists() == True:
        selected_canva = Canva.objects.get(id=args['access_code'])
        new_emoji = Emoji(
            emoji = args['emoji'],
            username = args['username'],
            canva = selected_canva,
            #Note: Make it so that it maches with HK
            input_time = datetime.now()
            )
        new_emoji.allocate_time_period()
        new_emoji.setting_position(args['access_code'])
        if new_emoji.setting_position(args['access_code']) == True and selected_canva.check_twentyfourhour_time_entry() ==True and selected_canva.check_time_period_entry(args['username']) ==True:
            new_emoji.save()
            return {'Emoji': new_emoji.emoji_json_response()}
        elif selected_canva.check_twentyfourhour_time_entry() == False:
            return {'Error': 'After 24 hours, the canva will be saved and no longer editable'}
        elif selected_canva.check_time_period_entry(args['username']) == False:
            return {'Error': 'The user has already input an emoji during this time period, please wait for the next time period'}
        elif new_emoji.setting_position(args['access_code']) == False:
            return {'Error': 'The canva size has reached to its maximum'}
    elif Canva.objects.filter(id=args['access_code']).exists() == False:
        return {'Error': 'Access code does not exit'}
        
@route_post(BASE_URL + 'new/canva')
def new_canva(args):
    new_canva = Canva(
        like = 0,
        view = 0,
        #Gets the current time of the user when they add a new canva (including date and time)
        created_time = datetime.now(),
        popularity_percentage = 0.0
    )
    new_canva.add_view_and_calculating_popularity()
    new_canva.save()
    return {'Canva': new_canva.canva_json_response()}

@route_post(BASE_URL + 'likes', args = {'access_code':int})
def like_canva(args):
    if Canva.objects.filter(id=args['access_code']).exists():
        chosen_canva = Canva.objects.get(id=args['access_code'])
        # Why can't I chain them together
        chosen_canva.increase_like()
        chosen_canva.add_view_and_calculating_popularity()
        return {'Canva':chosen_canva.canva_json_response()}
    else: 
        return {'Error': "No canva exist"}
