import unittest
from statements import *
class TestPartA3(unittest.TestCase):
    #est
    def test_1(self):
        self.assertEqual(verb_stem("eats"),"eat")
    def test_2(self):
        self.assertEqual(verb_stem("tells"),"tell")
    def test_3(self):
        self.assertEqual(verb_stem("shows"),"show")
    def test_4(self):
        self.assertEqual(verb_stem("pays"),"pay")
    def test_5(self):
        self.assertEqual(verb_stem("buys"),"buy")
    def test_6(self):
        self.assertEqual(verb_stem("flies"),"fly")
    def test_7(self):
        self.assertEqual(verb_stem("tries"),"try")
    def test_8(self):
        self.assertEqual(verb_stem("unifies"),"unify")
    def test_9(self):
        self.assertEqual(verb_stem("dies"),"die")
    def test_10(self):
        self.assertEqual(verb_stem("lies"),"lie")
    def test_11(self):
        self.assertEqual(verb_stem("ties"),"tie")
    def test_12(self):
        self.assertEqual(verb_stem("unties"),"untie")
    def test_13(self):
        self.assertEqual(verb_stem("goes"),"go")
    def test_14(self):
        self.assertEqual(verb_stem("boxes"),"box")
    def test_15(self):
        self.assertEqual(verb_stem("attaches"),"attach")
    def test_16(self):
        self.assertEqual(verb_stem("washes"),"wash")
    def test_17(self):
        self.assertEqual(verb_stem("dresses"),"dress")
    def test_18(self):
        self.assertEqual(verb_stem("fizzes"),"")
    def test_19(self):
        self.assertEqual(verb_stem("loses"),"lose")
    def test_20(self):
        self.assertEqual(verb_stem("dazes"),"")
    def test_21(self):
        self.assertEqual(verb_stem("lapses"),"lapse")
    def test_22(self):
        self.assertEqual(verb_stem("analyzes"),"analyze")
    def test_23(self):
        self.assertEqual(verb_stem("has"),"have")
    def test_24(self):
        self.assertEqual(verb_stem("likes"),"like")
    def test_25(self):
        self.assertEqual(verb_stem("hates"),"hate")
    def test_26(self):
        self.assertEqual(verb_stem("bathes"),"bathe")
    def test_28(self):
        self.assertEqual(verb_stem(""),"")
    def test_29(self):
        self.assertEqual(verb_stem("flys"),"")
    def test_30(self):
        self.assertEqual(verb_stem("wangjangles"),"")
    '''
    I think that this should be tested, but others don't, so uncomment
    if it turns out that it works
    def test_31(self):
        self.assertEqual(verb_stem("did"),"do")
    def test_32(self):
        self.assertEqual(verb_stem("are"),"are")
    '''

if __name__ == "__main__":
    unittest.main()
