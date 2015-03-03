kalimat = 'Saya sedang belajar python loohh'
voc = ['a', 'i', 'u', 'e', 'o']

print kalimat

print "".join(["." if n in voc else n for n in kalimat])