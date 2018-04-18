from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import os

cf = CanvasFrame()
t = Tree.fromstring('(S (NP the Dodgers) (VP (VP (V beat) (NP the Red Sox)) (CCVP (CC and) (VP (VBD were) (VBN beaten) (PP (P by) (NP the Giants))))))')
tc = TreeWidget(cf.canvas(),t)
cf.add_widget(tc,10,10) # (10,10) offsets
##cf.print_to_file('tree.ps')
##cf.destroy()
##os.system('convert tree.ps tree.png')
