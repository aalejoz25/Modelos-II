ASCII = open("codigoASCII.txt","w+")
for x in range(255):
  ASCII.write(chr(x))
ASCII.close()
