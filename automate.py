import pyautogui as pg
import pyperclip as pc
import webbrowser as wb
import time
mail = input("email : ")
password = input("password : ")
file = open("message.txt","r")
r = file.read().split("\n")
mailto = input("send mail to : ")
if "," in mailto:
    mailto = mailto.split(",")
else:
    mailto = [mailto]
print(mailto)
subject = r[0]
body = "%0A".join(r[1:])
def send_message(mailto,subject,body):
    l = f'https://mail.google.com/mail/u/0/?fs=1&to={mailto}&su={subject}&body={body}&tf=cm'
    pc.copy(l)
    pg.hotkey('ctrl','e')
    time.sleep(10)
    pg.press("backspace")
    pg.hotkey('ctrl','v')
    pg.press('enter')
    img("6.jpg")
    pg.moveTo(138,699)
    time.sleep(10)
    pg.click(x = 138,y = 699)
    print("Successfully send")
def img(n):
    n="./img/"+n
    img = pg.locateCenterOnScreen(n,confidence=.5,grayscale=True)
    error1 = pg.locateCenterOnScreen("./img/error1.jpg",confidence=.6,grayscale=True)
    error2 = pg.locateCenterOnScreen("./img/error2.jpg",confidence=.6,grayscale=True)
    while img==None:
        img = pg.locateCenterOnScreen(n,confidence=.5,grayscale=True)
        error1 = pg.locateCenterOnScreen("./img/error1.jpg",confidence=.6,grayscale=True)
        error2 = pg.locateCenterOnScreen("./img/error2.jpg",confidence=.6,grayscale=True)
        time.sleep(1)
        if error1!=None or error2!=None:
            raise Exception("No or weak internet connection")
    return img
def s(mail,password,subject,body,mailto):
    wb.open("https://google.com")
    img("1.jpg")
    pg.hotkey("win","up")
    pg.hotkey('ctrl','shift','n')
    img("2.jpg")
    pg.write("https://accounts.google.com/signin/v2/identifier?hl=en-GB&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    pg.press('enter')
    img("3.jpg")
    pg.write(mail)
    pg.press("enter")
    img("4.jpg")
    pg.hotkey("win","up")
    pg.write(password)
    pg.press('enter')
    img("5.jpg")
    for i in mailto:
        send_message(i,subject,body)
s(mail,password,subject,body,mailto)
