from tkinter import *
#fonction pour calculer x
def x(a:float,b:float)->float:
    if a <=0 or b<=0:
        return -1
    return int((a**2-b**2)/2/b*10**2)/10**2
#-----------------------------------------------------------------------------------
def create_canvas_image(bg:PhotoImage,a=None,b=None,x=None):
    canvas_image=Canvas(canvas,width=650,height=720,bg="white")
    canvas_image.create_image(-50,100,image=bg,anchor="nw")
    canvas_image.create_text(90,40,text="Un dessin approximatif",font=("Nordic",30,"italic bold underline"),fill="green",anchor="nw")
    canvas_image.create_text(50,560,fill="black",font=("Nordic",25,"italic "),text="(OK)⊥(AB)",anchor="nw")
    canvas_image.create_text(50, 600, fill="#004499", font=("Nordic",30,"italic "), text="o:",anchor="nw")
    canvas_image.create_text(90, 600, fill="black", font=("Nordic",30,"italic "), text="centre du cercle.",anchor="nw")
    canvas_image.create_text(50, 650, fill="#004499", font=("Nordic",30,"italic "), text="I:",anchor="nw")
    canvas_image.create_text(90, 650, fill="black", font=("Nordic",30,"italic "), text="milieu du AB.",anchor="nw")
    if a and b and x:
        canvas_image.create_text(190,275,fill="black",font=("Nordic",20,"italic"),anchor="nw",text=f"={a}m")
        canvas_image.create_text(360,210,fill="black",font=("Nordic",20,"italic"),anchor="nw",text=f"={b}m")
        canvas_image.create_text(360,390,fill="red",font=("Nordic",20,"italic"),anchor="nw",text=f"={x}m")
    canvas.create_window(0,0,window=canvas_image,anchor="nw")
def create_form(logo:PhotoImage):
    global entry_a,entry_b,canvas_entries
    canvas_entries=Canvas(window,width=430,height=730)
    canvas_entries.create_image(0,0,image=logo,anchor="nw")
    canvas_entries.create_text(200,65,text="les mésures en m",font=("nordic",30,"underline bold italic"),fill="blue")
    frame_a=Frame(canvas_entries)
    label_a=Label(frame_a,text="a :",font=("Nordic",20,"italic"))
    entry_a=Entry(frame_a,font=("Nordic",20,"italic"),width=10,border=0)
    label_unite_a=Label(frame_a,text="m",font=("Nordic",20,"italic"))
    label_a.grid(column=0,row=0)
    entry_a.grid(column=1,row=0)
    label_unite_a.grid(column=2,row=0)
    canvas_entries.create_window(100,200,window=frame_a,anchor="nw")
    frame_b=Frame(canvas_entries)
    label_b=Label(frame_b,text="b :",font=("Nordic",20,"italic"))
    entry_b=Entry(frame_b,font=("Nordic",20,"italic"),width=10,border=0)
    label_unite_b=Label(frame_b,text="m",font=("Nordic",20,"italic"))
    label_b.grid(column=0,row=0)
    entry_b.grid(column=1,row=0)
    label_unite_b.grid(column=2,row=0)
    canvas_entries.create_window(100,250,window=frame_b,anchor="nw")
    button_entrer=Button(canvas_entries,text="entrer",font=("Nordic",15,"italic"),bg="gray",fg="light blue",width=18,command=entrer)
    canvas_entries.create_window(100,300,window=button_entrer,anchor="nw")
    canvas.create_window(650,-10,window=canvas_entries,anchor="nw")
    entry_a.bind("<Button-1>",delete_a)
    entry_b.bind("<Button-1>",delete_b)
def create_all():
    global logo,bg
    bg=PhotoImage(file="images/bg.png")
    logo=PhotoImage(file="images/logo.png").zoom(4).subsample(3)
    create_canvas_image(bg)
    create_form(logo)

def entrer(*args):
    global number_click,label_message,erreur,bg,result,label_result
    create_canvas_image(bg)
    if erreur:
        label_message.destroy()
        erreur=False
    if result:
        label_result.destroy()

    number_click=[0,0]
    a=entry_a.get()
    b=entry_b.get()
    if not a or not b:
        erreur=TRUE
        label_message=Label(canvas_entries,font=("Nordic",20,"italic"),text="veuillez entrer les mesures !!",fg="red",bg="yellow",border=1)
        canvas_entries.create_window(215,130,window=label_message)
        return
    try:
        a=float(a)
        b=float(b)
        valeur_x=x(a,b)
    except:
        erreur=TRUE
        label_message=Label(canvas_entries,font=("Nordic",20,"italic"),fg="red",bg="yellow",border=1,text="entrer des nombres (1,2,3,...)!!")
        canvas_entries.create_window(215,130,window=label_message)
        return

    if valeur_x<0:
        erreur=TRUE
        label_message=Label(canvas_entries,font=("Nordic",20,"italic"),fg="red",bg="yellow",border=1,text="les mesures sont invalides !!")
        canvas_entries.create_window(215,130,window=label_message)
        return
    create_canvas_image(bg,a,b,valeur_x)
    label_result=Label(canvas_entries,font=("Nordic",30,"italic underline"),bg="yellow",fg="blue",text=f"x={valeur_x}m")
    canvas_entries.create_window(215,400,window=label_result)
    result=True

def delete_a(*args):
    global number_click
    if number_click[0]==0:
        entry_a.delete(0,END)
    number_click[0]+=1
def delete_b(*args):
    global number_click
    if number_click[1]==0:
        entry_b.delete(0,END)
    number_click[1]+=1
#-----------------------------------------------------------------------------------
window=Tk()
window.title("consmou")
window.iconbitmap("images/logo.ico")
window.geometry("1080x720")
window.resizable(False,False)
canvas=Canvas(window,width=1080,height=720)
create_all()
canvas.pack()
window.bind("<Return>",entrer)
number_click=[0,0]
erreur=False
result=False
window.mainloop()