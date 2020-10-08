from Game.Card import Card
import random
#מחלקת שחקן-מכילה את השם, כמות כסף וקלפים
class Player:
    #מתודת הקונסטרקטור של המחלקה player
    def __init__(self,name,money,mail,cardamount=5):
        self.name=name
        self.mail=mail
        if(money>=5000):
            self.money=money
        else:
            raise ValueError("You've typed an invalid money.")
        if((cardamount>=0)and(cardamount<=52)):
            self.cardamount=cardamount
        else:
            raise ValueError("You've typed an invalid cards amount.")
        self.cards=[]
    #מתודה המקבלת חבילת קלפים חדשה עבור שחקן
    def setHand(self,dcards):
        if(len(dcards.deckcards)>=self.cardamount):
            self.cards.clear()
            for i in range(0,self.cardamount):
                self.cards.append(dcards.dealOne())
        else:
            raise ValueError("The Deck is too short")
    #מתודה המושכת קלף אקראי מהשחקן
    def getCard(self):
        if(len(self.cards)>0):
            i=random.randint(0,self.cardamount-1)
            card=self.cards.pop(i)
            self.cardamount-=1
            return card

    #מתודה המוסיפה קלף לחפיסה
    def addCard(self,card):
        if(type(card)==Card):
            self.cards.append(card)
            self.cardamount+=1
        else:
            raise ValueError("It's not a card.")
    #מתודה המורידה כסף מקופת השחקן
    def reduceAmount(self,money):
        if((type(money)==int)or(type(money)==float)):
            if (money>0):
                self.money=self.money-money
            else:
                raise ValueError("You've entered a negative amount of money")
        else:
            raise ValueError("You've entered an invalid money type.")
    #מתודה המוסיפה כסף לשחקן
    def addAmount(self,money):
        if ((type(money) == int) or (type(money) == float)):
            if(money>0):
                self.money=self.money+money
            else:
                raise ValueError("You've entered a negative amount of money")
        else:
            raise ValueError("You've entered an invalid money type.")
    #מתודה repr של המחלקה
    def __repr__(self):
        return f'The name of the player is:{self.name}, the money of the player is: {self.money}, the cards amount is:{self.cardamount}, the cards of the player are: {self.cards}'
    #מתודת הדפסה של פרטי השחקן
    def print(self):
        print(Player.__repr__(self))
