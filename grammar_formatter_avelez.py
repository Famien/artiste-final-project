
# param - name of grammar
grammar = "grammar_avelez_167"

# constants
s_categories_phrases = set(["VP","NP","PP","notS","notVP"])


def open_grammar(g):
	return open(g,"a")

def rule_23(g):
	f = open_grammar(g)
	f.write("\n# adding rule (23)\n\n")
	for c in s_categories_phrases:
		f.write("1	"+c+"/"+c+" t\n")
	f.close()

def rule_22(g):
	f = open_grammar(g)
	f.write("\n# adding rule (22) Generalized Left Branch\n\n")
	for c in s_categories_phrases:
		for c2 in s_categories_phrases:
			if c!=c2:
				f.write("1 "+c+"/NP"+" "+c2+"/NP\n")
	f.close()

# add rules
rule_23(grammar)
rule_24(grammar)