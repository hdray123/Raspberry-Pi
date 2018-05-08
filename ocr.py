#coding:utf-8
from aip import AipOcr

APP_ID = 'xxxxxxx'
API_KEY = 'xxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


'''将识别出来的文字保存在txt文本'''
def save_str(picture_path='cc.jpg',save_txt='dd.txt'):
    image = get_file_content(picture_path)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    result=client.basicGeneral(image, options)
    str=''
    for word_list in result['words_result']:
        str=str+word_list['words'].encode('utf-8')
    with open(save_txt,'w') as f:
        f.write(str)
if __name__ == '__main__':
    save_str()