# -*- coding: utf-8 -*-
import urllib.request
import configparser
import yaml


def down_file(url, save_path, cookie):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Cookie": cookie
    }
    requests = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requests)
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


def batch_down():
    parse = load_yaml('conf.yaml')
    cookie = parse['cookie']
    batch_list = parse['batchdown']

    for batch in batch_list:
        url = batch['url']
        save_path = batch['save_path']
        if batch['status'] == "t":
            print(f'正在下载: {url}')
            down_file(url, save_path, cookie=cookie)
        else:
            continue


if __name__ == '__main__':
    batch_down()