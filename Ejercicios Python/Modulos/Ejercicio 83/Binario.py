def convertir_a_decimal( binario ):
     l = len(binario) - 1
     entero = 0
     for i in binario:
          potencia = 2 ** l
          entero = entero + ( int(i) * potencia)
          l = l - 1
     return entero

def sumar(pnumero, snumero):
     resultado=pnumero+snumero
     return resultado

def restar(pnumero, snumero):
     resultado=pnumero-snumero
     return resultado

def dividir(pnumero, snumero):
     resultado=pnumero/snumero
     return resultado

def multiplicar(pnumero, snumero):
     resultado=pnumero*snumero
     return resultado

def convertir_a_binario(numero_entero):
     binario = ""
     while (True):
          aux = str( numero_entero % 2 )
          numero_entero = int( numero_entero / 2 )
          binario = aux + binario
          if (numero_entero <= 1):
               binario = ( str( numero_entero ) if numero_entero > 0 else "" ) + binario
               break
     return binario
