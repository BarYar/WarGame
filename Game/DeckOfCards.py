import random
from Game.Card import Card
#מחלקה של רשימה של קלפים, המחלקה תכיל חפיסת קלפים שלמה 13 קלפים מכל סוג-סה"כ 52 קלפים
class DeckOfCards:
    #הקונסטרקטור של המחלקה
    def __init__(self):
        self.suits=["♦","♠","♥","♣"]
        self.values=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]
        DeckOfCards.newGame(self)
    #מתודה המכניסה את הערכים לחבילה.
    def startCards(self):
        for i in self.values:
            for j in self.suits:
                card=Card(i,j)
                self.deckcards.append(card)
    #מתדוה פרטית המערבבת את החפיסה
    def _shuffle(self):
        if(len(self.deckcards)!=52):
            pass
        else:
            random.shuffle(self.deckcards)
    #מתודה המחזירה את הקלף מראש החפיסה
    def dealOne(self):
        if(len(self.deckcards)>0):
            card=self.deckcards.pop()
            return card
    #מתודה המתחילה משחק חדש
    def newGame(self):
        self.deckcards=[]
        DeckOfCards.startCards(self)
        DeckOfCards._shuffle(self)
    #מתודה repr של המחלקה
    def __repr__(self):
        return f'{self.deckcards}'
    #מתודה המדפיסה את כל הקלפים בחפיסה
    def show(self):
        print(DeckOfCards.__repr__(self))




