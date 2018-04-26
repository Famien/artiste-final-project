import os

for f in os.listdir("trees"):
	os.system('convert '+"trees/"+f+' '+"trees/"+f.split('.')[0]+".png")
