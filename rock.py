from tkinter import *
from PIL import Image, ImageTk    #imaging library
from random import randint

#screen variable window and tk is the screen
window = Tk()
window.title("Rock,Paper and Scissor")
window.configure(background="#d2b48c") #background

image_rock1 = ImageTk.PhotoImage(Image.open("rl.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("pl.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("sl.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rr.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("pr.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("sr.png"))


#image for the rock paper scissor 

label_player=Label(window,image=image_scissor1)
label_computer=Label(window,image=image_scissor2)
label_computer.grid(row=1,column=0,sticky="nsew")
label_player.grid(row=1,column=4,sticky="nsew")

# scoring for the points

player_score= Label(window,text=0,font=("arail",60,"bold"),bg="#654321",fg="#d2b48c")
computer_score= Label(window,text=0,font=("arail",60,"bold"),bg="#654321",fg="#d2b48c")
player_score.grid(row=1,column=3,sticky="nsew")
computer_score.grid(row=1,column=1,sticky="nsew")

player_indicator= Label(window,font=("arial",40,"bold"),
                        text="Player",bg="#654321",fg="#d2b48c")
computer_indicator= Label(window,font=("arial",40,"bold"),
                        text="Computer",bg="#654321",fg="#d2b48c")
computer_indicator.grid(row=0,column=1,sticky="nsew")
player_indicator.grid(row=0,column=3,sticky="nsew")

# message for the win

final_message = Label(window,font=("arial",40,"bold"),bg="#654321",fg="#d2b48c")
final_message.grid(row=4,column=2,sticky="nsew")

# code for functions

def msg_upd(a):
    final_message["text"]=a

def comp_scoreupd():
    final= int(computer_score["text"])
    final=final+1
    computer_score["text"]= str(final)


def player_scoreupd():
    final= int(player_score["text"])
    final=final+1
    player_score["text"]= str(final)

def winner(p,c):
    if p==c:
        msg_upd("Its a tie")
    elif p== "rock":
        if c== "paper":
            msg_upd("Computer wins")
            comp_scoreupd()
        else:
            msg_upd("Player wins")
            player_scoreupd()
    elif p=="paper":
        if c== "scissor":
            msg_upd("Computer wins")
            comp_scoreupd()
        else:
            msg_upd("Player wins")
            player_scoreupd()
    elif p=="scissor":
        if c== "rock":
            msg_upd("Computer wins")
            comp_scoreupd()
        else:
            msg_upd("Player wins")
            player_scoreupd()
    else :
        pass

select=["rock","paper","scissor"]

def choice_upd(a):
    comp_choice=select[randint(0,2)]
    if comp_choice=="rock":
        label_computer.configure(image=image_rock2)
    elif comp_choice=="paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a=="rock":
        label_player.configure(image=image_rock1)
    elif a=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    winner(a,comp_choice)

window.grid_columnconfigure(2,minsize=360)

button_rock= Button(window,width=16,height=3,text=("Rock"),
                    font=("arial",20,"bold"),bg="#654321",fg="#d2b48c",command=lambda:choice_upd("rock")).grid(row=2,column=1,sticky="nsew")

button_paper= Button(window,width=16,height=3,text=("Paper"),
                     font=("arial",20,"bold"),bg="#654321",fg="#d2b48c",command=lambda:choice_upd("paper")).grid(row=2,column=2,sticky="nsew")

button_scissor= Button(window,width=16,height=3,text=("Scissor"),
                     font=("arial",20,"bold"),bg="#654321",fg="#d2b48c",command=lambda:choice_upd("scissor")).grid(row=2,column=3,sticky="nsew")
window.mainloop()
