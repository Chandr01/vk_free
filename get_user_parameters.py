# -*- coding: utf-8 -*-
import requests
from time import sleep
import json


def open_file():
    users = []
    with open('id.txt', 'r') as f:
        for i in f:
            users.append(i)
    return users


def get_all_users(user, token):
    url = 'https://api.vk.com/method/groups.get?user_id={}&extended=1&v=5.68&access_token={}'.format(user, token)
    req = requests.get(url)
    data = req.json()

    print(user, ' - ', data['response']['count'])
    groups_names = []
    for i in data['response']['items']:
        name = i['name']
        groups_names.append(name)

    to_write = {'user': user, 'names': groups_names}

    print(to_write)
    with open('groups.txt', 'a') as f:
        json.dump(to_write, f)
        f.write('\n')


def main():
    users = open_file()

    for user in users:
        user = user.strip()
        token = '32f5ef7157bb844a521370fa63b535122852fedd739ad9c8a79fa78042417b9f0fcdb5ce6e50abb954ae5'
        try:
            get_all_users(user, token)
        except:
            print(user, ' - no groups')
        sleep(0.4)


if __name__ == '__main__':
    main()
