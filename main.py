from utility.parsing import (get_post_data, get_posts, 
                             write_json, get_likes)

from tqdm import tqdm
import requests
from auth_data import token


def main():
    group_name = 'looksource' 
    #group_name = 'lookconsman' 
    raw_posts = get_posts(group_name, count=100, counts_amount=1)
    posts_data = [get_post_data(post) for post in raw_posts]
    write_json(posts_data, 'posts_100.json')
    
    ids = [post['id'] for post in posts_data]
    all_likes = {}
    for id in tqdm(ids):
        likes = get_likes(owner_id=-194512826, item_id=id)

        # make list containing one list to further proper pandas reading
        pandas_list = []
        pandas_list.append(likes)
        all_likes[id] = pandas_list

    write_json(all_likes, 'likes_100.json')
    

if __name__ == '__main__':
    main()