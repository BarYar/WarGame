from unittest import TestCase,mock
from unittest.mock import patch
from Game.Card import Card
class TestCard(TestCase):
    def setUp(self):
       self.card=Card("4","♠")
       self.other1=Card("3","♦")
       self.other3=Card("5","♣")
       self.other4=Card("4","♥")
       self.other2 =Card ("4","♦")
    #בודקת האם הוא מגדיר את הערכים נכון
    def testValue(self):
        self.assertTrue("4"==self.card.value)
    #בודק האם הוא מגדיר את הסוג נכון
    def testSuits(self):
        self.assertTrue("♠"==self.card.suit)
    #בודק שהוא מעלה value error כאשר הערכים הם לא ברשימת ערכים
    def testNonCardType(self):
        try:
            card=Card(1,5)
        except:
            pass
        else:
            self.fail()
#מתדוה הבודקת כאשר הtype הוא סטרינג והוא לא ברשימה
    def test_notinlist(self):
        try:
            card=Card("4","5")
        except:
            pass
        else:
            self.fail()
    #בודק ש__ge__ מחזיק true כאשר הערך יותר גדול
    def testge1(self):
        self.assertTrue(self.card>(self.other2))
     # בודק ש__ge__ מחזיר true כאשר הערך שווה והסוג גדול יותר
    def testge2(self):
            self.assertTrue(self.card>(self.other1))
    # בודק ש__ge__ מחזיר false כאשר הערך יותר קטן
    def testge3(self):
        self.assertFalse(self.card>(self.other3))
    # בודק ש__ge__ מחזיר true כאשר הערך יותר גדול
    def testge4(self):
            self.assertFalse(self.card>(self.other4))
    #פונקציה הבודקת את הrepr
    def testRepr(self):
        self.assertTrue("4♠"==self.card.__repr__())