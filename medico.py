medicamentos = []

nome = input("Qual é o nome do paciente?\n")

saiu = False

while saiu == False: 
    remedioN = input("Qual é o nome do medicamento?\n")

    if remedioN.lower().strip() == "sair":
        saiu = True

        for medicamento in medicamentos:
            ind = medicamentos.index(medicamento)
            remNL = medicamentos[ind]
            remN = remNL[0]
            frNL = remNL[1]

            print("Nome do rémedio: ", remN, "\nFrequência: ", frNL)
                
        break
    else:
        remedio = [remedioN]
        medicamentos.append(remedio)
        frequencia = input("Quantas vezes por dia/semana o remédio deve ser tomado?\n")
        
        medicamentoNL = medicamentos.index(remedio)
        medicamentos[medicamentoNL].append(frequencia)
        for medicamento in medicamentos:
            ind = medicamentos.index(medicamento)
            remNL = medicamentos[ind]
            remN = remNL[0]
            frNL = remNL[1]
            
            if medicamento == remedio:
                print("Nome do rémedio: ", remN, "\nFrequência: ", frNL)
                break