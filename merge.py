

import requests
import json
import base64

class MergeFace():
    def merge(self,url,**kwargs):
        params = dict(**kwargs)
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        try:
            req = requests.post(url=url,data=dict(params), headers = headers)
            resultInJsonObject = req.json()
            resultInBase64 = resultInJsonObject.get('result')
            with open('/home/liangxia/PycharmProjects/test/cn/zjnu/MergeFace/imgae/IMG_0130.jpg','wb') as resultfile:
                resultfile.write(base64.b64decode(resultInBase64))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    url = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
    api_key = '2DIrbVtZJLjsZyjhG7I3W3xObnSV9l4j'
    api_secret = '2-lBpzCX_XnTXMwrUU8XgFkVq5p-LYxI'
    with open('/home/liangxia/PycharmProjects/test/cn/zjnu/MergeFace/imgae/IMG_0128.jpg','rb') as buff1:
        image_data1 = buff1.read()
        template_base64 = base64.b64encode(image_data1)
    with open('/home/liangxia/PycharmProjects/test/cn/zjnu/MergeFace/imgae/IMG_0129.jpg','rb') as buff2:
        image_data2 = buff2.read()
        merge_base64 = base64.b64encode(image_data2)
    template_rectangle =str('70,80,100,100')
    mergeface = MergeFace()
    mergeface.merge(url=url,api_key=api_key,api_secret=api_secret,template_base64=template_base64,merge_base64=merge_base64)



