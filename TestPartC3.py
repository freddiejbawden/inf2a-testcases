from statements import *
from pos_tagging import *
from agreement import *
import unittest
from nltk import Tree

class TestPartC3(unittest.TestCase):

    def test_1(self):
        # S -> Nom QP
        an = Tree("AN",[Tree("N",["Ns"])])
        nom = Tree("Nom",[an])
        vp2 = Tree("VP",[Tree("BE",["Bes"]),Tree("A",["A"])])
        qp = Tree("QP",[vp2])
        s = Tree("S",[nom,qp])
        self.assertFalse(check_node(s))
    def test_2(self):
        an = Tree("AN",[Tree("N",["Ns"])])
        nom = Tree("Nom",[an])
        np = Tree("NP",[Tree("AR",["AR"]),nom])
        self.assertTrue(check_node(np))
    def test_3(self):
        an = Tree("AN",[Tree("N",["Np"])])
        nom = Tree("Nom",[an])
        np = Tree("NP",[nom])
        self.assertTrue(check_node(np))
    def test_4(self):
        do = Tree("DO",["DOs"])
        an = Tree("AN",[Tree("N",["Ns"])])
        nom = Tree("Nom",[an])
        np = Tree("NP",[Tree("AR",["AR"]),nom])
        t = Tree("T",["Tp"])
        qp = Tree("QP",[do,np,t])
        self.assertTrue(check_node(qp))
    def test_5(self):
        do = Tree("DO",["DOs"])
        an = Tree("AN",[Tree("N",["Ns"])])
        nom = Tree("Nom",[an])
        np = Tree("NP",[Tree("AR",["AR"]),nom])
        t = Tree("T",["Ts"])
        qp = Tree("QP",[do,np,t])
        self.assertFalse(check_node(qp))







if __name__ == "__main__":
    unittest.main()
