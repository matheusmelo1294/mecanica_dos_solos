print("Olá, pode me chamar de Ultron, irei lhe ajudar a calcular os ÍNDICES FÍSICOS. Começaremos com teor de umidade...")

peso_agua = float(input("Digite o peso da água existente:"))
print("O peso da água é:", peso_agua, )

peso_solo = float(input("Digite o peso das partículas sólidas:"))
print("O peso das partículas sólidas é:", peso_solo)

teor = (peso_agua/peso_solo)*100

print("O teor de umidade é:", teor, "%")

print("Agora a massa específica real")

peso_solo = float(input("Digite o peso do solo:"))
volume_solo = float(input("Digite o volume do solo:"))

massa_especifica_real = peso_solo/volume_solo

print("A massa específica real é:", massa_especifica_real)

print("Agora, a massa específica aparente úmida:")

peso_total = float(input("Digite o peso total:"))
volume_total = float(input("Digite o volume total:"))

meau = peso_total/volume_total

print("A massa específica aparente úmida é:", meau, "N/m³")

print("Agora iremos fazer o cálculo da massa específica aparente seca:")
peso_meas = float(input("Digite a variação de peso:"))
volume_rec = float(input("Digite o volume do recipiente"))

meas = peso_meas/volume_rec
print("A massa específica aparente seca é:", meas)

print("Vamos calcular a Densidade Global...")

pedp = float(input("Digite o peso específico das partículas:"))
pedvaa = float(input("Digite o peso específico de igual volume da água:"))

dg = pedp/pedvaa

print("Densidade Global:", dg)

print("Vamos calcular o índice de vazios")

volporos = float(input("Digite o volume dos poros:"))
volpartsol = float(input("Digite o volume ocupado pelas partículas sólidas:"))

indvazios = volporos/volpartsol

print("O volume de vazios é:", indvazios)

print("Vamos de POROSIDADE")

volume_dos_poros = float(input("Digite o volume dos poros:"))

volume_tot = float(input("Digite o volume total:"))

porosidade = (volume_dos_poros/volume_tot)*100

print("A porosidade do solo é:", porosidade, "%")

print("Estamos quase no final, agora é a vez do Grau de Saturação")

volh20 = float(input("Digite o volume de água:"))
vv = float(input("Digite o volume de vazios:"))

grausat = (volh20/vv)*100

print("O grau de saturação é:", grausat, "%")

print("O gran finale fica para o Grau de Aeração")

var = float(input("Digite o volume do ar:"))

vv2 = float(input("Digite o volume de vazios:"))

graudeaeracao = (var/vv2)*100

print("O grau de aeração é:", graudeaeracao, "%")

print("Chegamos ao fim, espero que tenha ajudado")

print("Software desenvolvido por Matheus Melo")
print("CREA: 62001802-0")
    
