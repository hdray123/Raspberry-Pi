## 盲阅

引用了百度开源ai的[sdk](https://ai.baidu.com/)

可以自己申请，我使用的图片文字识别 和文字转语音都不用钱

申请账号创建好后会给 APP_ID、API_KEY、SECRET_KEY

```python
APP_ID = 'xxxxxxx'
API_KEY = 'xxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxx'
```

使用python2.7需要的第三方库在[requirements.txt](./requirements.txt)

目前只做到了图像文字到文本文字在到盲文的步骤和文本文字转换成语音的步骤，和实现照相的拍取。盲文的显示器这一硬件设施并未实现。

