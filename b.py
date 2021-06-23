import tkinter
from tkinter import *
from tkinter import messagebox

root=tkinter.Tk()
root.title('TIC-TAC-TOE')
root.iconbitmap('tictactoe.ico')
root.geometry('270x300')
root.resizable(0,0)


bg_color='#064884'
button_color="#e15a2b"
green='#1CF148'
reddish_color='#DDB59F'


def buttons_disabled():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


frame=LabelFrame(root,bg=bg_color)
frame.pack(fill=BOTH,expand=True)
var='x'
count=0
won=False

def win():
    global won
    if b1['text']==b2['text']==b3['text']!=' ':
        won=True
        b1.config(bg=green)
        b2.config(bg=green)
        b3.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()


    elif b4['text']==b5['text']==b6['text']!=' ':
        won=True
        b4.config(bg=green)
        b5.config(bg=green)
        b6.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b7['text']==b8['text']==b9['text']!=' ':
        won=True
        b7.config(bg=green)
        b8.config(bg=green)
        b9.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b1['text']==b4['text']==b7['text']!=' ':
        won=True
        b1.config(bg=green)
        b4.config(bg=green)
        b7.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b2['text']==b5['text']==b8['text']!=' ':
        won=True
        b2.config(bg=green)
        b5.config(bg=green)
        b8.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b3['text']==b6['text']==b9['text']!=' ':
        won=True
        b3.config(bg=green)
        b6.config(bg=green)
        b9.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b1['text']==b5['text']==b9['text']!=' ':
        won=True
        b1.config(bg=green)
        b5.config(bg=green)
        b9.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()

    elif b3['text']==b5['text']==b7['text']!=' ':
        won=True
        b3.config(bg=green)
        b5.config(bg=green)
        b7.config(bg=green)
        if var=='x':
          messagebox.showinfo("RESULT",'X WON')
          buttons_disabled()
        elif var=='o':
          messagebox.showinfo("RESULT","O WON")
          buttons_disabled()



def reset():
    global var
    global count
    global won
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10
    var='x'
    count=0
    won=False
    b1=Button(frame,bg=button_color,text=" ",height=3,width=10,command=lambda:trigger(b1))
    b2=Button(frame,bg=button_color,height=3,text=" ",width=10,command=lambda:trigger(b2))
    b3=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b3))
    b4=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b4))
    b5=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b5))
    b6=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b6))
    b7=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b7))
    b8=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b8))
    b9=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b9))
    b10=Button(frame,bg=reddish_color,height=3,width=10,text="RESET GAME",command=reset)

    b1.grid(row=0,column=0,padx=5,pady=5)
    b2.grid(row=0,column=1,padx=5,pady=5)
    b3.grid(row=0,column=2,padx=5,pady=5)
    b4.grid(row=1,column=0,padx=5,pady=5)
    b5.grid(row=1,column=1,padx=5,pady=5)
    b6.grid(row=1,column=2,padx=5,pady=5)
    b7.grid(row=2,column=0,padx=5,pady=5)
    b8.grid(row=2,column=1,padx=5,pady=5)
    b9.grid(row=2,column=2,padx=5,pady=5)
    b10.grid(row=3,column=0,columnspan=3,padx=0,pady=5)




def trigger(b):
    global var
    global count
    if count<8:
        if b["text"]==" ":
         if var=='x':
            b.config(text="X")
            count+=1
            win()
            var='o'
         elif var=='o':
            b.config(text="O")
            count+=1
            win()
            var='x'
        else:
            messagebox.showinfo("WRONG INPUT","YOU SELECTED WRONG BOX")
    else:
        if not won:
            if b["text"]==" ":
             if var=='x':
                b.config(text="X")
                count+=1
                win()
                var='o'
             elif var=='o':
                b.config(text="O")
                count+=1
                win()
                var='x'
             if not won:
                messagebox.showinfo("RESULT","GAME TIED")
                buttons_disabled()


b1=Button(frame,bg=button_color,text=" ",height=3,width=10,command=lambda:trigger(b1))
b2=Button(frame,bg=button_color,height=3,text=" ",width=10,command=lambda:trigger(b2))
b3=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b3))
b4=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b4))
b5=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b5))
b6=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b6))
b7=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b7))
b8=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b8))
b9=Button(frame,bg=button_color,height=3,width=10,text=" ",command=lambda:trigger(b9))
b10=Button(frame,bg=reddish_color,height=3,width=10,text="RESET GAME",command=reset)

b1.grid(row=0,column=0,padx=5,pady=5)
b2.grid(row=0,column=1,padx=5,pady=5)
b3.grid(row=0,column=2,padx=5,pady=5)
b4.grid(row=1,column=0,padx=5,pady=5)
b5.grid(row=1,column=1,padx=5,pady=5)
b6.grid(row=1,column=2,padx=5,pady=5)
b7.grid(row=2,column=0,padx=5,pady=5)
b8.grid(row=2,column=1,padx=5,pady=5)
b9.grid(row=2,column=2,padx=5,pady=5)
b10.grid(row=3,column=0,columnspan=3,padx=0,pady=5)







root.mainloop()
