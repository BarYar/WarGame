from Game.DeckOfCards import DeckOfCards
import random
from Game.Player import Player
import tkinter as game
import time
import os
#מחלקת משחק קלפים-בכל משחק יש 4 שחקנים וחבילת קלפים אחת
class CardGame:
    #פונקציית הקונסטרקטור של המחלקה-מקבלת כפרמטר את כמות הקלפים שכל שחקן מקבל
    def __init__(self,money,cardsAmount=5):
#יכולים להזין כמות קלפים גדולה מהחפסיסה כי זה תלוי במשחק.
        if(type(cardsAmount)==int):
            if(cardsAmount>=0):
                self.cardsAmount=cardsAmount
            else:
                raise ValueError("You've typed an invalid amount of cards.")
        else:
            raise ValueError("You've entered an invalid type for amount of cards.")
        if(type(money)==int):
            if(money>=0):
                self.money=money
            else:
                raise ValueError("You've entered an invalid amount of money.")
        else:
            raise ValueError("You've entered an invalid type for money.")
        self.deckCards = DeckOfCards()
        self.players=[]
        CardGame.playersPersonalInformation(self)
        CardGame.newGame(self)
    #מתודה המתחילה משחק חדש.
    def newGame(self):
        self.deckCards.newGame()
        for i in range(0,4):
            self.players[i].cardamount=self.cardsAmount
            self.players[i].setHand(self.deckCards)
        CardGame.print(self)
    #מתודה הבודקת את הג'ימייל
    def testmail(self,mail):
        p=0
        for i in range(0,len(mail)):
            if (mail[i]=="@"):
                p=i
                break
        if(p!=0):
            if(mail[p:len(mail)]=="@gmail.com"):
                return True
        return False

    # מתודה המכניסה את שמות השחקנים לרשימה ומוודא שפרטיהם נכונים
    def ename(self):
        name = self.playersname.get()
        mail=self.emailp.get()
        self.er.config(text="")
        self.mer.config(text="")
        if (name == ""):#מוודא שהשם לא ריק
            self.er.config(text='Type a Password!',fg="red")
        if not self.testmail(mail):#מוודא שהמייל תקין
            self.mer.config(text='Invalid mail!',fg="red")
        else: #אם כל הפרטים תקינים-מכניס לרשימה ומוחק את הפרטים מהEntry
            self.playersname.delete(0, 'end')
            self.emailp.delete(0, 'end')
            player = Player(name, self.money,mail)
            self.players.append(player)
            self.countp += 1
            self.playersname.delete(0, 'end')
        if (self.countp == 5):#אם הוכנסו כבר ארבעה שחקנים-מוחק את החלון
            self.playersbuttun.destroy()
            self.playersname.destroy()
            self.emailp.destroy()
            self.labeln.destroy()
            self.labelm.destroy()
            self.er.destroy()
            self.mer.destroy()
            self.welcome.destroy()
            begin = game.Label(text="Now Let's start the game.")
            begin.grid(row=2,column=1)
            self.window.after(10,lambda :self.window.destroy())

    #מתודה שמריצה את חלון הכנסת פרטי השחקן Tkinter
    def playersPersonalInformation(self):
        #הגדרות בסיסיות לחלון
        self.countp=1
        self.window = game.Tk()
        self.window.geometry("400x200")
        self.window.title("War Game")
        project_root = os.path.dirname(os.path.dirname(__file__))#מוצא את תיקיית הפרויקט
        self.window.iconbitmap(f'{project_root}\Files\joker.ico')
        #הגדרות הLabels לחלון
        self.welcome = game.Label(text="Let's start the game.\n But first you need to enter your 4 players information.", fg="green")
        self.welcome.grid(row=1,column=1)
        # time.sleep(5)
        # self.welcome.destroy()
        self.playersname=game.Entry()
        self.playersname.grid(row=2,column=1)
        self.labeln=game.Label(text="Name:")
        self.labeln.grid(row=2, column=0)
        self.emailp=game.Entry()
        self.emailp.grid(row=3,column=1)
        self.labelm = game.Label(text="Mail:")
        self.labelm.grid(row=3, column=0)
        self.playersbuttun=game.Button(text="Enter",command=self.ename)
        self.playersbuttun.grid(row=4,column=1)
        self.er = game.Label()
        self.er.grid(row=5, column=1)
        self.mer = game.Label()
        self.mer.grid(row=6, column=1)


    #מתודת הדפסה של המשחק קלפים
    def print(self):
        for i in range (0,4):
            print (f'His name is:{self.players[i].name},He has:{self.players[i].money} ILS .\n His cards are:{self.players[i].cards}')

