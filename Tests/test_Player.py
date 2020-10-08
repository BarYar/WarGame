from unittest import TestCase,mock
from unittest.mock import patch
from Game.DeckOfCards import DeckOfCards
from Game.Card import Card
from Game.Player import Player
class TestPlayer(TestCase):
    #פונקציית הsetup של testplayer
    def setUp(self):
        self.player=Player("Bar",8000)
        self.deck=DeckOfCards()
        self.player.setHand(self.deck)
    #בודק שמעלה התראה אם מכניסים כמות כסף מתחת ל5000 לשחקן
    def testinit1(self):
        try:
            player=Player("Yossi",500)
        except:
            pass
        else:
            self.fail()
#בודק שמעלה התראה כאשר הכמות קלפים לא בטווח של 52-0
    def testinit2(self):
        try:
            player = Player("Bar", 8000,-1)
        except:
            pass
        else:
            self.fail()
#בודק שמעדכן ערכים
    def testinit3(self):
        self.assertTrue(self.player.name=='Bar')
        self.assertTrue(self.player.money == 8000)
        self.assertTrue(self.player.cardamount == 5)
#בודק שלא מפעילים את הפונקציה אם מכניסים רשימה קצרה מ5
    def test_set_Hand1(self):
        dcards=DeckOfCards()
        dcards.deckcards.clear()
        card=Card("4","♣")
        for i in range(0,4):
            dcards.deckcards.append(card)
        self.player.cards.clear()
        try:
            self.player.setHand(dcards)
        except:
            pass
        else:
            self.fail()


#בודק שהפונקציה מעדכנת את הקלפים כאשר החפסית קלפים תקנית
    def test_set_Hand2(self):
        self.player.setHand(self.deck)
        self.assertTrue(len(self.player.cards)==self.player.cardamount)
#מתודה הבודקת אם getcard מעדכן את הcardsamount של השחקן
    def test_get_card1(self):
        am=self.player.cardamount
        self.player.getCard()
        self.assertEqual(am-1,self.player.cardamount)
#מתודה הבודקת אם הוא מחזיר None כאשר אין לשחקן קלפים
    def test_get_card2(self):
        player = Player("Yossi", 7000)
        card=player.getCard()
        self.assertTrue(card==None)
#מתודה הבודקת אם הוא מוציא קלף מהרשימת קלפים של שחקן
    def test_get_card3(self):
        cards=self.player.cards.copy()
        card=self.player.getCard()
        self.assertTrue(card in cards)
#מתודה הבודקת שהוא מעלה value error במידה והוא מכניס משתנה שהוא לא card
    def test_add_card1(self):
        a=5
        try:
            self.player.addCard(a)
        except:
            pass
        else:
            self.fail()

# מתודה הבודקת שהוא מוסיף קלף תקין ושהוא מעדכן את כמות הכרטיסים
    def test_add_card2(self):
        card=Card("4","♣")
        amount=self.player.cardamount
        self.player.addCard(card)
        self.assertTrue(amount+1==self.player.cardamount)
        self.assertIn(card,self.player.cards)
#מתודה הבודקת שהוא מעלה תקלה במידה והמספר שלילי
    def test_reduce_amount1(self):
        try:
            self.player.reduceAmount(-100)
        except:
            pass
        else:
            self.fail()
#מתודה הבודקת שהוא מעדכן את כמות הכסף כשהוא חוקי
    def test_reduce_amount2(self):
        money=self.player.money
        self.player.reduceAmount(100)
        self.assertTrue(money-100==self.player.money)
#מתדוה הבודקת שהוא מעלה התראה כאשר הtype של הכסף לא int
    def test_reduce_amount3(self):
        try:
            self.player.reduceAmount("100")
        except:
            pass
        else:
            self.fail()

# מתודה הבודקת שהוא מעדכן את כמות הכסף כשהוא חוקי
    def test_add_amount1(self):
        money = self.player.money
        self.player.addAmount(100)
        self.assertTrue(money + 100 == self.player.money)

# מתודה הבודקת שהוא מעלה תקלה במידה והמספר שלילי
    def test_add_amount2(self):
        try:
            self.player.addAmount(-100)
        except:
            pass
        else:
            self.fail()
#מתדוה הבודקת שהוא מעלה התראה כאשר הtype של הכסף לא int
    def test_add_amount3(self):
        try:
            self.player.addAmount("100")
        except:
            pass
        else:
            self.fail()
