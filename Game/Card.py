#מחלקה של קלף- לכל קלף יש ערך ומספר
class Card:
    #מתודת הקונסטרקטור של המחלקה
    def __init__(self,value,suit):
        self.suits = ["♦","♠","♥","♣"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if((type(value)==str)and(type(value)==str)):
            if((value in self.values)and(suit in self.suits)):
                self.value=value
                self.suit=suit
            else:
                raise ValueError("Invalid Card")
        else:
            raise ValueError("Invalid Card")
    #מתודת הrepr של המחלקה
    def __repr__(self):
        return f'{self.value}{self.suit}'
    #מתודה שבודקת איזה קלף בעל ערך גדול יותר
    def __gt__(self, other):
        otherv=0
        others=0
        myv=0
        mys=0
        for i in range (0,13):
            if (self.value == self.values[i]):
                myv = i
            if (other.value == self.values[i]):
                otherv = i
        for j in range (0,4):
            if (self.suit==self.suits[j]):
                    mys=j
            if (other.suit==self.suits[j]):
                    others=j
        if (myv>otherv):
            return True
        elif(myv==otherv):
            if(mys>others):
                return True
            else:
                return False
        else:
            return False
    def __eq__(self, other):
        if(type(other)==Card):
            if(self.suit==other.suit):
                if(self.value==other.value):
                    return True
            return False
        else:
            raise ValueError("You've entered a non card object.")

