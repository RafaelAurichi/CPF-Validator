entrada = input("Digite seu CPF: ")
entrada = entrada.replace(".", "")
entrada = entrada.replace("-", "")
listaInput = list(entrada)

validar1 = list(range(12));

if len(listaInput) == 11:

  if listaInput[0] == listaInput[1] == listaInput[2] == listaInput[3] == listaInput[4] == listaInput[5] == listaInput[6] == listaInput[7] == listaInput[8] == listaInput[9] == listaInput[10]:
    igual = 0
  else: igual = 1
    
  if igual == 1: 
    digito1 = (int(listaInput[0]) * 10) + (int(listaInput[1]) * 9) + (int(listaInput[2]) * 8) + (int(listaInput[3]) * 7) + (int(listaInput[4]) * 6) + (int(listaInput[5]) * 5) + (int(listaInput[6]) * 4) + (int(listaInput[7]) * 3) + (int(listaInput[8]) * 2)
    digito2 = (int(listaInput[0]) * 11) + (int(listaInput[1]) * 10) + (int(listaInput[2]) * 9) + (int(listaInput[3]) * 8) + (int(listaInput[4]) * 7) + (int(listaInput[5]) * 6) + (int(listaInput[6]) * 5) + (int(listaInput[7]) * 4) + (int(listaInput[8]) * 3) + (int(listaInput[9]) * 2)
      
    digito1 = digito1 * 10
    digito2 = digito2 * 10

    if (digito1 % 11 == 10 and int(listaInput[9]) == 0) or (digito2 % 11 == 10 and int(listaInput[10]) == 0):
      ditito1 = "certo"
      digito2 = "certo"

    if (digito1 % 11 == int(listaInput[9]) or digito1 == "certo") and (digito2 % 11 == int(listaInput[10]) or digito2 == "certo"):
      print("O CPF é válido!")
    else: print("CPF inválido! Por favor digite um CPF válido.")
  
  else: print("CPF inválido! Por favor digite um CPF válido.") 

else: print("CPF inválido! Por favor digite um CPF válido.")