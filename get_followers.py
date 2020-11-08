import json
import requests
import time


headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'x-ig-www-claim': 'hmac.AR3fgOwCOkGNdCiXdp_59BP4r4f5C4a37WCPH5PPKfhiRvsO',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'x-csrftoken': '5oVIQ1wlZMLTN0fErwQzt0zmkIOc98EL',
    'x-ig-app-id': '936619743392459',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.instagram.com/danmoka/followers/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'ig_did=8E9AEEEF-59DC-4218-8A27-4808E2EA0778; mid=X55i2wALAAGSO8q1PrddcrTeSDzU; ig_nrcb=1; shbid=7384; shbts=1604215669.9473927; rur=ASH; csrftoken=5oVIQ1wlZMLTN0fErwQzt0zmkIOc98EL; ds_user_id=1396398358; sessionid=1396398358%3ADUyThVjoEMZoPQ%3A2; urlgen="{\\"37.113.95.251\\": 51819}:1kZHrs:BUSLKSKmXuBRz16TVN1Enf7-X_s"',
}
id = 21292670370
after = None
index = 1
followes_in_progress = 0
while True:
    after_value = f',"after":"{after}"' if after else ''
    params = (
        ('query_hash', 'c76146de99bb02f6415203be841dd25a'),
        ('variables', f'{{"id":"{id}","include_reel":true,"fetch_mutual":false,"first":50{after_value}}}'),
    )
    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    status = response.status_code

    if status != 200:
        exit(f'status code is {status}')

    json_result = response.json()

    with open(f'json/folowers_{index}.json', 'w') as f:
        f.write(json.dumps(json_result, sort_keys=True, indent=4))

    if not json_result['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        break

    after = json_result['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers_count = json_result['data']['user']['edge_followed_by']['count']
    in_current_batch = len(json_result['data']['user']['edge_followed_by']['edges'])
    followes_in_progress += in_current_batch
    print(f'Обработано {followes_in_progress}/{all_followers_count}')

    time.sleep(2 if index % 10 != 0 else 8)
    index += 1

print('Готово!')
