import requests

def submit_flag(url,flag,token,event_hash):
    proxies = { "http": None, "https": None}
    data={
        "flag":f"{flag}",
        "token":f"{token}",
        "event_hash":f"{event_hash}"
    }

    try:
        res = requests.post(url=url,data=data,proxies=proxies)
        print(f"[+]success {url} " + res.text)
    except:
        print(f"[*]error {url}")
        pass


def bugku_awd(url,flag,token,event_id):
    proxies = { "http": None, "https": None}
    data={
        "flag":f"{flag}",
        "token":f"{token}",
        "id":f"{event_id}"
    }
    res = requests.post(url=url,data=data,proxies=proxies)
    print(res.text)


url="http://10.222.2.236:80/event_attack_defense/submit_flag/"  
token=""    
flag='test'

submit_flag(url,flag,"718e574a48c70728e682a646f0368c07","3d9b3bf1-adc4-48ea-b526-7e0f17322f8e.event")

bugku_awd("https://ctf.bugku.com/awd/submit.html",flag,token,'46')