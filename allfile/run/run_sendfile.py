#coding:utf-8
import requests
import requests.sessions
import json

class SendFile():
    """企业微信机器人在群里面发文件"""

    #发送群组人数在群情况
    def send_group_assistant(self,file):
        # 文件上传接口
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media'
        headers = {'Content-Type': 'multipart/form-data'}
        files = {'file': open(file, 'rb')}

        params = {
            'key': 'aedf0ed5-f89e-451c-b54b-923c41c568e8',
            'type': 'file'
        }
        response = requests.post(url=url, headers=headers, params=params, files=files)
        media_id = response.json()['media_id']
        print("media_id的参数为：", response.json()['media_id'])

        # 机器人发送文件类型接口
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=aedf0ed5-f89e-451c-b54b-923c41c568e8'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "msgtype": "file",
            "file": {
                "media_id": media_id
            }
        }
        response2 = requests.post(url=url,headers=headers,json=payload)
        print("企业微信机器人上传文件返回结果为：", response2.json())



    # 上传文件接口方法
    def uploadFile(self):
        """上传文件接口"""
        # 文件上传接口
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media'
        headers = {'Content-Type': 'multipart/form-data'}
        files = {'file': open('D:\\FramWork\\allfile\\run\\群组每日在群情况统计(所有公司).xlsx', 'rb')}

        params = {
            'key': 'aedf0ed5-f89e-451c-b54b-923c41c568e8',
            'type': 'file'
        }
        response = requests.post(url=url, headers=headers, params=params, files=files)
        media_id = response.json()['media_id']
        print("media_id的参数为：", response.json()['media_id'])


if __name__ == '__main__':
    sendFile = SendFile()
    #sendFile.uploadFile()
    #sendFile.send_group_assistant("D:\\FramWork\\allfile\\run\\群组每日在群情况统计(所有公司).xlsx")
    #sendFile.send_group_assistant("D:\\FramWork\\allfile\\run\\每日助理在线情况统计(所有公司).xlsx")







