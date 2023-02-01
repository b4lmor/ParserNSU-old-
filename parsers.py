import requests
import json


def get_data_A():

    cookies = {
        '_ym_d': '1644686242',
        '_ym_uid': '1644686242404219752',
        '_ga': 'GA1.2.1357313403.1655311867',
        '_gid': 'GA1.2.203528922.1656860411',
        '_ym_isad': '2',
        'advanced-frontend': 'm9dorp94t0gqttmoortastj2r2',
        '_csrf-frontend': 'c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'abiturient.nsu.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryE22xSSAGUWSsxtbK',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_d=1644686242; _ym_uid=1644686242404219752; _ga=GA1.2.1357313403.1655311867; _gid=GA1.2.203528922.1656860411; _ym_isad=2; advanced-frontend=m9dorp94t0gqttmoortastj2r2; _csrf-frontend=c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D; _ym_visorc=w',
        'origin': 'https://abiturient.nsu.ru',
        'referer': 'https://abiturient.nsu.ru/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = '------WebKitFormBoundaryE22xSSAGUWSsxtbK\r\nContent-Disposition: form-data; name="_csrf-frontend"\r\n\r\nXCKXHiPu84pBzTLJFpBuW4CorWELHolbY3xdw9aEXSMvbMVmbIKeugW3XZl-3BsOx8vMECYtuSgMSzKigOtwcA==\r\n------WebKitFormBoundaryE22xSSAGUWSsxtbK\r\nContent-Disposition: form-data; name="type"\r\n\r\n20\r\n------WebKitFormBoundaryE22xSSAGUWSsxtbK\r\nContent-Disposition: form-data; name="condition"\r\n\r\n10\r\n------WebKitFormBoundaryE22xSSAGUWSsxtbK\r\nContent-Disposition: form-data; name="faculty"\r\n\r\n8\r\n------WebKitFormBoundaryE22xSSAGUWSsxtbK\r\nContent-Disposition: form-data; name="direction"\r\n\r\n374\r\n------WebKitFormBoundaryE22xSSAGUWSsxtbK--\r\n'

    response = requests.post('https://abiturient.nsu.ru/bachelor/list-content', cookies=cookies, headers=headers, data=data)

    with open(f'result.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def get_data_B():
    cookies = {
        '_ym_d': '1644686242',
        '_ym_uid': '1644686242404219752',
        '_ga': 'GA1.2.1357313403.1655311867',
        '_gid': 'GA1.2.203528922.1656860411',
        'advanced-frontend': 'm9dorp94t0gqttmoortastj2r2',
        '_csrf-frontend': 'c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'abiturient.nsu.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarycOS1tKjYf3sX9AZx',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_d=1644686242; _ym_uid=1644686242404219752; _ga=GA1.2.1357313403.1655311867; _gid=GA1.2.203528922.1656860411; advanced-frontend=m9dorp94t0gqttmoortastj2r2; _csrf-frontend=c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D; _ym_isad=2; _ym_visorc=w',
        'origin': 'https://abiturient.nsu.ru',
        'referer': 'https://abiturient.nsu.ru/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = '------WebKitFormBoundarycOS1tKjYf3sX9AZx\r\nContent-Disposition: form-data; name="_csrf-frontend"\r\n\r\n7NpZWfhLh_HqbwRJp34OqTN7df2c86CPTk__AdQqH2uflAshtyfqwa4VaxnPMnv8dBgUjLHAkPwheJBggkUyOA==\r\n------WebKitFormBoundarycOS1tKjYf3sX9AZx\r\nContent-Disposition: form-data; name="type"\r\n\r\n20\r\n------WebKitFormBoundarycOS1tKjYf3sX9AZx\r\nContent-Disposition: form-data; name="condition"\r\n\r\n10\r\n------WebKitFormBoundarycOS1tKjYf3sX9AZx\r\nContent-Disposition: form-data; name="faculty"\r\n\r\n8\r\n------WebKitFormBoundarycOS1tKjYf3sX9AZx\r\nContent-Disposition: form-data; name="direction"\r\n\r\n369\r\n------WebKitFormBoundarycOS1tKjYf3sX9AZx--\r\n'

    response = requests.post('https://abiturient.nsu.ru/bachelor/list-content', cookies=cookies, headers=headers, data=data)

    with open(f'result.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def get_data_C():
    cookies = {
        '_ym_d': '1644686242',
        '_ym_uid': '1644686242404219752',
        '_ga': 'GA1.2.1357313403.1655311867',
        '_gid': 'GA1.2.203528922.1656860411',
        'advanced-frontend': 'm9dorp94t0gqttmoortastj2r2',
        '_csrf-frontend': 'c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'abiturient.nsu.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfCtqS4apvnCpHu1n',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_d=1644686242; _ym_uid=1644686242404219752; _ga=GA1.2.1357313403.1655311867; _gid=GA1.2.203528922.1656860411; advanced-frontend=m9dorp94t0gqttmoortastj2r2; _csrf-frontend=c1f71c23c80a416e6b5bf81d733ff9ebee2cc67139d8ba0c79662851d1de8e30a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22sNRxOlm0DzoPhLuUGcaq-30so7oaVo-S%22%3B%7D; _ym_isad=2; _ym_visorc=w',
        'origin': 'https://abiturient.nsu.ru',
        'referer': 'https://abiturient.nsu.ru/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = '------WebKitFormBoundaryfCtqS4apvnCpHu1n\r\nContent-Disposition: form-data; name="_csrf-frontend"\r\n\r\n7NpZWfhLh_HqbwRJp34OqTN7df2c86CPTk__AdQqH2uflAshtyfqwa4VaxnPMnv8dBgUjLHAkPwheJBggkUyOA==\r\n------WebKitFormBoundaryfCtqS4apvnCpHu1n\r\nContent-Disposition: form-data; name="type"\r\n\r\n20\r\n------WebKitFormBoundaryfCtqS4apvnCpHu1n\r\nContent-Disposition: form-data; name="condition"\r\n\r\n10\r\n------WebKitFormBoundaryfCtqS4apvnCpHu1n\r\nContent-Disposition: form-data; name="faculty"\r\n\r\n6\r\n------WebKitFormBoundaryfCtqS4apvnCpHu1n\r\nContent-Disposition: form-data; name="direction"\r\n\r\n347\r\n------WebKitFormBoundaryfCtqS4apvnCpHu1n--\r\n'

    response = requests.post('https://abiturient.nsu.ru/bachelor/list-content', cookies=cookies, headers=headers, data=data)
    
    with open(f'result.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)