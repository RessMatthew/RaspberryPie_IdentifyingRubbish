import base64
import hashlib
import json
import time

from cv2 import cv2 as cv

import wx_sdk


def cap_face():
    cap = cv.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv.namedWindow("Capture Picture", cv.WINDOW_AUTOSIZE)
        cv.imshow("Picture", img)
        # 按q照相
        if cv.waitKey(1) == ord("q"):
            cv.imwrite("1.jpg", img)
            break

    cap.release()
    cv.destroyAllWindows()


def shibie():
    # cap_face()
    # path = "C:\\Users\\huawei\\Desktop\\suliao.png"
    path = "1.jpg"
    f = open(r'%s' % path, 'rb')

    Str = str(base64.b64encode(f.read()), encoding='utf-8')
    # print(Str)
    f.close()

    # url = 'https://way.jd.com/JDAI/garbageImageSearch'
    url = "https://aiapi.jd.com/jdai/garbageImageSearch"
    bodyStr = '{ 	"cityId":"310000", 	"imgBase64":"%s"}' % Str  # body中的内容

    timestamp = int(time.time() * 1000)
    secretKey = 'd4ad7839a0becf6eebdd7db8be543a35'
    sign = hashlib.md5((secretKey + str(timestamp)).encode()).hexdigest()

    params = {
        'appkey': '0ae605a4e4fedd3ab0ec0eecc4789fbd',  # 需要填入自己的appkey
        'timestamp': timestamp,
        'sign': sign
    }

    response = wx_sdk.wx_post_req(url, params, bodyStr=bodyStr)
    return_dic = json.loads(response.text)
    # print(return_dic)

    respond = return_dic['code']
    # respond_msg = return_dic['msg']
    print("response Code: ", respond)
    # arr = return_dic['result']['result']['garbage_info']
    arr = return_dic['result']['garbage_info']
    # if (respond == "10000") & (respond_msg == "查询成功,扣费"):
    if (respond == "10000"):
        # max = arr[0]['confidence']
        maxId = 0
        # for i in range(len(arr)):
        #     if arr[i]['confidence'] > max:
        #         max = arr[i]['confidence']
        #         maxId = i
        print("垃圾名称：{}-类别：{}".format(arr[maxId]['garbage_name'], arr[maxId]['cate_name']))
        # 投放建议：
        print(arr[maxId]['ps'])
        # print("垃圾： ", arr[maxId]['cate_name'])
        # print("名称： ", arr[maxId]['garbage_name'])
        # print("建议： ", arr[maxId]['ps'])
    else:
        print("眼前一片洁净 ， 没有发现垃圾")


if __name__ == '__main__':
    # while True:
    shibie()
    # time.sleep(2)
