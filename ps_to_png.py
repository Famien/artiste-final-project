def main():
    import os
    import sys

    for i in range(2, 42):
        fname = 'tree' + str(i)
        os.system('convert ' + fname + '.ps ' + fname + '.png')
        print(i)

main()	
