import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
import os
#------------------------------------------------------------
def last_mounth(title_y_m):
    if int(title_y_m[5:7])==1:
        result=f"{int(title_y_m[0:4])-1}-12"
    else:
        result=f"{title_y_m[0:5]}{int(title_y_m[5:7])-1}"
        if int(title_y_m[5:7])-1<10:
            result=f"{title_y_m[0:5]}0{int(title_y_m[5:7])-1}"
    return result

#open file
global files
date,time=str(datetime.datetime.now()).split()
time=time[0:5]
title_y_m=date[0:7]
last_title_y_m=last_mounth(title_y_m)
nombre_caracteres=-1
try :
    os.mkdir("data")
    print("dossier data a été creé")
except :
    print("dossier data existe")
try :
  
    my_file=open(f"data\{title_y_m}.txt","r+",encoding="utf-8")
    lines=my_file.readlines()
    for line in lines:
        nombre_caracteres+=len(line)+1
    if line:
        line=line.strip().split("|")
        N,somme_actuel,somme_de_sortie,somme_d_entree=int(line[0])+1,int(line[4].split()[0]),abs(int(line[5].split()[0])),int(line[6].split()[0])
    files=[title_y_m]
    while lines[0].strip().split("|")[7]=="resultat du mois dernier" and lines[0].strip().split("|")[1]=="0 DHs":
        files.append(last_mounth(files[len(files)-1]))
        lines=open(f"data\{files[len(files)-1]}.txt","r+",encoding="utf-8").readlines()
    my_file.close()
except :
    try:
        print("start")
        last_file=open(f"data\{last_title_y_m}.txt","r+",encoding="utf-8")
        lines=last_file.readlines()
        somme_dernier_mois=lines[len(last_file.readlines())-1].strip().split("|")[4]
        my_file=open(f"data\{title_y_m}.txt","w+",encoding="utf-8")
        line_1=f"1|0 DHs|{time}|{date}|{somme_dernier_mois}|-0 DHs|+0 DHs|resultat du mois dernier\n"
        my_file.write(line_1)
        my_file.close()
        last_file.close()
        nombre_caracteres+=len(line_1)+1
        N,somme_actuel,somme_de_sortie,somme_d_entree=2,int(somme_dernier_mois.split()[0]),0,0
        files=[title_y_m,last_title_y_m]
        while lines[0].strip().split("|")[7]=="resultat du mois dernier" and lines[0].strip().split("|")[1]=="0 DHs":
            files.append(last_mounth(files[len(files)-1]))
            lines=open(f"data\{files[len(files)-1]}.txt","r+",encoding="utf-8").readlines()
    except:
        my_file=open(f"data\{title_y_m}.txt","w+",encoding="utf-8")
        my_file.close()
        N,somme_actuel,somme_de_sortie,somme_d_entree=1,0,0,0
        files=[title_y_m]   
#define button fonctions
def add_informations():
    global canvas,button_add,button_remove
    canvas.destroy()
    create_background()
    canvas.create_text(375,30,fill="blue",font=("Nordic",30,"italic underline"),text="ajouter des informations")
    button_add=Button(canvas,text="+",fg="black",bg="green",font=("Nordic",20,"bold italic"),width=3,command=add_act)
    button_remove=Button(canvas,text="-",fg="white",bg="red",font=("Nordic",20,"bold italic"),width=3,command=remove_act)
    canvas.create_window(320,100,window=button_remove)
    canvas.create_window(400,100,window=button_add)
    
def create_entrys():
    global canvas,button_add,button_remove,is_positive,entry_activites,text_comment,frame_buttons_aj_inf,button_save,update_bool
    button_add.destroy()
    button_remove.destroy()
    frame_scroll=Frame(canvas)
    scroll=Scrollbar(frame_scroll,orient=VERTICAL)
    if is_positive:
        text_signe="+"
        color="green"
    else:
        text_signe="-"
        color="red"
    entry_activites=Entry(canvas,font=("Nordic",20,"italic"),width=20,border=0,fg=color)
    text_comment=Text(canvas,font=("Nordic",20,"italic"),width=30,border=0,height=10,yscrollcommand=scroll.set)
    scroll.config(command=text_comment.yview)
    scroll.pack(side=RIGHT,fill=Y,ipady=131)
    canvas.create_window(375,170,window=entry_activites)
    canvas.create_text(570,170,fill="black",font=("Nordic",20,"italic"),text="DHs")
    canvas.create_text(180,170,fill=color,font=("Nordic",60,"italic"),text=text_signe)
    canvas.create_text(220,135,fill="brown",font=("Nordic",20,"italic"),text="action : ")
    canvas.create_text(220,220,fill="brown",font=("Nordic",20,"italic"),text="Comment : ")
    canvas.create_window(375,390,window=text_comment)
    canvas.create_window(610,390,window=frame_scroll)

    frame_buttons_aj_inf=Frame(canvas)
    button_save=Button(frame_buttons_aj_inf,text="enregistrer",font=("Nordic",15,"italic bold"),fg="gray",bg="light blue",width=9,command=save_data)
    button_menu=Button(frame_buttons_aj_inf,text="menu",font=("Nordic",15,"italic bold"),fg="gray",bg="light blue",width=9,command=return_to_menu)
    if update_bool:
        button_save.configure(text="modifier",command=save_updating)
        button_return_treeview=Button(frame_buttons_aj_inf,text="return",font=("Nordic",15,"italic bold"),fg="gray",bg="light blue",width=9,command=update_file)
        button_return_treeview.grid(row=0,column=1)
        update_bool=False
    button_save.grid(row=0,column=0)
    button_menu.grid(row=0,column=2)
    canvas.create_window(375,570,window=frame_buttons_aj_inf)

def add_act():
    global is_positive,frame_buttons_aj_inf,button_remove_fr
    is_positive=True
    create_entrys()
    button_remove_fr=Button(frame_buttons_aj_inf,text="-",fg="white",bg="red",font=("Nordic",15,"bold italic"),width=3,command=new_remove_act)
    button_remove_fr.grid(row=0,column=3)
    frame_buttons_aj_inf.update()

def remove_act():
    global is_positive,frame_buttons_aj_inf,button_add_fr
    is_positive=False
    create_entrys()
    button_add_fr=Button(frame_buttons_aj_inf,text="+",fg="black",bg="green",font=("Nordic",15,"bold italic"),width=3,command=new_add_act)
    button_add_fr.grid(row=0,column=3)
    frame_buttons_aj_inf.update()
def return_to_menu():
    global canvas
    canvas.destroy()
    create_menu()
def new_add_act():
    global frame_buttons_aj_inf,is_positive,button_remove_fr,button_add_fr,entry_activites
    is_positive=True
    button_add_fr.destroy()
    canvas.create_text(180,170,fill="#d9c2f0",font=("Nordic",60,"italic"),text="-")
    canvas.create_text(180,170,fill="green",font=("Nordic",60,"italic"),text="+")
    button_remove_fr=Button(frame_buttons_aj_inf,text="-",fg="white",bg="red",font=("Nordic",15,"bold italic"),width=3,command=new_remove_act)
    button_remove_fr.grid(row=0,column=3)
    entry_activites.configure(fg="green")
    frame_buttons_aj_inf.update()
def new_remove_act():
    global frame_buttons_aj_inf,is_positive,button_remove_fr,button_add_fr,entry_activites
    is_positive=False
    button_remove_fr.destroy()
    canvas.create_text(180,170,fill="#d9c2f0",font=("Nordic",60,"italic"),text="+")
    canvas.create_text(180,170,fill="red",font=("Nordic",60,"italic"),text="-")
    button_add_fr=Button(frame_buttons_aj_inf,text="+",fg="black",bg="green",font=("Nordic",15,"bold italic"),width=3,command=new_add_act)
    button_add_fr.grid(row=0,column=3)
    entry_activites.configure(fg="red")
    frame_buttons_aj_inf.update()
def check_entrys():
    global entry_activites,text_comment,frame_messages,somme_actuel,is_positive,action,commentaire
    try:
        frame_messages.destroy()
        frame_messages=Frame(canvas)
    except :
        frame_messages=Frame(canvas)

    value_activitie_is_okey=True
    value_comment_is_okey=True
    try :
        action=int(entry_activites.get())
        if action<=0:
            label_message=Label(frame_messages,text="entrer un nombre strictement positive !!",bg="yellow",fg="red",font=("Nordic",10,"bold"),width=55)
            label_message.pack()
            value_activitie_is_okey=False
        elif action>somme_actuel and not is_positive:
            label_message=Label(frame_messages,text=f"votre solde est négative ({somme_actuel-action} DHs) !!",bg="yellow",fg="red",font=("Nordic",10,"bold"),width=55)
            label_message.pack()
    except :
        label_message=Label(frame_messages,text="entrer un entier positive !!",bg="yellow",fg="red",font=("Nordic",10,"bold"),width=55)
        label_message.pack()
        value_activitie_is_okey=False
    commentaire=" ".join(text_comment.get(1.0,END).strip().split("\n"))
    if len(commentaire)>250 or len(commentaire)<1 :
        label_message=Label(frame_messages,text="votre commentaire doivent étre entre 1 et 250 characteres !!",bg="yellow",fg="red",font=("Nordic",10,"bold"),width=55)
        label_message.pack()
        value_comment_is_okey=False
    arabic_chars=set("دجحخهعغفقثصضشسيبلتانمكطذظزوةىلارؤءئإلإلأأآلآ")
    for char in commentaire:
        if char in arabic_chars:
            value_comment_is_okey=False
            label_message=Label(frame_messages,text="votre commentaire ne doit pas etre en arabe !!",bg="yellow",fg="red",font=("Nordic",10,"bold"),width=55)
            label_message.pack()
            break
    canvas.create_window(375,90,window=frame_messages)
    return value_activitie_is_okey and value_comment_is_okey

def save_data():
    global entry_activites,text_comment,frame_messages,nombre_caracteres,N,somme_actuel,somme_de_sortie,somme_d_entree,is_positive,title_y_m,action
    if check_entrys():
        date,time=str(datetime.datetime.now()).split()
        time=time[0:5]
        if is_positive:
            somme_actuel+=action
            somme_d_entree+=action
            signe="+"
        else:
            somme_actuel-=action
            somme_de_sortie+=action
            signe="-"
        if somme_actuel>0:
            signe_somme="+"
        else:
            signe_somme=""
        to_write=f"{N}|{signe}{action} DHs|{time}|{date}|{signe_somme}{somme_actuel} DHs|-{somme_de_sortie} DHs|+{somme_d_entree} DHs|{commentaire}\n"
        N+=1
        my_file=open(f"data\{title_y_m}.txt","r+",encoding="utf-8")
        my_file.seek(max(0,nombre_caracteres))
        my_file.write(to_write)
        nombre_caracteres+=len(to_write)+1
        print(to_write)
        my_file.close()
        entry_activites.delete(0,END)
        text_comment.delete(1.0,END)
        label_message=Label(frame_messages,text="données enregistreés",bg="green",fg="yellow",font=("Nordic",10,"bold"),width=55)
        label_message.pack()
        solde()
#--------------------------------------------------------------------------------------------------------
def show_list_box_files():
    global canvas,frame_list_files,list_box_files
    frame_list_files=Frame(canvas)
    my_scroll=Scrollbar(frame_list_files,orient=VERTICAL)
    list_box_files=Listbox(frame_list_files,width=40,height=15,font=("Nordic",15,"italic"),selectmode=BROWSE,yscrollcommand=my_scroll.set)
    my_scroll.config(command=list_box_files.yview)
    my_scroll.pack(side=RIGHT,fill=Y)
    list_box_files.pack(side=LEFT)
    for item_file in files:
        list_box_files.insert(0,item_file)
    canvas.create_window(375,320,window=frame_list_files)

def show_historiques():
    global canvas,button_show,button_return_to_menu,files,list_box_files,frame_button_show_return,frame_list_files
    canvas.destroy()
    create_background()
    canvas.create_text(375,30,fill="blue",font=("Nordic",33,"italic underline"),text="afficher les historiques")
    show_list_box_files()
    canvas.create_text(360,110,fill="brown",font=("Nordic",20,"italic"),text="selectionner le mois d'historiques :")
    frame_button_show_return=Frame(canvas)
    button_show=Button(frame_button_show_return,fg="gray",bg="light blue",font=("Nordic",20,"bold italic"),text="ouvrir",command=open_file)
    button_return_to_menu=Button(frame_button_show_return,fg="gray",bg="light blue",font=("Nordic",20,"bold italic"),text="menu",command=return_to_menu)
    button_show.grid(column=0,row=0)
    button_return_to_menu.grid(column=1,row=0)
    canvas.create_window(360,550,window=frame_button_show_return)
def show_treeviews(lines):
        global table
        frame_treeview=Frame(canvas)
        frame_treeview2=Frame(frame_treeview)
        scroll=Scrollbar(frame_treeview2,orient=VERTICAL)
        scroll2=Scrollbar(frame_treeview,orient=HORIZONTAL)
        style=ttk.Style()
        table=ttk.Treeview(frame_treeview2,height=25,columns=(1,2,3,4,5,6,7),yscrollcommand=scroll.set,xscrollcommand=scroll2.set)
        scroll.config(command=table.yview)
        scroll2.config(command=table.xview)
        table.column("#0",anchor=CENTER,width=50,minwidth=50)
        table.column(1,anchor=CENTER,width=215,minwidth=215)
        table.column(2,anchor=CENTER,width=65,minwidth=65)
        table.column(3,anchor=CENTER,width=85,minwidth=85)
        table.column(4,anchor=CENTER,width=400,minwidth=400)
        table.column(5,anchor=CENTER,width=215,minwidth=215)
        table.column(6,anchor=CENTER,width=215,minwidth=215)
        table.column(7,anchor=CENTER,width=340,minwidth=340)
        table.heading("#0",text="N°",anchor=CENTER)
        table.heading(1,text="Action",anchor=CENTER)
        table.heading(2,text="Heure",anchor=CENTER)
        table.heading(3,text="Date",anchor=CENTER)
        table.heading(4,text="Solde",anchor=CENTER)
        table.heading(5,text="Somme de sorties",anchor=CENTER)
        table.heading(6,text="Somme d'entrées",anchor=CENTER)
        table.heading(7,text="Commentaire",anchor=CENTER)
        table.pack(side=LEFT,fill=Y)
        scroll.pack(side=RIGHT,fill=Y)
        frame_treeview2.pack()
        scroll2.pack(fill=X)
        canvas.create_window(800,360,window=frame_treeview)
        id=0
        style.theme_use("default")
        style.configure("Treeview",font=("Nordic",11,"italic bold"),fieldbackground="#D3D3D3")
        style.configure("Treeview.Heading",font=("Nordic",15,"italic "))
    #stretch
        table.tag_configure("pair",background="light blue")
        table.tag_configure("impair",background="white")
        style.map("Treeview",background=[("selected","gray")])
        for line in lines:
            line=line.strip().split("|")
            table.insert("",iid=id,index=END,text=line[0],values=line[1:],tags=(["pair","impair"][id%2],))
            id+=1
        
def open_file():
    global canvas,frame_list_files
    title_file=list_box_files.get(ANCHOR)
    if not title_file:
        label_message_sh=Label(canvas,fg="red",bg="yellow",font=("Nordic",15,"bold italic"),text="selectionner un mois !!",width=30)
        canvas.create_window(375,80,window=label_message_sh)
        return 
    canvas.destroy()
    create_background(x=500)
    window.geometry(("1610x720"))
    canvas.create_text(805,30,fill="blue",font=("Nordic",33,"italic underline"),text=f"historiques : {title_file}")
    frame_buttons_table=Frame(canvas)
    button_return=Button(frame_buttons_table,fg="gray",bg="light blue",font=("Nordic",20,"bold italic"),text="Return",command=show_historiques)
    button_menu=Button(frame_buttons_table,fg="gray",bg="light blue",font=("Nordic",20,"bold italic"),text="menu",command=return_to_menu)
    button_return.grid(row=0,column=0)
    button_menu.grid(row=0,column=1)
    canvas.create_window(805,680,window=frame_buttons_table)
    my_file=open(f"data\{title_file}.txt","r",encoding="utf-8")
    lines=my_file.readlines()
    my_file.close()
    show_treeviews(lines)
#-------------------------------------------------------------------------------------------------------
def update_file():
    global canvas
    canvas.destroy()
    create_background(x=500)
    window.geometry("1610x720")
    canvas.create_text(805,30,fill="blue",font=("Nordic",33,"italic underline"),text=f"modifier l'historiques")
    show_treeviews(open(f"data\{title_y_m}.txt","r+",encoding="utf-8").readlines())
    frame_buttons=Frame(canvas)
    button_update=Button(frame_buttons,bg="light blue",fg="gray",font=("Nordic",20,"italic bold"),text="modifier",command=update_line)
    button_delete=Button(frame_buttons,bg="light blue",fg="gray",font=("Nordic",20,"italic bold"),text="supprimer",command=delete_line)
    button_return_menu=Button(frame_buttons,bg="light blue",fg="gray",font=("Nordic",20,"italic bold"),text="menu",width=6,command=return_to_menu)
    button_update.grid(row=0,column=0)
    button_delete.grid(row=0,column=1)
    button_return_menu.grid(row=0,column=2)
    canvas.create_window(805,680,window=frame_buttons)
global update_bool
update_bool=False
def update_line():
    global canvas,label_message,update_bool,item
    item=table.focus()
    try:
        label_message.destroy()
        label_message=Label(canvas,font=("Nordic",15,"italic bold"),fg="red",bg="yellow")
    except:
        label_message=Label(canvas,font=("Nordic",15,"italic bold"),fg="red",bg="yellow")
    if item in table.selection() and len(table.selection())==1:
        item=int(item)
    elif not item or item not in table.selection() or len(table.selection())>1:
        label_message.configure(text="selectioner une ligne !!")
        canvas.create_window(805,70,window=label_message)
        return
    selected=table.item(item,"values")
    if item==0 and selected[6]=="resultat du mois dernier"and selected[0]=="0 DHs":
        label_message.configure(text="ne selectionnez pas cette ligne !!")
        canvas.create_window(805,70,window=label_message)
        return
    add_informations()
    label_cache=Label(canvas,bg="#d9c2f0",width=750,fg="blue",font=("Nordic",30,"italic underline"),text=f"modifier la ligne {item+1}")
    canvas.create_window(375,30,window=label_cache)
    update_bool=True

    
def recalcule(lines,item,solde,somme_de_sortie,somme_d_entree):
    global nombre_caracteres,somme_actuel
    for index in range(item+1,len(lines)):
        if not lines[index]:
            continue
        line=lines[index].split("|")
        action=int(line[1].split()[0])
        solde+=action
        if action>0:
            somme_d_entree+=action
        else:
            somme_de_sortie+=action
        if solde>0:
            signe="+"
        else:
            signe=""
        line[0],line[4],line[5],line[6]=f"{index+1}",f"{signe}{solde} DHs",f"-{abs(somme_de_sortie)} DHs",f"+{somme_d_entree} DHs"
        lines[index]="|".join(line)
        somme_actuel=solde

def save_updating():
    global item,action,commentaire,title_y_m,nombre_caracteres,is_positive,somme_actuel,label_message
    file_to_update=open(f"data\{title_y_m}.txt","r+",encoding="utf-8")
    lines=file_to_update.readlines()
    nombre_caracteres-=len(lines[item])
    line=lines[item].strip().split("|")
    somme_actuel=int(line[4].split()[0])-int(line[1].split()[0])
    file_to_update.close()
    if not check_entrys():
        return
    file_to_update=open(f"data\{title_y_m}.txt","w+",encoding="utf-8")
    if int(line[1].split()[0])>0:
        somme_d_entree,somme_de_sortie=int(line[6].split()[0])-int(line[1].split()[0]),int(line[5].split()[0])
    else:
        somme_d_entree,somme_de_sortie=int(line[6].split()[0]),int(line[5].split()[0])-int(line[1].split()[0])
    if is_positive:
        signe="+"
        somme_actuel+=action
        somme_d_entree+=action
    else:
        signe="-"
        somme_actuel-=action
        somme_de_sortie-=action
    if somme_actuel>0:
        signe_somme="+"
    else:
        signe_somme=""
    line[1],line[4],line[5],line[6],line[7]=f"{signe}{action} DHs",f"{signe_somme}{somme_actuel} DHs",f"-{abs(somme_de_sortie)} DHs",f"+{somme_d_entree} DHs",f"{commentaire}\n"
    lines[item]="|".join(line)
    nombre_caracteres=-1
    recalcule(lines,item,somme_actuel,somme_de_sortie,somme_d_entree)
    file_to_update.seek(0)
    for line in lines:
        file_to_update.write(line)
        nombre_caracteres+=len(line)+1
    file_to_update.close()
    update_file()
    label_message=Label(canvas,text="votre modifications est enregistrés",bg="green",fg="yellow",font=("Nordic",10,"bold"),width=55)
    canvas.create_window(805,70,window=label_message)
def delete_line():
    global canvas,label_message,update_bool,item,somme_actuel,nombre_caracteres,label_message
    item=table.focus()
    try:
        label_message.destroy()
        label_message=Label(canvas,font=("Nordic",15,"italic bold"),fg="red",bg="yellow")
    except:
        label_message=Label(canvas,font=("Nordic",15,"italic bold"),fg="red",bg="yellow")
    if item in table.selection() and len(table.selection())==1:
        item=int(item)
    elif not item or item not in table.selection() or len(table.selection())>1:
        label_message.configure(text="selectioner une ligne !!")
        canvas.create_window(805,70,window=label_message)
        return
    selected=table.item(item,"values")
    if item==0 and selected[6]=="resultat du mois dernier"and selected[0]=="0 DHs":
        label_message.configure(text="ne selectionnez pas cette ligne !!")
        canvas.create_window(805,70,window=label_message)
        return
    file_to_update=open(f"data\{title_y_m}.txt","r+",encoding="utf-8")
    lines=file_to_update.readlines()
    nombre_caracteres-=len(lines.pop(item))
    if item>0:
        line=lines[item-1].strip().split("|")
        somme_actuel,somme_de_sortie,somme_d_entree=int(line[4].split()[0]),int(line[5].split()[0]),int(line[6].split()[0])
    else:
        somme_actuel,somme_de_sortie,somme_d_entree=0,0,0
    
    recalcule(lines,item-1,somme_actuel,somme_de_sortie,somme_d_entree)
    file_to_update.close()
    file_to_update=open(f"data\{title_y_m}.txt","w+",encoding="utf-8")
    for line in lines:
        file_to_update.write(line)
    file_to_update.close()
    update_file()
    label_message=Label(canvas,text=f"line {item+1} est supprimée",bg="green",fg="yellow",font=("Nordic",10,"bold"),width=55)
    canvas.create_window(805,70,window=label_message)
    solde()
    
#------------------------------------------------------------------------------------------------------
#create window
window=Tk()
window.geometry(("750x720"))
window.resizable(False,False)
window.config(background="#d9c2f0")
window.title("calculateur d'argents")
window.iconbitmap("images\icon.ico")
#define image 
bg=PhotoImage(file="images\Background.png")
def create_background(bg=PhotoImage(file="images\Background.png"),x=0):
    global canvas,somme_actuel
    window.geometry("750x720")
    canvas=Canvas(window,width=1610,height=720,bg="#d9c2f0",border=0)
    canvas.create_image(x,-200,image=bg,anchor="nw")
    canvas.pack()
    solde()
def solde():
    global frame_solde
    try:
        frame_solde.destroy()
    except:
        print("solde est affiché")
    frame_solde=Frame(canvas)
    label_solde=Label(frame_solde,fg="brown",bg="#d9c2f0",font=("Nordic",15,"italic underline"),text="Solde :")
    if somme_actuel==0:
        color="light blue"
        text_solde=f"0 DHs"
    elif somme_actuel>0:
        color="green"
        text_solde=f"+{somme_actuel} DHs"
    else:
        color="red"
        text_solde=f"{somme_actuel} DHS"
    label_result=Label(frame_solde,bg=color,font=("Nordic",15,"italic"),text=text_solde)
    label_result.grid(column=1,row=0)
    label_solde.grid(column=0,row=0)
    canvas.create_window(75+len(text_solde)*5,700,window=frame_solde)
def create_menu(x=150,y=100,bg=PhotoImage(file="images\Background.png")):
    global canvas
#create background
    create_background(bg)
#create texte
    canvas.create_text(x+225,y,fill="#d9ffc2",font=("Nordic",30),text="Calculateur d'argents")
#create cadre
    canvas.create_line(x+40,y,x,y,width=2,fill="yellow")
    canvas.create_line(x+450,y,x+410,y,width=2,fill="yellow")
    canvas.create_line(x,y,x,y+190,width=2,fill="yellow")
    canvas.create_line(x,y+190,x+450,y+190,width=2,fill="yellow")
    canvas.create_line(x+450,y+190,x+450,y,width=2,fill="yellow")
#create buttons 
    button_add_informations=Button(canvas,text="ajouter des informations",font=("Nordic",15),fg="gray",bg="light blue" , width=30,command=add_informations)
    button_show_historiques=Button(canvas,text="afficher les historiques",font=("Nordic",15),fg="gray",bg="light blue",width=30,command=show_historiques)
    button_send_it_to_my_email=Button(canvas,text="modifier une ligne",font=("Nordic",15),fg="gray",bg="light blue",width=30,command=update_file)
    canvas.create_window(x+225,y+50,window=button_add_informations)
    canvas.create_window(x+225,y+100,window=button_show_historiques)
    canvas.create_window(x+225,y+150,window=button_send_it_to_my_email)
    canvas.update()
create_menu()
window.mainloop()