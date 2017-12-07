import requests
import datetime
import pandas as pd
from time import sleep
from tqdm import tqdm


def open_file():
    posts = []
    with open('posts.txt', 'r') as f:
        for i in f:
            posts.append(i)
    return posts


def clear_posts(posts):
    posts_ids = []
    for i in posts:
        post_id = i.split('wall')[1].strip()
        posts_ids.append(post_id)
    return posts_ids


def create_urls(ids, token):
    urls = []
    for i in ids:
        url = 'https://api.vk.com/method/wall.getById?posts={}&v=5.69&access_token={}'.format(i, token)
        urls.append(url)
    return urls


def get_data(urls, ids, token):
    data = {}
    count = 0
    for i in tqdm(urls):
        try:
            f_data = requests.get(i)
            gr_ind = ids[count].split('_')[0].replace('-', '')

            gr_members = 'https://api.vk.com/method/groups.getMembers?group_id={}&fields=city&v=5.69&access_token={}'.format(
                gr_ind, token)
            sleep(0.1)
            gr_link = requests.get(gr_members)
            gr_count = gr_link.json()['response']['count']
            # print(gr_count)
            try:
                city = gr_link.json()['response']['items'][3]['city']['title']
            except:
                city = 'Не указан'
            # print(city)
            sleep(0.1)
            if int(gr_count) >= 100:
                link = 'http://vk.com/wall{}'.format(ids[count])
                text = f_data.json()['response'][0]['text'].strip().replace('\n', ' ')
                Likes = f_data.json()['response'][0]['likes']['count']
                Reposts = f_data.json()['response'][0]['reposts']['count']
                date = datetime.datetime.fromtimestamp(f_data.json()['response'][0]['date']).strftime(
                    '%Y-%m-%d %H:%M:%S')
                data[count] = {'Ссылка': link, 'Дата публикации': date, 'В группе': gr_count, 'Лайки': Likes,
                               'Репосты': Reposts, 'Текст поста': text, 'Город': city}


            else:
                print(gr_count, 'members', i)
            count += 1
            sleep(0.2)
        except:
            print('Проскачили {}'.format(i))
            count += 1

    return data


def save_file(data):
    frame = pd.DataFrame(data).T
    frame.to_excel('{}.xlsx'.format(datetime.datetime.now().strftime('%Y-%m-%d')))


def main():
    token = '32f5ef7157bb844a521370fa63b535122852fedd739ad9c8a79fa78042417b9f0fcdb5ce6e50abb954ae5'
    posts = open_file()
    ids = clear_posts(posts)
    urls = create_urls(ids, token)
    data = get_data(urls, ids, token)

    save_file(data)


if __name__ == '__main__':
    main()
