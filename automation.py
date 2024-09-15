import pyautogui as p
import time as t
name =input("Enter the message to send : ")#("hello \n"*100)
num = int(input("enter the number for sending : "))
t.sleep(2)
print("loading....")
t.sleep(2)
for i in range(num):
          p.typewrite(name)
          p.press("enter")
p.alert('do you like this code')
          
          
