import requests
from bs4 import BeautifulSoup
from time import sleep


def get_all_users(group, token):
    url = 'https://api.vk.com/method/groups.getMembers?group_id={}&access_token={}'.format(group, token)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    users = int(soup.text.split(':')[2].split(',')[0])
    return users


def get_users_id(group, token, ofset):
    ofset = ofset * 1000
    url = 'https://api.vk.com/method/groups.getMembers?group_id={}&offset={}&access_token={}'.format(group,
                                                                                                             ofset,
                                                                                                             token)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    response = soup.text.split('[')[1].replace(']', '').replace('}', '').split(',')
    sleep(0.4)
    return response


def save_file(ids):
    with open('id.txt', 'a') as f:
        for i in ids:
            a = i + '\n'
            f.write(a)


def main():
    group = 'velo_dom'

    token = '32f5ef7157bb844a521370fa63b535122852fedd739ad9c8a79fa78042417b9f0fcdb5ce6e50abb954ae5'
    users = get_all_users(group, token)
    count = users // 1000
    print(count)
    ids = []
    cou = 0
    for i in range(count + 1):
        index = get_users_id(group, token, ofset=i)
        print(cou, '\n', index)
        for a in index:
            ids.append(a)
        cou += 1
    print(ids)
    count1 = 0
    for i in ids:
        count1 += 1
    print(count1)
    save_file(ids)


if __name__ == '__main__':
    main()
