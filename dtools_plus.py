# -*- coding: utf-8 -*-
import urllib.request
import configparser
import yaml
import multiprocessing
import requests


def down_file(url, save_path, cookie):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Cookie": cookie
    }
    print(f'正在下载: {url}')
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    with open(save_path, "wb") as f:
        f.write(data)


def load_conf(cfg):
    config = configparser.RawConfigParser()
    config.read(cfg, encoding='utf-8')
    return config


def load_yaml(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        result = yaml.safe_load(f)
    return result


def get_cookie():
    # 发送GET请求到目标网站
    response = requests.get('http://192.168.12.165:8980/')

    # 获取响应中的cookies
    cookies = response.cookies

    cookie_str = ''
    for cookie in cookies:
        if cookie.name == '_gitlab_session':
            cookie_str = f'{cookie.name}={cookie.value};'
            break
    print(cookie_str)
    return cookie_str


def batch_down():
    parse = load_yaml('conf.yaml')
    cookie = parse['cookie']
    batch_list = parse['batchdown']
    new_list = []
    for batch in batch_list:
        if batch['status'] == "t":
            url = batch['url']
            save_path = batch['save_path']
            new_arg = (url, save_path, cookie)
            new_list.append(new_arg)
        else:
            continue
    print(new_list)
    pool = multiprocessing.Pool(processes=len(new_list))
    pool.starmap(down_file, new_list)
    pool.close()
    pool.join()


if __name__ == '__main__':
    batch_down()