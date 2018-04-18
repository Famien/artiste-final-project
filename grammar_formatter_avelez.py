
# param - name of grammar
grammar = "grammar_avelez_167"

# constants
s_categories_phrases = set(["VP","NP","PP","notS","notVP"])


def open_grammar_append(g):
	return open(g,"a")

def open_grammar_read(g):
	return open(g,"r")

def rule_23(g):
	f = open_grammar_append(g)
	f.write("\n# adding rule (23)\n\n")
	for c in s_categories_phrases:
		f.write("1	"+c+"/"+c+" t\n")
	f.close()

def rule_22(g):
	f = open_grammar_append(g)
	f.write("\n# adding rule (22) Generalized Left Branch\n\n")
	for c in s_categories_phrases:
		for c2 in s_categories_phrases:
			if c!=c2:
				f.write("1 "+c+"/NP"+" "+c2+"/NP\n")
	f.close()

def rule_32(g):
	f = open_grammar_append(g)
	r = open_grammar_read(g)
	f.write("\n# adding rule (32) subject-auxiliary inversion\n\n")
	for line in r.readlines():
		if "#" not in line:
			rule = line.split()
			if len(rule)>=3 and rule[1]=="VP+FIN+AUX" and "V" in rule[2]:
				f.write("1 "+"Q V+FIN+AUX NP "+" ".join(rule[3:])+"\n")
	f.close()
	r.close()

def rule_76(g):
	f = open_grammar_append(g)
	f.write("\n# adding rule (76) rightward displacement\n\n")
	clausals = set(["S", "notS"])
	betas = clausals | s_categories_phrases
	for a in clausals:
		for b in betas:
			f.write("1 "+a+" "+a+"/"+b+" "+b+"\n")
	f.close()

# add rules
#rule_23(grammar)
# rule_22(grammar)
# rule_32(grammar)
# rule_76(grammar)


