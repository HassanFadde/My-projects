from tkinter import *
import time
dict_colors={"white":"red","red":"white"}
program_run=False
#fonctions-------------------------------------------------
def change_color(x,y):
    global coordonnes,dict_colors,fourmi_x,fourmi_y
    coordonnes[y][x][1],cellule=dict_colors[coordonnes[y][x][1]],coordonnes[y][x][0]
    canvas.create_rectangle(cellule[0],cellule[1],cellule[0]+taille,cellule[1]+taille,fill=coordonnes[y][x][1])
    if fourmi_x==cellule[0]and fourmi_y==cellule[1]:
        canvas.create_polygon([fourmi_x+taille//2,fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+taille,fourmi_x+taille//2,fourmi_y])
def click_gauche(event):
   global taille,program_run
   if program_run: 
       return
   x,y=(event.x-(event.x%taille))//taille,(event.y-(event.y%taille))//taille
   change_color(x,y)
def click_droite(event):
    global coordonnes,direction,taille,fourmi_x,fourmi_y,program_run
    if program_run:
        return
    x,y=(event.x-(event.x%taille)),(event.y-(event.y%taille))
    canvas.create_rectangle(fourmi_x,fourmi_y,fourmi_x+taille,fourmi_y+taille,fill=coordonnes[fourmi_y//taille][fourmi_x//taille][1])
    fourmi_x=x
    fourmi_y=y
    direction="haut"
    canvas.create_polygon([fourmi_x+taille//2,fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+taille,fourmi_x+taille//2,fourmi_y])
def tourne_droite():
    global fourmi_x,fourmi_y,direction,taille,coordonnes
    canvas.create_rectangle(fourmi_x,fourmi_y,fourmi_x+taille,fourmi_y+taille,fill=coordonnes[fourmi_y//taille][fourmi_x//taille][1])
    if direction=="haut":
        direction="droite"
        fourmi_x+=taille
        canvas.create_polygon([fourmi_x,fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+(taille//2),fourmi_x,fourmi_y])
    elif direction == "droite":
        direction="bas"
        fourmi_y+=taille
        canvas.create_polygon([fourmi_x,fourmi_y,fourmi_x+taille,fourmi_y,fourmi_x+(taille//2),fourmi_y+taille,fourmi_x,fourmi_y])
    elif direction == "bas":
        direction="gauche"
        fourmi_x-=taille
        canvas.create_polygon([fourmi_x,fourmi_y+(taille//2),fourmi_x+taille,fourmi_y,fourmi_x+taille,fourmi_y+taille,fourmi_x,fourmi_y+(taille//2)])
    elif direction == "gauche":
        direction="haut"
        fourmi_y-=taille
        canvas.create_polygon([fourmi_x+(taille//2),fourmi_y,fourmi_x+taille,fourmi_y+taille,fourmi_x,fourmi_y+taille,fourmi_x+(taille//2),fourmi_y])
def tourne_gauche():
    global fourmi_x,fourmi_y,direction,taille,coordonnes
    canvas.create_rectangle(fourmi_x,fourmi_y,fourmi_x+taille,fourmi_y+taille,fill=coordonnes[fourmi_y//taille][fourmi_x//taille][1])    
    if direction == "haut":
        direction="gauche"
        fourmi_x-=taille
        canvas.create_polygon([fourmi_x,fourmi_y+(taille//2),fourmi_x+taille,fourmi_y,fourmi_x+taille,fourmi_y+taille,fourmi_x,fourmi_y+(taille//2)])
    elif direction == "gauche":
        direction="bas"
        fourmi_y+=taille
        canvas.create_polygon([fourmi_x,fourmi_y,fourmi_x+taille,fourmi_y,fourmi_x+(taille//2),fourmi_y+taille,fourmi_x,fourmi_y])
    elif direction == "bas":
        direction="droite"
        fourmi_x+=taille
        canvas.create_polygon([fourmi_x,fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+(taille//2),fourmi_x,fourmi_y])
    elif direction == "droite":
        direction="haut"
        fourmi_y-=taille
        canvas.create_polygon([fourmi_x+(taille//2),fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+taille,fourmi_x+(taille//2),fourmi_y])
def stop(event):
    global program_run
    program_run=False
def commencer_la_simulation(event):
    global coordonnes,fourmi_x,fourmi_y,button_start,button_end,label_nombre_tours,program_run,width,height
    program_run=True
    label=Label(frame_form)
    label.grid(row=0,column=0,ipadx=100,ipady=4)
    nombre_tours=0
    while fourmi_x in range(0,width-taille) and fourmi_y  in range(0,height-taille) and program_run:
        nombre_tours+=1
        change_color(fourmi_x//taille,fourmi_y//taille)
        if coordonnes[fourmi_y//taille][fourmi_x//taille][1]=="white":
            tourne_gauche()
        else:
            tourne_droite()
        label_nombre_tours=Label(frame_form,text=f"nombre du tours {nombre_tours}",font=("courrier",20),bg="yellow",fg="green",width=24)
        label_nombre_tours.grid(row=0,column=0)
        canvas.update()
        #time.sleep(0.2)
    program_run=False
#----------------------------------------------------------
window=Tk()
window.title("la fourmi de longton")
window.iconbitmap("logo.ico")
window.resizable(False,False)
taille=10
width,height=1080,720
width,height=width//taille*taille,height//taille*taille
window.geometry(f"{width+5}x{height+65}")
canvas=Canvas(window,width=width, height=height,bg="white")
frame_form=Frame(window)
coordonnes=[]
for y in range(0,height,taille):
    row=[]
    for x in range(0,width,taille):
        canvas.create_rectangle(x,y,x+taille,y+taille,fill="white")
        row.append([(x,y),"white"])
    if row:
      coordonnes.append(row)
canvas.bind("<Button-1>",click_gauche)
canvas.bind("<Button-3>",click_droite)
window.bind("<Return>",commencer_la_simulation)
window.bind("<BackSpace>",stop)
#fourmmi(triangle)----------------------------------------------
fourmi_x,fourmi_y,direction=width//2-((width//2)%taille),height//2-((height//2)%taille),"haut"
canvas.create_polygon([fourmi_x+taille//2,fourmi_y,fourmi_x,fourmi_y+taille,fourmi_x+taille,fourmi_y+taille,fourmi_x+taille//2,fourmi_y])
canvas.pack()
#-----------------------------------------------------
frame_form.pack()
window.mainloop()