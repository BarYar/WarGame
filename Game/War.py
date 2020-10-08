from Game.CardGame import CardGame
import random
import time
import tkinter as tk
from tkinter.ttk import *
import smtplib, ssl
from tkinter import font
import os
#פונקציה שמוחקת את כל הframes בwindow
def clearFrames(window):
    list=window.winfo_children()
    for i in list:
        i.destroy()
class war:
    def __init__(self):
        self.countcards = 0  # כמות קלפים בround
        self.discards = []  # כרטיסים שיצאו משימוש
        self.rounds = 0  # כמות סיבובים
        # פונקציה המוציא את הקלף הכי גדול
        # משחק מלחמה
        self.money = random.randint(5000, 10000)
        self.game = CardGame(self.money)
        self.cards = []
        self.rcards = {}
        self.max1 = 0
        self.max2 = 0
        self.maxmoney=0
        self.winners=[]
        self.winnerLabels=[]
        self.project_root = os.path.dirname(os.path.dirname(__file__))  # מוצא את תיקיית הפרויקט
        port = 465  # For SSL
        # Create a secure SSL context
        context = ssl.create_default_context()
        b = False
        # שולח מייל עם הקלפים לשחקנים.
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            while not b:
                try:
                    password = input("Type your password and press enter: ")
                    server.login("card.game1j@gmail.com", password)
                except:
                    print("Invalid password.")
                else:
                    b=True
            sender_email = "card.game1j@gmail@gmail.com"
            for i in range(0,4):
                message=self.game.players[i].cards.__repr__().encode('utf-8')
                #message=message,f'{message},{i},{str(c)}'
                #message = f'Hey {game.players[i].name} your cards are: {c}'.encode('utf-8')
                server.sendmail(sender_email,self.game.players[i].mail,message)
                #@gmail.com
        self.newWindow()
        self.newround()
    #מהלך של שחקן במשחק
    def pmove(self,player,card):
        self.discards.append([player,card])
        if(self.countcards<4):
            self.countcards += 1
            self.game.players[player].money -= (100*self.rounds)
            self.cards.append(self.game.players[player].cards[card])
            self.rcards[self.game.players[player].name]=self.game.players[player].cards[card]
            for i in range(0,5):
                self.lbutton[player][i].config(state=tk.DISABLED)
        if (self.countcards == 4):
            self.rounds += 1
            print("hey",self.countcards)
            roundmoney = self.rounds * 100 * 4
            if (self.cards[0] > (self.cards[1])):
                self.max1 = 0
            else:
                self.max1 = 1
            if (self.cards[2] > (self.cards[3])):
                self.max2 = 2
            else:
                self.max2 = 3
            if (self.cards[self.max1] > (self.cards[self.max2])):
                pass
            else:
                self.max1 = self.max2
            self.game.players[self.max1].addAmount(roundmoney)
            print(self.game.players[self.max1].money)
            print(self.rounds)
            self.winnerLabels.append(tk.Label(self.window,text=f'Round:{self.rounds}, winner is:{self.game.players[self.max1].name}, the cards were:\n{self.rcards} ',height=23, width=250,font=self.fontw,compound=tk.CENTER,image=self.background_image))
            self.winnerLabels[self.rounds-1].place(x=0,y=50+self.rounds*100)
            self.cards.clear()
            self.rcards.clear()
            self.countcards=0
            self.max1=0
            self.max2=0
            if(self.rounds==5):
                print("bye")
                clearFrames(self.window)
                self.endGame()
            else:
                self.newround()
    def newWindow(self):
        #חלון המשחק
        self.window=tk.Tk()
        self.window.geometry("1000x1050")
        self.background_image=tk.PhotoImage(file=f'{self.project_root}\Files\BgPic.png')
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.title("War Game")
        #הגדרת הפונטים
        self.fonttitle = font.Font ( family="Helvetica",size=26,weight="bold" )
        self.fontp=font.Font ( family="Times New Roman",size=15,weight="bold" )
        self.fontb=font.Font( family="Times New Roman",size=17,weight="bold" )
        self.fontw=font.Font( family="Times New Roman",size=10,weight="bold" )
        self.window.iconbitmap(r'C:\Users\user7\PycharmProjects\Loop4\games\cards\joker.ico')
        self.welcome = tk.Label(text="The War Game!", fg="black",bg="white",height=3, width=14,font=self.fonttitle)
        self.welcome.place(x=350,y=0)
        self.cpic=tk.PhotoImage(file=f'{self.project_root}\Files\CardPic.png')
    #מתודה המתחילה round חדש
    def newround(self):
        self.lframe = []
        self.lbutton = []
        self.lplayerst = []
        for i in range(0,4):
            self.lframe.append(tk.Frame(self.window))
            self.lplayerst.append(tk.Label(self.lframe[i],text=f'Name:{self.game.players[i].name} Money:{self.game.players[i].money} ',height=3,width=24,font=self.fontp
                                      ,fg="black",bg="white"))
            self.lplayerst[i].pack(side='top')
            self.lbutton.append([])
            for j in range(0,5):
                self.lbutton[i].append(tk.Button(self.lframe[i],text=j+1, image=self.cpic,compound=tk.CENTER,command=lambda j=j,i=i: self.pmove(i,j),fg='yellow',font=self.fontb))
                self.lbutton[i][j].pack(side='left')
                self.lbutton[i][j].config(height=80, width=53)
                if ([i,j] in self.discards):
                    self.lbutton[i][j].config(state=tk.DISABLED)
            self.lframe[i].place(x=350,y=(i*1.35+1)*150)
        self.window.mainloop()
    #מתודה אשר רצה בסוף המשחק
    def endGame(self):
        print("heyyyy")
        self.background_image=tk.PhotoImage(file=f'{self.project_root}\Files\BgPic.png')
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.welcome = tk.Label(text="The War Game!", fg="black", bg="white", height=3, width=14, font=self.fonttitle)
        self.welcome.place(x=350, y=0)
        for i in range (0,4):
            if(self.game.players[i].money>self.maxmoney):
                self.winners.clear()
                self.winners.append(self.game.players[i])
                self.maxmoney=self.game.players[i].money
            elif (self.game.players[i].money == max):
                self.winners.append(self.game.players[i])
        s=' is'
        b=False
        if(len(self.winners)>1):
            s='s are'
            b=True
        winst=f'The winner{s}:'
        for i in range(0,len(self.winners)):
            winst=winst+self.winners[i].name
            winst=winst+f' Money:{self.money}'
        self.WinnerLabelGame=tk.Label(text=winst,font=self.fonttitle)
        self.WinnerLabelGame.place(x=275,y=300)




