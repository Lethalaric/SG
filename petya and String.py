inputan1 = raw_input('Inputan 1 : ')
inputan2 = raw_input('Inputan 2 : ')

print "".join(["0" if inputan1 == inputan2  else "-1" if inputan1 < inputan2 else "1"])