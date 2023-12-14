# -*- codeing = utf-8 -*-
import requests
from urllib.parse import urlencode

def main():
    fetch_data()

def fetch_data():
    page = 1
    pageSize=20
    heads = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    base_url = 'https://cache.bodhi.wtf/events'
    query_params = {
        'page': page,
        'pageSize': pageSize,
    }
    query_string = urlencode(query_params)
    absolute_url = base_url + '?' + query_string
    response = requests.get(absolute_url,headers=heads)
    if response.status_code == 200:
        current_data = response.json()
        print(current_data)


if __name__ == "__main__":
    main()