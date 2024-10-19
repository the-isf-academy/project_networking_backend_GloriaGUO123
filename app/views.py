# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Emoji, Canva

# @route_get(BASE_URL + 'all/emoji')
# # def all_emojis(args = {'access_code':int}):
# def all_emojis(args):
#     emojis_list = []
#     for emoji in Emoji.objects.all():
#         emojis_list.append(emoji.json_response())
#     if emojis_list != []:
#         return {'Emojis': emojis_list}
#     elif emojis_list == []:
#         return {'Error': 'No emojis exist currently'}

@route_get(BASE_URL + 'all/emoji', args = {'access_code':int})
def all_emojis(args):
    for canva in Canva.objects.all():
        if canva.checking_accesscode(args['access_code']) == True:
            emojis_list = []
            user_canva = Canva.objects.get(id=args['access_code'])
            print(user_canva)
            for emoji in user_canva.emojis:
                emojis_list.append(emoji.json_response())
            if emojis_list != []:
                return {'Emojis': emojis_list}
            elif emojis_list == []:
                return {'Error': 'No emojis exist currently'}
        elif canva.checking_accesscode(args['access_code']) == False:
                return {'Error': 'Access Code Incorrect'}

# @route_get(BASE_URL + 'all/canva')
# def all_canvas(args = {'accesscode':int}):
#         canvas_list = []
#         for canva in Canva.objects.all():
#             canvas_list.append(canva.json_response())
#         if canvas_list != []:
#             return {'Canvas': canvas_list}
#         elif emojis_list == []:
#             return {'Error': 'No canvas exist currently'}

@route_post(BASE_URL + 'new', args={'emoji':str, 'username': str})
def new_emoji(args):
    new_emoji = Emoji(
        emoji = args['emoji'],
        username = args['username'],
        )
    new_emoji.setting_position()
    new_emoji.save()
    return {'Emoji': new_emoji.json_response()}
    # if new_emoji.setting_position() == True:
    #     return {'Emoji': new_emoji.json_response()}
    
    # elif new_emoji.setting_position == False:
    #     return {'Error': 'The canva size has reached to its maximum'}