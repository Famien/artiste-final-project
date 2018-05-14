##from nltk import Tree
##from nltk.draw.util import CanvasFrame
##from nltk.draw import TreeWidget
##import os
##
##cf = CanvasFrame()
##tstr = '(VP (V have wanted) (barVP (barVPword to) (VP (V know) (PP (P for) (NP (N many years))))))'
##t = Tree.fromstring(tstr)
##tc = TreeWidget(cf.canvas(),t)
##cf.add_widget(tc,10,10) # (10,10) offsets
##cf.print_to_file('tree.ps')
##cf.destroy()
##os.system('convert tree.ps tree.png')

def main():
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    import os
    import sys

    file = sys.argv[1]
    f = open(file,"r")
    i = 1
    for s in f.readlines():
        cf = CanvasFrame()
        t = Tree.fromstring(s)
        tc = TreeWidget(cf.canvas(),t)
        cf.add_widget(tc,10,10) # (10,10) offsets
        nf = "trees/tree"+str(i)+".ps"
        cf.print_to_file(nf)
        cf.destroy()
        #os.system("mv "+nf+" trees/"+nf)
        print(i)
        i+=1

main()	
