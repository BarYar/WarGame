from unittest import TestCase,mock
from unittest.mock import patch
from Game.DeckOfCards import DeckOfCards
from Game.cards.Card import Card
class TestDeckOfCards(TestCase):
    #setUp לטסטים
    def setUp(self):
        self.deck=DeckOfCards()
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["♦", "♠", "♥", "♣"]
    #בדיקה לקונסטרקטור ערכים
    def testValues(self):
        self.assertTrue(self.deck.values==["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"])
    #בדיקה לקונסטרקטור סוגים
    def testSuits(self):
        self.assertTrue(self.deck.suits == ["♦","♠","♥","♣"])
    #בדיקה שהפונקציה קוראת נכון לnew game
    def testCallnginit(self):
        with patch('games.cards.DeckOfCards.DeckOfCards.newGame') as ng:
            deck=DeckOfCards()
            ng.assert_called_with(deck)
    # טסט שבודק את הקריאה לstartCards בnew game.
    def test_new_game1(self):
        with patch('games.cards.DeckOfCards.DeckOfCards.startCards') as sc:
            self.deck.newGame()
            sc.assert_called_with(self.deck)
    #טסט שבודק את הקריאה לשאפל בnew game
    def test_new_game2(self):
        with patch('games.cards.DeckOfCards.DeckOfCards._shuffle') as sh:
            self.deck.newGame()
            sh.assert_called_with(self.deck)
    #מתודה הבודקת את שזה מכניס 52 קלפים-עם ערכים מתאימים
    def test_start_cards(self):
        with patch('games.cards.DeckOfCards.DeckOfCards.newGame') as ng:
                ng.return_value=self.deck
                self.deck.newGame()
                d=[]
                for i in self.values:
                    for j in self.suits:
                        card=Card(i,j)
                        d.append(card)
                for i in range(0,52):
                    self.assertTrue(d[i] in self.deck.deckcards)
    #בדיקת פונקציית השאפל-בודק שמשנה את חבילת הקלפים-במקומות 0- במידה ולא השתנה אז גם ב20.
    #הסיבה שבודקים בשני מקומות-סטטיסטית קיים סיכוי שהראשון לא ישתנה
    def test_shuffle1(self):
        deck=[]
        for i in range(0,5):
            deck.append(self.deck.deckcards[i])
        self.deck._shuffle()
        try:
            self.assertTrue(self.deck.deckcards[0]!=deck[0])
        except:
            self.assertTrue(self.deck.deckcards[4] != deck[4])
    #מתודה שבודקת שזה לא עושה שאפל לחפיסת קלפים לא מלאה
    def test_shuffle2(self):
        card1=Card(self.deck.deckcards[0].value,self.deck.deckcards[0].suit)
        card2=Card(self.deck.deckcards[4].value,self.deck.deckcards[4].suit)
        del self.deck.deckcards[51]
        self.deck._shuffle()
        try:
            self.assertTrue(self.deck.deckcards[0] == card1)
        except:
            self.assertTrue(self.deck.deckcards[4] == card2)
    #פונקציה שבודקת את dealone חפיסה לא ריקה
    def test_deal_one1(self):
        card1=self.deck.deckcards[51]
        card2=self.deck.dealOne()
        self.assertTrue(card1==card2)
    #מתודה שבודקת את dealone חפיסה ריקה
    def test_deal_one2(self):
        deck1=DeckOfCards()
        deck1.deckcards=[]
        deck1.dealOne()
        deck1.deckcards=[]
    #מתודה שבודקת אם אורך החבילה מתקצר בdealone
    def test_deal_one3(self):
        num=len(self.deck.deckcards)
        self.deck.dealOne()
        self.assertTrue(num==len(self.deck.deckcards)+1)
    #מתודה שבודקת את המתודה show של החפיסה
    def test_show(self):
        with patch('games.cards.DeckOfCards.DeckOfCards.__repr__') as rp:
            self.deck.show()
            rp.assert_called_with(self.deck)
