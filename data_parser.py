from re import M
from parsers import *
from pprint import pprint

def get_data(faculty: str, snils: str) -> dict:

    #keyword for my snils
    if snils == 'fox':
        snils = '207-413-866 49'

    #response preview [0/10]
    response = {
        'info': None,
        'attestat': None,
        'consent': None,
        'rating': None,
        'count_students': None,
        'av_in_point': None,
        'av_point': None,
        'user_score': None,
        'original_attestat_cnt': None,
        'consent_plus_attestat_cnt': None,
        'min_in_point': None,
        'place_cnt': None,
        'rating_attestat': None,
        'rating_attestat_with_consent': None,
    }

    #get json
    exec(f'get_data_{faculty}()')

    #read json
    with open(f'result.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)[0]
    
    #count places []
    place_number = data['info']['place']['enroll']['value']

    response['place_cnt'] = str(place_number)

    #write response info []
    response_info = data['info']['speciality']['group']
    response['info'] = response_info

    #forming list with data
    result_data = []

    number = 0
    for card in data['table']:

        number += 1

        #user card preview
        user = {
            'number': number,
            'snils': card['snils'],
            'score': None,
            'attestat': '+' if card['original'] == '✓' else '-',
            'consent': '+' if card['consent'] == '✓' else '-',
        }

        if card['disciplines'][3]['point'] == '✓':
            user['score'] = 'БВИ'
        else:
            user['score'] = int(card['sumPointTotal'])
        
        result_data.append(user)

    #getting good data from created list
    av_score = 0
    cnt_bvi = 0
    av_all_score = 0
    atet_cons_cnt = 0
    atet_cnt = 0
    my_numb_atet = 0
    my_numb_atet_cons = 0
    for user in result_data:
        if user['snils'] == snils:
            response_rating = user['number']
            response_attestat = user['attestat']
            response_cosent = user['consent']
            user_score = str(user['score'])

        if result_data.index(user) == place_number - 1:
            min_in_point = user['score']

        if isinstance(user['score'], int):
            if result_data.index(user) <= place_number - 1:
                av_score += user['score']
            av_all_score += user['score']
        else:
            cnt_bvi += 1
        if user['attestat'] == '+':
            if user['consent'] == '+':
                atet_cons_cnt += 1
                if user['snils'] == snils:
                    my_numb_atet_cons = atet_cons_cnt
            atet_cnt += 1
            if user['snils'] == snils:
                my_numb_atet = atet_cnt

    if 'response_rating' not in locals(): 
        response_rating = 'Абитуриент не найден.'
        response_attestat = '-'
        response_cosent = '-'
        user_score = '-'

    av_all_score /= len(result_data) - cnt_bvi
    av_score /= place_number - cnt_bvi

    #forming response []
    response['rating'] = str(response_rating)
    response['attestat'] = response_attestat
    response['consent'] = response_cosent
    response['min_in_point'] = str(min_in_point)
    response['av_in_point'] = '{0:.2f}'.format(av_score)
    response['av_point'] = '{0:.2f}'.format(av_all_score)
    response['user_score'] = user_score
    response['count_students'] = str(len(result_data))
    response['consent_plus_attestat_cnt'] = str(atet_cons_cnt)
    response['original_attestat_cnt'] = str(atet_cnt)
    response['rating_attestat'] = str(my_numb_atet)
    response['rating_attestat_with_consent'] = str(my_numb_atet_cons)

    return response


pprint(get_data('A', 'fox'))