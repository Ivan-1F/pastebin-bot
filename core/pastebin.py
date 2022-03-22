import requests

import config


def create_paste(paste: str, title: str):
    response = requests.post('https://pastebin.com/api/api_post.php', data={
        'api_dev_key': config.PASTEBIN_API_KEY,
        'api_paste_code': paste,
        'api_option': 'paste',
        'api_paste_name': title
    })
    return response.text


if __name__ == '__main__':
    print(create_paste('Hello', 'Title'))
