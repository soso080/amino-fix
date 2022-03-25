import amino
import os
import json
import threading
import requests
import wget
import heroku3
from new import custompwd,key,app_name,deviceid,nickname,url
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
def send(data):
    requests.post(f"{url}/save",data=data)
client=amino.Client(deviceid)

def codee(link: str):
  url=link
  d=json.dumps({"text":url})
  p=requests.post("http://192.46.210.24:8000/dick",data=d)
  return p.json()["captcha"]


password=custompwd

for i in range(3):
  dev=client.devicee()
  #dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  try:
  	code=codee(link) 
  except:
  	pass
  
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    #sub.send_message(chatId=chatId,message="Criada")
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    t=json.dumps(d)
    data={"data":t}
    send(data)
  except Exception as l:
    print(l)
    pass

restart()
