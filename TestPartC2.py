from statements import *
from pos_tagging import *
import agreement
import unittest
from nltk import Tree
class TestPartC(unittest.TestCase):

    def test_1(self):
        t = Tree("VP",[Tree("T",["Tp"])])
        p = agreement.V_phrase_num(t)
        self.assertEquals(p,"p")

    def test_2(self):
        np = Tree("NP", [Tree("Nom",[Tree("AN",[Tree("N",["Np"])])])])
        vp = Tree("VP",[Tree("T",["Ts"]),np])
        p = agreement.V_phrase_num(vp)
        self.assertEquals(p,"s")

    def test_3(self):
        vp = Tree("VP",[Tree("BE",["Bep"]),Tree("A",["A"])])
        p = agreement.V_phrase_num(vp)
        self.assertEquals(p,"p")

    def test_4(self):
        vp1 = Tree("VP",[Tree("I",["Is"])])
        vp2 = Tree("VP",[Tree("BE",["Bep"]),Tree("A",["A"])])
        vp = Tree("VP",[vp1,"AND",vp2])
        p = agreement.V_phrase_num(vp)
        self.assertEquals(p,"s")

    def test_5(self):
        vp1 = Tree("VP",[Tree("I",["Is"])])
        rel = Tree("Rel",[Tree("WHO",["WHO"]),vp1])
        p = agreement.V_phrase_num(rel)
        self.assertEquals(p,"s")

    def test_6(self):
        t = Tree("T",["Ts"])
        np = Tree("NP", [Tree("Nom",[Tree("AN",[Tree("N",["Np"])])])])
        rel = Tree("Rel",[np,t])
        p = agreement.V_phrase_num(rel)
        self.assertEquals(p,"s")
    def test_7(self):
        t = Tree("I",["Is"])
        np = Tree("NP", [Tree("Nom",[Tree("AN",[Tree("N",["Np"])])])])
        rel = Tree("Rel",[np,t])
        p = agreement.V_phrase_num(rel)
        self.assertEquals(p,"")
    def test_8(self):
        vp2 = Tree("VP",[Tree("BE",["Bep"]),Tree("A",["A"])])
        qp = Tree("QP",[vp2])
        p = agreement.V_phrase_num(qp)
        self.assertEquals(p,"p")

    def test_9(self):
        np = Tree("NP", [Tree("Nom",[Tree("AN",[Tree("N",["Np"])])])])
        t = Tree("T",["Tp"])
        qp = Tree("QP",[Tree("DO",["DOs"]),np, t])
        p = agreement.V_phrase_num(qp)
        self.assertEquals(p,"p")
    def test_10(self):
        np = Tree("NP", [Tree("P",["P"])])
        t = Tree("T",["Tp"])
        qp = Tree("QP",[Tree("DO",["DOs"]),np, t])
        p = agreement.V_phrase_num(qp)
        self.assertEquals(p,"p")
    def test_11(self):
        np = Tree("NP", [Tree("P",["P"])])
        t = Tree("I",["Ip"])
        qp = Tree("QP",[Tree("DO",["DOs"]),np, t])
        p = agreement.V_phrase_num(qp)
        self.assertEquals(p,"")

if __name__ == "__main__":
    unittest.main()
