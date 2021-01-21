from Arboles_Binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)

abb.transversal("inorden")
abb.transversal("preorden")
abb.transversal("posorden")
