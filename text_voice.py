#coding:utf-8
import re
from aip import AipSpeech
APP_ID = 'xxxxxxxxxx'
API_KEY = 'xxxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



def read_str(save_txt='dd.txt'):
    with open('dd.txt', 'rb') as f:
        str = f.read()
    rule = re.compile(ur"[^\u4e00-\u9fa5]")
    str = rule.sub('', str.decode('utf-8'))
    return str

#变成声音
def text_voice():
    str=read_str("dd.txt")
    result  = client.synthesis(str, 'zh', 1, {
        'vol': 5,
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

if __name__ == '__main__':
    text_voice()