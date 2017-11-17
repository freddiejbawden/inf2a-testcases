from statements import *
import unittest

class TestPartAComplete(unittest.TestCase):
    def test_lexicon_add1(self):
        lx = Lexicon()
        lx.add("John","P")
        lx.add("Mary","P")
        x = lx.stems
        y = {"John" : ["P"],"Mary" : ["P"]}
        self.assertEqual(x,y)
    def test_lexicon_add2(self):
        lx = Lexicon()
        lx.add("John","P")
        lx.add("John","P")
        x = lx.stems
        y = {"John" : ["P"]}
        self.assertEqual(x,y)
    def test_lexicon_add2(self):
        lx = Lexicon()
        lx.add("John","P")
        lx.add("Mary","P")
        lx.add("like","T")
        x = lx.getAll("P")
        y = ["John","Mary"]
        self.assertEqual(x,y)
    def test_factbase_normal(self):
        fb = FactBase()
        fb.addUnary("duck","John")
        x = fb.queryUnary("duck","John")
        self.assertTrue(x)
    def test_factbase_singleEntry(self):
        fb = FactBase()
        fb.addUnary("duck","John")
        x = fb.unary
        y = {"duck":["John"]}
        self.assertEqual(x,y)
    def test_factbase_doubleEntry(self):
        fb = FactBase()
        fb.addUnary("duck","John")
        fb.addUnary("duck","John")
        x = fb.unary
        y = { "duck" : ["John"]}
        self.assertEqual(x,y)
    def test_factbase_binaryNormal(self):
        fb = FactBase()
        fb.addBinary("love","John","Mary")
        x = fb.binary
        y = {"love":[("John","Mary")]}
        self.assertEqual(x,y)
    def test_factbase_binaryDouble(self):
        fb = FactBase()
        fb.addBinary("love","John","Mary")
        fb.addBinary("love","John","Mary")
        x = fb.binary
        y = {"love":[("John","Mary")]}
        self.assertEqual(x,y)
    def test_binary_whole(self):
        lx = Lexicon()
        fb = FactBase()
        wlist = ("John loves Mary").split(" ")
        process_statement(lx, wlist, fb)
        x = fb.queryBinary("T_love","Mary","John")
        self.assertFalse(x)
    def test_binary_whole(self):
        lx = Lexicon()
        fb = FactBase()
        wlist = ("John loves Mary").split(" ")
        process_statement(lx, wlist, fb)
        x = fb.queryBinary("T_love","John","Mary")
        self.assertTrue(x)
    def test_unary_whole(self):
        lx = Lexicon()
        fb = FactBase()
        wlist = ("John ducks").split(" ")
        process_statement(lx, wlist, fb)
        x = fb.queryUnary("I_duck","John")
        self.assertTrue(x)

if __name__ == "__main__":
    unittest.main()
