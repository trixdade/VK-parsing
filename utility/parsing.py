import json
import requests
from time import sleep
from tqdm import tqdm
from auth_data import token


def write_json(data, filename='posts.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=True)


stop = 0
def get_likes(
    owner_id: int, 
    item_id: int, 
    count: int = 1000, 
    offset_step: int = 1000,
    max_likes: int = 10000
    ) -> list:

    """
    Returning list of post likers 
    """

    all_likes = []
    
    global stop
    for offset in range(0, max_likes, offset_step):
        if stop%3 == 0:
            sleep(1)

        url = f"https://api.vk.com/method/likes.getList"
        stop += 1
        request_params = {
                'type': 'post',
                'access_token': token, 
                'owner_id': owner_id, 
                'count': count,
                'item_id': item_id, 
                'offset': offset,
                'v':5.131
                }
        
        try:
            req = requests.get(url, params=request_params)
            likes = req.json()['response']['items']
        except:
            sleep(1)
            req = requests.get(url, params=request_params)
            likes = req.json()['response']['items']

        if (len(likes)) == 0:
            break
        
        all_likes.extend(likes)

    return all_likes

def get_posts(
    group_name: str, 
    count: int = 100, 
    counts_amount: int = 5, 
    offset_step: int = 100,
    ) -> list:

    all_posts = []
    for offset in tqdm(range(0, count*counts_amount, offset_step)):
        url = f"https://api.vk.com/method/wall.get"
        req = requests.get(url, params={
            'domain': group_name, 
            'count': count, 
            'access_token': token, 
            'offset': offset,
            'extended': 1,
            'fields': 'id',
            'v':5.131
            })
        print(req.json())
        posts = req.json()['response']['items']
        all_posts.extend(posts)
    return all_posts


def get_post_data(post: dict) -> dict:
    try:
        post_id = post['id']
    except:
        post_id = -1
    
    try:
        owner_id = post['owner_id']
    except:
        owner_id = -1

    try:
        date = post['date']
    except:
        date = -1

    try:
        text = post['text']
    except:
        text = -1

    try:
        likes = post['likes']['count']
    except:
        likes = -1

    try:
        reposts = post['reposts']['count']
    except:
        reposts = -1
    
    try:
        attachments = post['attachments']
    except:
        attachments = -1
    
    try:
        marked_as_ads = post['marked_as_ads']
    except:
        marked_as_ads = -1

    post_data = {
        'id': post_id,
        'owner_id': owner_id,
        'date': date,
        'text': text,
        'likes': likes,
        'reposts': reposts,
        'attachments': attachments,
        'marked_as_ads': marked_as_ads
    }

    return post_data