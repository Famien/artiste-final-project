

def main():
	from nltk import Tree
	from nltk.draw.util import CanvasFrame
	from nltk.draw import TreeWidget
	import os
	import sys

	file = sys.argv[1]
	name = file[-3:]
	f = open(file,"r")
	i = 0
	for s in f.readlines():
		cf = CanvasFrame()
		t = Tree.fromstring(s)
		tc = TreeWidget(cf.canvas(),t)
		cf.add_widget(tc,10,10) # (10,10) offsets
		nf = "tree"+name+str(i)+".ps"
		cf.print_to_file(nf)
		cf.destroy()
		os.system("mv "+nf+" trees/"+nf)
		i+=1

main()	