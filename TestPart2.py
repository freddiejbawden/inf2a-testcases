import unittest
from pos_tagging import *
lx = Lexicon()
lx.add("John","P")
lx.add("orange","N")
lx.add("orange","A")
lx.add("fish","N")
lx.add("fish","I")
lx.add("fish","T")
lx.add("likes","I")


class TestPartB1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(noun_stem("countries"),"country")
    def test_2(self):
        self.assertEqual(noun_stem("dogs"),"dog")
    def test_3(self):
        self.assertEqual(noun_stem("ashes"),"ash")
    def test_4(self):
        self.assertEqual(noun_stem("women"),"woman")
    def test_5(self):
        self.assertEqual(noun_stem("sheep"),"sheep")
    def test_6(self):
        self.assertEqual(noun_stem("buffalo"),"buffalo")
    def test_7(self):
        self.assertEqual(noun_stem("men"),"man")
    def test_8(self):
        self.assertEquals(noun_stem("butterflys"),"")

    def test_8(self):
        self.assertEqual(tag_word(lx,"John"),["P"])
    def test_9(self):
        self.assertEqual(sorted(tag_word(lx,"orange")),["A","Ns"])
    def test_10(self):
        self.assertEqual(sorted(tag_word(lx,"fish")),sorted(["Ns","Np","Ip","Tp"]))
    def test_11(self):
        self.assertEqual(tag_word(lx,"a"),["AR"])
    def test_12(self):
        self.assertEqual(tag_word(lx,"zxghqw"),[])
    def test_13(self):
        x = "John likes fish"
        expout =[['P', 'Is', 'Ns'], ['P', 'Is', 'Np'], ['P', 'Is', 'Tp'], ['P', 'Is', 'Ip']]

        self.assertEqual(sorted(tag_words(lx,x.split(" "))),sorted(expout))
    def test_14(self):
        self.assertTrue("sheep" in unchanging_plurals_list)

if __name__ == "__main__":
    unittest.main()
