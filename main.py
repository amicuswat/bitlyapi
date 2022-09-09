import os
import sys

import argparse
import requests

from urllib.parse import urlparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()

    bitlink_url = urlparse(args.url).netloc + urlparse(args.url).path

    if is_bitlink(token, bitlink_url):
        print('Clicks:', count_clicks(token, bitlink_url))
    else:
        print('Short link:', shorten_link(token, args.url))
   

def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)

    return response.ok
       

def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    long_url = f'{{"long_url": "{url}"}}'
        
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=long_url)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary', headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


if __name__ == '__main__':
    main()

