from statements import *
from pos_tagging import *
import agreement
import unittest
from nltk import Tree
class TestPartC(unittest.TestCase):

    def test_1(self):
        np = Tree("NP", [Tree("Nom",[Tree("AN",[Tree("N",["Np"])])])])
        plural = agreement.N_phrase_num(np)
        self.assertEquals(plural,"p")

    def test_2(self):
        an = Tree("AN",[Tree("N",["Np"])])
        vp = Tree("VP",[Tree("I",["Is"])])
        np = Tree("NP", [Tree("Nom",[an,vp])])
        p = agreement.N_phrase_num(np)
        self.assertEquals(p,"p")

    def test_3(self):
        an1 = Tree("AN",[Tree("N",["Np"])])
        an2 = Tree("AN",["A",an1])
        vp = Tree("VP",[Tree("I",["Is"])])
        np = Tree("NP", [Tree("Nom",[an2,vp])])
        p = agreement.N_phrase_num(np)
        self.assertEquals(p,"p")

    def test_4(self):
        an = Tree("AN",[Tree("N",["Ns"])])
        nom = Tree("Nom",[an])
        np = Tree("NP",[Tree("AR",["AR"]), nom])
        p = agreement.N_phrase_num(np)
        self.assertEquals(p,"s")

    def test_5(self):
        np = Tree("P",["P"])
        p = agreement.N_phrase_num(np)
        self.assertEquals(p,None)


if __name__ == "__main__":
    unittest.main()
