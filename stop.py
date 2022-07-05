from tkinter import *

def stop(root,but,img):

    stop_frame=Frame(root,padx=75,bg="black")
    stop_frame.place(x=15,y=45) 
    global t1,i;t1=0;i=0

    def convert(t):

        
        
            
        h=t//360000;   t-=h*360000       
        m=t//6000; t-=m*6000
        s=t//100;  cs=t-s*100
       
        if h<10:
            h="0"+str(h)
        if m<10:
            m="0"+str(m)
        if s<10:
            s="0"+str(s)
        if cs<10:
            cs="0"+str(cs)
            
        return h,m,s,cs

    def start():
 
        global a;a=1
        b3['state']=NORMAL        
        b1.config(command=stop,image=img[1])
        for i in but:
            i['state']=DISABLED
        
        def update():            
            if a!=0:
                global t1 
                h,m,s,cs=convert(t1)
                l.config(text=f"{h}:{m}:{s}.{cs}")
                t1+=1
                l.after(10,update)
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
        for i in but:
            i['state']=NORMAL  
        for i in lap_frame.winfo_children():
            i.destroy()     
        
    def lap():

        global i;i+=1
        if i==13: 
            b3['state']=DISABLED
        h,m,s,cs=convert(t1)
        la=Label(lap_frame,text=f"{h}:{m}:{s}.{cs}"
        ,font="Helvetica 20",bg="black",fg="white") 
        la.pack()

    
    
    but_frame=LabelFrame(stop_frame,padx=10,pady=10,bg="black")
    l=Label(stop_frame,text="00:00:00.00",font=("Helvetica",50),bg="black",fg="white")
    lap_frame=Frame(stop_frame,padx=10,bg="black")

    but_frame.pack(pady=20)
    l.pack(padx=10,pady=25)
    lap_frame.pack()

    b1=Button(but_frame,relief=FLAT,bg="black",image=img[0],command=start)
    b2=Button(but_frame,relief=FLAT,bg="black",image=img[2],command=reset,padx=10)
    b3=Button(but_frame,relief=FLAT,bg="black",image=img[3],command=lap,padx=10,state=DISABLED)
    b1.grid(row=0,column=0,padx=20)
    b2.grid(row=0,column=3,padx=20)
    b3.grid(row=0,column=6,padx=20)


  
