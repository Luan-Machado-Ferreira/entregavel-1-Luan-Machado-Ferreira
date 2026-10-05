#Função principal. Verifica se a bateria disponível é suficiente para realizar a missão.
def verificar_bateria_robo(bateria_atual, duracao_prevista, consumo):

    # Remove o símbolo "%" e converte a entrada para um número decimal.
    bateria_atual = float(bateria_atual.replace("%", ""))

    # Valida os valores. Se uma condição for falsa, gera um AssertionError.
    assert 0 <= bateria_atual <= 100, "Programa encerrado, motivo: Valor inválido para bateria."
    assert duracao_prevista > 0, "Programa encerrado, motivo: Valor inválido para a duração prevista."
    assert consumo > 0, "Programa encerrado, motivo: Valor inválido para o consumo."

    # Calcula o consumo total da missão, em pontos percentuais de bateria.
    consumo_total = duracao_prevista * consumo

    # Calcula a bateria restante após o consumo previsto.
    bateria_restante_estimada = bateria_atual - consumo_total

    # Retorna uma tupla com dois elementos:
    # [0]: True se a bateria for insuficiente; False se for suficiente.
    # [1]: Valor estimado da bateria restante.
    return bateria_restante_estimada < 0, bateria_restante_estimada

# Exibe a apresentação do programa.
print("Bem vindo ao programa que verifica se um robô tem bateria suficiente para realizar uma missão!")

try:
    # Lê as três entradas e depois executa a função.
    # A bateria é passada como texto; duração e consumo são convertidos para float.
    resultado = verificar_bateria_robo(
        input("Digite em porcentagem a bateria atual: "),
        float(input("Digite a duração prevista da missão, em minutos: ")),
        float(input("Digite o consumo por minuto, em pontos percentuais da bateria: "))
    )
    # Se a bateria for suficiente, informa quanto restará.
    if resultado[0] == False:
        print(f"A missão pode ser concluída e a bateria restante será de: {resultado[1]}%")
    else:
        # Transforma o valor negativo em positivo para informar a quantidade faltante.
        print(f"A missão não pode ser concluída e a bateria, em pontos percentuais, faltante será de: {resultado[1]*-1}")
except AssertionError as erro:
    # Captura os erros gerados pelos asserts e exibe somente a mensagem.
    print(erro)