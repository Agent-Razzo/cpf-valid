import sys

cpf = str(sys.argv[1])
result = 0

for x in cpf:
	if x not in [".", "-"]:
		result += int(x)

STR_result = str(result)
state_digit = cpf[10]

print(result)
if STR_result[0] == STR_result[1]:
	print("CPF Válido!")
else:
	print("CPF Inválido.")

match state_digit:
   case "0": print("CPF registrado em Rio Grande do Sul")
   case "1": print("CPF registrado em Distrito Federal ou Goiás ou Mato Grosso ou Mato Grosso do Sul ou Tocantins")
   case "2": print("CPF registrado em Pará ou Amazonas ou Acre ou Amapá ou Rondônia ou Roraima")
   case "3": print("CPF registrado em Ceará ou Maranhão ou Piauí")
   case "4": print("CPF registrado em Pernambuco ou Rio Grande do Norte ou Paraíba ou Alagoas")
   case "5": print("CPF registrado em Bahia ou Sergipe")
   case "6": print("CPF registrado em Minas Gerais")
   case "7": print("CPF registrado em Rio de Janeiro ou Espirito Santo")
   case "8": print("CPF registrado em São Paulo")
   case "9": print("CPF registrado em Paraná ou Santa Catarina")
   case _: print("Inválido.")
