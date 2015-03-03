kata = raw_input('Masukan kata : ')
a = len(kata) - 1
print "".join(kata[:a] + kata[::-1])
