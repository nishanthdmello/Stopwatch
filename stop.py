from tkinter import *
t1=0;i=0

def convert(t2):
    t=[0,0,0,0]
    t[0]=t2//360000; t2%=360000
    t[1]=t2//6000;    t2%=6000
    t[2]=t2//100;  t[3]=t2%100

    for i in range(4):
        if t[i]<10:
            t[i]="0"+str(t[i])
    
    return t

def update():
    if a:
        global t1 
        h,m,s,cs=convert(t1)
        l.config(text=f"{h}:{m}:{s}.{cs}")
        t1+=1
        l.after(10,update)

def start():
    global a;a=1
    b3['state']=NORMAL        
    b1.config(command=stop,image=img[1])
    update()

def stop(): 
    global a;a=0
    b3['state']=DISABLED 
    b1.config(command=start,image=img[0])

def reset():
    global a,t1;a=0;t1=0
    b3['state']=DISABLED 
    b1.config(command=start,image=img[0])
    l.config(text="00:00:00.00")
    
    for i in lap_frame.winfo_children():
        i.destroy()     
    
def lap():
    global i;i+=1
    if i==10: 
        b3['state']=DISABLED
    h,m,s,cs=convert(t1)
    la=Label(lap_frame,text=f"{h}:{m}:{s}.{cs}",font="Helvetica 20",bg="black",fg="white") 
    la.pack()


# All declarations are here

root=Tk()
root.title("Stopwatch")
root.geometry('490x280')
root.configure(bg="black") 

strimg=PhotoImage(file="play.png")
stpimg=PhotoImage(file="pause.png")
rstimg=PhotoImage(file="reset.png")
lapimg=PhotoImage(file="lap.png")
img=[strimg,stpimg,rstimg,lapimg]    
    
but_frame=LabelFrame(root,padx=10,pady=10,bg="black")
but_frame.pack(pady=20)

l=Label(root,text="00:00:00.00",font=("Helvetica",50),bg="black",fg="white")
l.pack(padx=10,pady=25)

lap_frame=Frame(root,padx=10,bg="black")
lap_frame.pack()


b1=Button(but_frame,relief=FLAT,bg="black",image=img[0],command=start)
b2=Button(but_frame,relief=FLAT,bg="black",image=img[2],command=reset,padx=10)
b3=Button(but_frame,relief=FLAT,bg="black",image=img[3],command=lap,padx=10,state=DISABLED)
b1.grid(row=0,column=0,padx=20)
b2.grid(row=0,column=3,padx=20)
b3.grid(row=0,column=6,padx=20)

mainloop()

  
