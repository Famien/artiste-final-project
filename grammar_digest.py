# for line in file
# els = line.split()
# add els[1] to symbols
# print len(symbols)

symbols = set()
with open("grammar_final", "rb") as f:
  with open("grammar_final_digested", "wb") as f2:
    for line in f:
      print elements
      if len(elements) == 0:
          
      continue
      if elements[0][0] != "#" and elements[0] != "\n":
        symbol = elements[1]
        symbols.add(symbol)

print len(symbols)
print symbols
