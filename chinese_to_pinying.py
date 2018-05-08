#coding:utf-8
from pypinyin import lazy_pinyin
import re

'''读txt文本中的汉字返回 str'''
def read_str(save_txt='dd.txt'):
    with open('dd.txt', 'rb') as f:
        str = f.read()
    rule = re.compile(ur"[^\u4e00-\u9fa5]")
    str = rule.sub('', str.decode('utf-8'))
    return str



'''拼音转盲文'''
def str_to_Braille(save_txt='dd.txt'):

    str=read_str(save_txt)
    patern=re.compile('\w*')
    pinying=lazy_pinyin(str)
    list=[]
    for word in pinying:
        if patern.match(word.encode('utf-8')).group()!='':
            list.append(patern.match(word.encode('utf-8')).group())
    print(list)
    patern_1=re.compile('[b|p|m|f|d|t|n|l|g|j|k|q|h|x|r|z|c|s|y|w]')
    patern_2=re.compile('zh|ch|sh')
    patern_3=re.compile('ang|eng|ing|ong')
    patern_4=re.compile('un|vn|an|en|in|ie|ue|er|ao|ou|iu|ai|ei|ui')
    patern_5=re.compile('a|o|e|i|u|v')
    dict={'b':'12','p':'1234','m':'134','f':'124',
          'd':'145','t':'2345','n':'1345','l':'123',
          'g':'1245','k':'13','h':'125','j':'1245',
          'q':'13','x':'125','z':'1356','c':'14','s':'234','zh':'34',
          'ch':'12345','sh':'156','r':'245','y':'1246','w':'123456',
          'a':'3.5','o':'135','e':'26','i':'24','u':'136','v':'346',
          'ai':'246','ei':'2346','ui':'2456','ao':'235','ou':'12356',
          'iu':'1256','ie':'15','ue':'23456','er':'1235','an':'1236',
          'en':'356','in':'126','un':'25','vn':'456','ang':'236','eng':'3456',
          'ing':'16','ong':'256'
          }
    for word in list:
        try:
            str_first=patern_2.match(word).group()
        except AttributeError:
            try:
                str_first=patern_1.match(word).group()
            except AttributeError:
                pass

        word_end=word.replace(str_first,'')
        try:
            str_end=patern_3.match(word_end).group()
        except AttributeError:
            try:
                str_end=patern_4.match(word_end).group()
            except AttributeError:
                try:
                    str_end=patern_5.match(word_end).group()
                except AttributeError:
                    pass
        print(str_first,str_end)
        print(dict[str_first],dict[str_end])

if __name__ == '__main__':
    str_to_Braille()