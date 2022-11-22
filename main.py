from utility.parsing import (get_post_data, get_posts, 
                             write_json, get_likes)

from tqdm import tqdm


def main():
    group_name = 'looksource' 
    #group_name = 'lookconsman' 
    raw_posts = get_posts(group_name, count=3, counts_amount=1)
    print(raw_posts)
    posts_data = [get_post_data(post) for post in raw_posts]
    write_json(posts_data, 'data/pos.json')
    ids = [post['id'] for post in posts_data]
    all_likes = {}
    for id in tqdm(ids):
        likes = get_likes(owner_id=-194512826, item_id=id)

        # make list containing one list for proper further pandas reading
        pandas_list = []
        pandas_list.append(likes)
        all_likes[id] = pandas_list

    write_json(all_likes, 'data/lik.json')


if __name__ == '__main__':
    main()