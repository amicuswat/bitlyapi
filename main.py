import os
import sys

import argparse

import json
import requests

from urllib.parse import urlparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TOKEN')

    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()

    url_ = args.url

    url_parsed = urlparse(url_)
    bitlink_url = url_parsed.netloc + url_parsed.path

    bitlink_code = is_bitlink(token, bitlink_url)

    if bitlink_code == 200:
        response = count_clicks(token, bitlink_url)
        clicks = response.json()['total_clicks']
        print('Clicks:', clicks) 
    elif bitlink_code == 403:
        print('Error - you do not have acces to this bitlink')
        sys.exit()
    else:
        response = shorten_link(token, url_)
        if response.ok:
            print(response.json()['link'])
        else:
            response.raise_for_status()
   

def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)

    return response.status_code
       

def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = f'{{"long_url": "{url}"}}' 
        
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    
    return response


def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    
    params = (
        ('unit', 'day'),
        ('units', '-1'),
    )

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary', headers=headers, params=params)
    
    return response


if __name__ == '__main__':
    main()

