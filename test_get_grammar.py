import nltk
from nltk.corpus import treebank
from nltk.grammar import CFG, Nonterminal
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

nltk.download('treebank')

mini_grammar = CFG(Nonterminal('S'),
                                  treebank.parsed_sents()[0].productions())
parser = nltk.parse.EarleyChartParser(mini_grammar)

t = nltk.corpus.treebank.parsed_sents('wsj_0001.mrg')[0]

cf = CanvasFrame()

tc = TreeWidget(cf.canvas(),t)
cf.add_widget(tc,10,10) # (10,10) offsets
cf.print_to_file('tree.ps')
cf.destroy()
