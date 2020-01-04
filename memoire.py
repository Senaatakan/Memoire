"""Oyunda ekranda beliren dairenin rengi ve içinde yazan sayı akılda tutulur. Ardından gelen ekrandaki dairenin
 rengi çncekiyle aynı renkse space tuşuna basarak 20 puan kazanılır. Aynı zamanda önceki ekrandaki sayı sonraki
 ekrandaki sayıyı tam bölüyorsa veya sonraki ekrandaki sayı önceki ekrandaki sayıyı tam bölüyorsa space tuşuna
 basarak 20 puan kazanılır. Yanlış anda tuşa basılırsa 30 puan kaybedilir. 100 puana ulaşan oyuncu oyunu kazanır."""


import random
import turtle
import time

sonucTurtle=turtle.Turtle()
daireTurtle=turtle.Turtle()
sayiTurtle=turtle.Turtle()
skorTurtle=turtle.Turtle()

skor = 0


skorTurtle.speed(0)
skorTurtle.hideturtle()
skorTurtle.penup()
skorTurtle.setpos(-350,0)
skorTurtle.color("black")
daireTurtle.width = 5    
daireTurtle.speed(0)
sonucTurtle.penup()
sonucTurtle.hideturtle()
sonucTurtle.setpos(0,230)
sayiTurtle.hideturtle()
daireTurtle.hideturtle()

liste=["pink","red","green","blue","orange"]

skorTurtle.write(skor, align="center",font= ("Arial",15,"normal"))



renk = random.choice(liste)
sayi = random.randint(3,5)
ilkrenk = "orange"
ilksayi = 10
def f():
    global skor
    global ilkrenk
    global ilksayi
    global renk
    global sayi
    if((ilkrenk == renk) or (sayi%ilksayi == 0) or (ilksayi%sayi==0)):
        skor +=20
    else:
        skor -=30
    skorTurtle.clear()
    skorTurtle.write(skor, align="center",font= ("Arial",15,"normal"))
turtle.listen()
turtle.onkey(f, "space")


starttime = time.time()



while (skor<100 and skor>-100):
    
    daireTurtle.dot(400,renk)
    sayiTurtle.write(sayi, align="center", font= ("Arial",40,"normal"))
    
    
    endtime = time.time()
    duration = int(endtime - starttime)

    if(duration == 2):
        starttime = time.time()
        ilkrenk = renk
        ilksayi = sayi
        renk = random.choice(liste)
        sayi = random.randint(3,30)
        
        
if(skor >= 100):
    sonucTurtle.color("green")
    sonucTurtle.write("Başardınız!", True, align="center",font= ("Arial",20,"normal"))
else:
    sonucTurtle.color("red")
    sonucTurtle.write("Kaybettiniz!", True, align="center",font= ("Arial",20,"normal"))