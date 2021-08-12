from tkinter import *
cellules_vivantes=[]
nombre_cellule_vivante=0
click_canon=bool
#fonction------------------------------------------
def rendre_cette_cellule_vivante():
    global coordonnes,num_carre,nombre_cellule_vivante,button_s,button_t,cellules_vivantes,label_message,button_f,button_c
    x,y=(entry_x.get()),(entry_y.get())
    if not x or not y :
        label_message=Label(frame_message,text="entrer les coordonnes d'une cellule",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    nums=list(map(str,range(1,num_carre)))
    if x not in nums or y not in nums:
        label_message=Label(frame_message,text="entrer les coordonnes d'une cellule dans le plan ",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    x,y=int(x)-1,int(y)-1
    if coordonnes[y][x][1]=="red":
        label_message=Label(frame_message,text="cette cellule est déja vivante",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    label_message=Label(frame_message,bg="#99aab5")
    label_message.grid(column=0,row=0,ipadx=130)
    change_color("red",x,y)
    cellules_vivantes.append((x,y))
    entry_x.delete(0,END)
    entry_y.delete(0,END)
    if nombre_cellule_vivante==1:
        button_t=Button(frame_buttons,text="tuer cette cellule",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_cette_cellule)
        button_t.pack()
        button_f=Button(frame_buttons,text="tuer toutes les cellules",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_toutes_les_cellules)
        button_f.pack()
        button_s=Button(frame_buttons,text="commencer le development",width=24,font=("courrier",10),bg="red",fg="black",command=commencer_le_developement)
        button_s.pack()

def tuer_cette_cellule():
    global coordonnes,num_carre,nombre_cellule_vivante,label_message
    x,y=(entry_x.get()),(entry_y.get())
    if not x or not y :
        label_message=Label(frame_message,text="entrer les coordonnes d'une cellule vivante",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    nums=list(map(str,range(1,num_carre)))
    if x not in nums or y not in nums:
        label_message=Label(frame_message,text="entrer les coordonnes d'une cellule dans le plan ",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    x,y=int(x)-1,int(y)-1
    if coordonnes[y][x][1]=="white":
        label_message=Label(frame_message,text="cette cellule n'est pas vivante",fg="red",bg="yellow",width=36)
        label_message.grid(column=0,row=0)
        return
    label_message=Label(frame_message,bg="#99aab5")
    label_message.grid(column=0,row=0,ipadx=130)
    change_color("white",x,y)
    cellules_vivantes.remove((x,y))
    entry_x.delete(0,END)
    entry_y.delete(0,END)
    if nombre_cellule_vivante==0:
        button_t.destroy()
        button_f.destroy()
        button_s.destroy()
def tuer_toutes_les_cellules():
    global nombre_cellule_vivante,cellules_vivantes,button_c,button_s,button_t,nombre_cellule_vivante
    for cellule in cellules_vivantes:
        change_color("white",cellule[0], cellule[1])
    cellules_vivantes=[]
    nombre_cellule_vivante=0
    button_t.destroy()
    button_s.destroy()
    button_f.destroy()
    if click_canon:
        button_c=Button(frame_buttons,text="canon à planeur",width=24,font=("courrier",10),bg="yellow",fg="green",command=canon_à_planeur)
        button_c.pack()
def nombre_voisins(x,y):
   global coordonnes
   result=0
   directions=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
   for sens in directions:
       new_x,new_y=x+sens[0],y+sens[1]
       if new_x >=0 and new_x<=38 and new_y >=0 and new_y <=38 and coordonnes[new_y][new_x][1]=="red":
           result+=1
   return result
def list_cellules_suiver(cellules_vivantes:list)->list:
    directions=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    cellules_suiver=[]
    for cellule_vivante in cellules_vivantes:
        if cellule_vivante not in cellules_suiver:
            cellules_suiver.append(cellule_vivante)
        for mov in directions:
            new_x,new_y=cellule_vivante[0]+mov[0],cellule_vivante[1]+mov[1]
            if new_x >=0 and new_x<=38 and new_y>=0 and new_y<=38 and (new_x,new_y)not in cellules_suiver:
                cellules_suiver.append((new_x,new_y))
    cellules_suiver.sort()
    return cellules_suiver
def change_color(color,x,y,canon=False):
    global nombre_cellule_vivante,coordonnes,cellules_vivantes
    if color=="white":
        nombre_cellule_vivante-=1
    else:
        nombre_cellule_vivante+=1
    coordonnes[y][x][1]=color
    if (x,y) not in cellules_vivantes and canon:
        cellules_vivantes.append((x,y))
    cellule=coordonnes[y][x][0]
    canvas.create_rectangle(cellule[0],cellule[1],cellule[2],cellule[3],fill=color)
def cellules_qui_va_changer(cellules_suiver:list)->list:
    global nombre_cellule_vivante,cellules_vivantes
    result=[]
    for cellule in cellules_suiver:
        if coordonnes[cellule[1]][cellule[0]][1]=="white" and nombre_voisins(cellule[0], cellule[1])==3:
            result.append((cellule[0],cellule[1],"red"))
            cellules_vivantes.append(cellule)
        elif coordonnes[cellule[1]][cellule[0]][1]=="red" and nombre_voisins(cellule[0], cellule[1]) not in [2,3]:
            result.append((cellule[0],cellule[1],"white"))
            cellules_vivantes.remove(cellule)
    for changement in result:
        coordonnes[changement[1]][changement[0]][1]=changement[2]
    return result
def stop():
    global button_l,button_s,button_t,program_run,button_c,button_f,click_canon
    program_run=False
    button_stop.destroy()
    button_l=Button(frame_buttons,text="rendre cette cellule vivante",width=24,font=("courrier",10),bg="yellow",fg="green",command=rendre_cette_cellule_vivante)
    button_l.pack()
    button_c=Button(frame_buttons,text="canon à planeur",width=24,font=("courrier",10),bg="yellow",fg="green",command=canon_à_planeur)
    button_c.pack()
    click_canon=False
    if nombre_cellule_vivante==0:
        return
    button_t=Button(frame_buttons,text="tuer cette cellule",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_cette_cellule)
    button_t.pack()
    button_f=Button(frame_buttons,text="tuer toutes les cellules",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_toutes_les_cellules)
    button_f.pack()
    button_s=Button(frame_buttons,text="commencer le development",width=24,font=("courrier",10),bg="red",fg="black",command=commencer_le_developement)
    button_s.pack()
def commencer_le_developement():
    global button_stop,program_run,label_message,button_c,button_f
    nombre_changements=0
    program_run=True
    button_l.destroy()
    button_f.destroy()
    button_c.destroy()
    button_s.destroy()
    button_t.destroy()
    button_stop=Button(frame_buttons,text="stop",width=24,font=("courrier",10),bg="blue",fg="white",command=stop)
    button_stop.pack()
    label_message=Label(frame_message,bg="#99aab5")
    label_message.grid(column=0,row=0,ipadx=130)
    while program_run:
        changements=cellules_qui_va_changer(list_cellules_suiver(cellules_vivantes))
        if not changements:
            stop()
            return
        nombre_changements+=1
        label_commentaire_1=Label(frame_message,text=f"nombre du changements : {nombre_changements}",fg="red",bg="yellow",width=36)
        label_commentaire_1.grid(column=0,row=1)
        label_commentaire_2=Label(frame_message,text=f"nombre du cellules vivantes : {nombre_cellule_vivante}",fg="red",bg="yellow",width=36)
        label_commentaire_2.grid(column=0,row=2)
        if nombre_changements==1:
            print("**********************************************************")
        print("changement : ",nombre_changements)
        for changement in changements:
            print("  ",changement)
            change_color(changement[2],changement[0],changement[1])
            window.update()
        print("-----------------------------")
        label_commentaire_2=Label(frame_message,text=f"nombre du cellules vivantes : {nombre_cellule_vivante}",fg="red",bg="yellow",width=36)
        label_commentaire_2.grid(column=0,row=2)
def canon_à_planeur():
    global button_t,button_s,label_message,nombre_cellule_vivante,button_f,click_canon
    click_canon=True
    if nombre_cellule_vivante==0:
        label_message=Label(frame_message,bg="#99aab5")
        label_message.grid(column=0,row=0,ipadx=130)
        button_t=Button(frame_buttons,text="tuer cette cellule",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_cette_cellule)
        button_t.pack()
        button_f=Button(frame_buttons,text="tuer toutes les cellules",width=24,font=("courrier",10),bg="black",fg="white",command=tuer_toutes_les_cellules)
        button_f.pack()
        button_s=Button(frame_buttons,text="commencer le development",width=24,font=("courrier",10),bg="red",fg="black",command=commencer_le_developement)
        button_s.pack()
    change_color("red",1,5,True)
    change_color("red",1,6,True)
    change_color("red",2,5,True)
    change_color("red",2,6,True)
    change_color("red",11,5,True)
    change_color("red",11,6,True)
    change_color("red",11,7,True)
    change_color("red",12,4,True)
    change_color("red",12,8,True)
    change_color("red",13,3,True)
    change_color("red",13,9,True)
    change_color("red",14,3,True)
    change_color("red",14,9,True)
    change_color("red",15,6,True)
    change_color("red",16,4,True)
    change_color("red",16,8,True)
    change_color("red",17,5,True)
    change_color("red",17,6,True)
    change_color("red",17,7,True)
    change_color("red",18,6,True)
    change_color("red",21,3,True)
    change_color("red",21,4,True)
    change_color("red",21,5,True)
    change_color("red",22,3,True)
    change_color("red",22,4,True)
    change_color("red",22,5,True)
    change_color("red",23,2,True)
    change_color("red",23,6,True)
    change_color("red",25,1,True)
    change_color("red",25,2,True)
    change_color("red",25,6,True)
    change_color("red",25,7,True)
    change_color("red",35,3,True)
    change_color("red",35,4,True)
    change_color("red",36,3,True)
    change_color("red",36,4,True)
    button_c.destroy()
#--------------------------------------------------
window=Tk()

width_w,height_w,num_carre=1080,725,40
window.title("le jeu de la vie")
window.geometry(f"{width_w}x{height_w}")
window.resizable(False,False)
window.config(background="#99aab5")
window.iconbitmap("logo.ico")
height_c=height_w//num_carre*num_carre
coordonnes=[]
i=0
frame=Frame(window)
canvas=Canvas(frame,width=height_c, height=height_c,bg="white")
#tracer un plan
for y in range(0,height_c,int(height_c/num_carre)):
    row=[]
    for x in range(0,height_c,int(height_c/num_carre)):
        canvas.create_rectangle(x,y,x+int(height_c/num_carre),y+int(height_c/num_carre),fill="white")
        if y==0:
          canvas.create_text(x+int(height_c/(num_carre*2)),y+int(height_c/(num_carre*2)),text=int(x/(height_c/num_carre)))
        elif x==0:
          canvas.create_text(x+int(height_c/(num_carre*2)),y+int(height_c/(num_carre*2)),text=int(y/(height_c/num_carre)))
        else:
            row.append([(x,y,x+int(height_c/num_carre),y+int(height_c/num_carre)),"white"])
    if row:
      coordonnes.append(row)
canvas.pack()
frame.pack(side=LEFT)
#tracer les parametre
right_frame=Frame(window,bg="#99aab5")
#image---------------------------------------
images=PhotoImage(file="le jeu de la vie.png")
canvas_image=Canvas(right_frame,width=300,height=300,bg="yellow",bd=0,highlightthickness=0)
canvas_image.create_image(150,150,image=images)
canvas_image.pack()
#form----------------------------------------
frame_form=Frame(right_frame,bg="#99aab5")
frame_input=Frame(frame_form, bg="#99aab5")
#---------------------------------------------
frame_x=Frame(frame_input,bg="#99aab5")
label_x=Label(frame_x,text="x :")
entry_x=Entry(frame_x,bg="white",fg="black",font=("courrier",10),width=10)
label_x.grid(column=0,row=0,sticky=W)
entry_x.grid(column=1, row=0,sticky=W)
frame_x.grid(row=0,column=0,sticky=W)
frame_y=Frame(frame_input,bg="#99aab5")
label_y=Label(frame_y,text="y :")
entry_y=Entry(frame_y,bg="white",fg="black",font=("courrier",10),width=10)
label_y.grid(column=0,row=0,sticky=W)
entry_y.grid(column=1, row=0,sticky=W)
frame_y.grid(row=0,column=1,sticky=W,padx=10)
#---------------------------------------------
frame_input.pack(fill=X,padx=80,pady=5)
frame_buttons=Frame(frame_form, bg="#99aab5")
#--------------------------------------------
button_l=Button(frame_buttons,text="rendre cette cellule vivante",width=24,font=("courrier",10),bg="yellow",fg="green",command=rendre_cette_cellule_vivante)
button_l.pack()
button_c=Button(frame_buttons,text="canon à planeur",width=24,font=("courrier",10),bg="yellow",fg="green",command=canon_à_planeur)
button_c.pack()
click_canon=False
#-------------------------------------------
frame_buttons.pack(fill=X)
frame_form.pack(ipadx=width_w-height_c,pady=30)
#message--------------------------------------
frame_message=Frame(right_frame,bg="#99aab5")
frame_message.pack()
#------------------------------------------
right_frame.pack(side=LEFT,ipady=height_w,ipadx=width_w-height_w)    

window.mainloop()