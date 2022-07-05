from tkinter import *
from alarm import*
from stop import*
from clock import*
from timer import*

root=Tk()
root.title("CLOCK")
root.geometry('567x300')
root.configure(bg="black")

strimg=PhotoImage(file="play.png")
stpimg=PhotoImage(file="pause.png")
rstimg=PhotoImage(file="reset.png")
lapimg=PhotoImage(file="lap.png")
alarm_img=PhotoImage(file="alarm.png")
stop_img=PhotoImage(file="stopwatch.png")
timer_img=PhotoImage(file="timer.png")
clock_img=PhotoImage(file="clock.png")

l=Label(root,text="WELCOME",font="times 50 bold",fg="white",bg="black")
l.place(x=100,y=125)

but_alarm=Button(root,command=lambda:alarm(root,but),bg="black")
but_clock=Button(root,command=lambda:clock1(root),bg="black")
but_timer=Button(root,command=lambda:timer(root,but,img),bg="black")
but_stop=Button(root,command=lambda:stop(root,but,img),bg="black")                                                                     
but_alarm.place(x=1,y=5)
but_clock.place(x=141.6,y=5)
but_timer.place(x=283,y=5)
but_stop.place(x=424,y=5)

but_img=[alarm_img,clock_img,timer_img,stop_img]
but=[but_alarm,but_clock,but_timer,but_stop]
img=[strimg,stpimg,rstimg,lapimg]

for i in range(4):
    but[i].config(image=but_img[i],relief=FLAT,width=141.5)
    
mainloop()
