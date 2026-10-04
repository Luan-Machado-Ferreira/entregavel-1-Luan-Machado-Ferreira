def verificar_bateria_robo(bateria_atual, duracao_prevista, consumo):

    bateria_atual = float(bateria_atual.replace("%", ""))

    if bateria_atual < 0 or bateria_atual > 100:
        raise Exception("Programa encerrado, motivo: Valor inválido para bateria.")
    if duracao_prevista <= 0:
        raise Exception("Programa encerrado, motivo: Valor inválido para a duração prevista.")
    if consumo <= 0:
        raise Exception("Programa encerrado, motivo: Valor inválido para o consumo.")
    
    consumo_total = duracao_prevista * consumo
    bateria_restante_estimada = bateria_atual - consumo_total

    return bateria_restante_estimada < 0, bateria_restante_estimada

print("Bem vindo ao programa que verifica se um robô tem bateria suficiente para realizar uma missão!")

resultado = verificar_bateria_robo(
    input("Digite em porcentagem a bateria atual: "),
    float(input("Digite a duração prevista da missão, em minutos: ")),
    float(input("Digite o consumo por minuto, em pontos percentuais da bateria: "))
)

if resultado[0] == False:
    print(f"A missão pode ser concluída e a bateria restante será de: {resultado[1]}%")
else:
    print(f"A missão não pode ser concluída e a bateria, em pontos percentuais, faltante será de: {resultado[1]*-1}")