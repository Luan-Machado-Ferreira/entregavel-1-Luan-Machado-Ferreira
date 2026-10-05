# entregavel-1-Luan-Machado-Ferreira
Repositório para arquivos relacionados ao entregável 1 da fase 2 do processo seletivo da Minerva Harpia.

**Autor:** Luan Machado Ferreira

## Objetivo

O programa `missao.py` verifica se um robô possui bateria suficiente para concluir uma missão, considerando:

- A bateria atual, em porcentagem.
- A duração prevista da missão, em minutos.
- O consumo de bateria por minuto, em pontos percentuais.

O cálculo considera que o consumo por minuto permanece constante durante toda a missão. O programa informa se a missão pode ser concluída e quanto restará de bateria ou quantos pontos percentuais faltarão.

## Requisitos

- **Python 3 instalado** para executar o programa.
- **Git instalado** para clonar o repositório. (Opcional, você pode baixar o arquivo zip do código, abrindo o repoitório, depois clicando em "código" e depois em baixar zip.)

O programa pode ser executado no Windows ou no Linux e não requer a instalação de pacotes adicionais do Python.

## Como clonar o repositório

1. Abra o terminal e acesse a pasta onde deseja guardar o projeto.

2. Execute o comando abaixo para baixar o repositório:

   ```bash
   git clone https://github.com/Luan-Machado-Ferreira/entregavel-1-Luan-Machado-Ferreira.git
   ```

3. Entre na pasta criada pela clonagem:

   ```bash
   cd entregavel-1-Luan-Machado-Ferreira
   ```

Essa é a pasta principal do repositório, onde estão o arquivo `README.md` e as pastas `src` e `imagens`.

## Como executar o programa

Execute um dos comandos abaixo **a partir da pasta principal do repositório**.

### Linux, WSL ou Windows (CMD ou PowerShell)

```bash
python3 src/missao.py
```

Após iniciar o programa, digite cada valor solicitado e pressione **Enter**.

## Valores de entrada

| Entrada | Valores aceitos |
| --- | --- |
| Bateria atual | Entre 0 e 100. Pode ser informada como `80` ou `80%`. |
| Duração prevista | Número maior que zero, em minutos. |
| Consumo por minuto | Número maior que zero, em pontos percentuais de bateria por minuto. |

Para valores decimais, utilize ponto, por exemplo `2.5`.

## Exemplos de execução

### Bateria suficiente

```text
Bem vindo ao programa que verifica se um robô tem bateria suficiente para realizar uma missão!
Digite em porcentagem a bateria atual: 80%
Digite a duração prevista da missão, em minutos: 10
Digite o consumo por minuto, em pontos percentuais da bateria: 5
A missão pode ser concluída e a bateria restante será de: 30.0%
```

Nesse exemplo, o robô possui 80% de bateria e a missão consome 50 pontos percentuais: 10 minutos multiplicados por 5 pontos percentuais por minuto. Portanto, restam 30% de bateria.

### Bateria insuficiente

```text
Bem vindo ao programa que verifica se um robô tem bateria suficiente para realizar uma missão!
Digite em porcentagem a bateria atual: 10%
Digite a duração prevista da missão, em minutos: 10
Digite o consumo por minuto, em pontos percentuais da bateria: 5
A missão não pode ser concluída e a bateria, em pontos percentuais, faltante será de: 40.0
```

Nesse exemplo, o robô possui 10% de bateria e a missão consome 50 pontos percentuais: 10 minutos multiplicados por 5 pontos percentuais por minuto. Portanto, faltará 40 pontos percentuais de bateria.

### Valor numérico inválido

Valores numéricos fora dos limites aceitos geram uma mensagem indicando qual entrada é inválida. A validação ocorre após a leitura das três entradas.

```text
Bem vindo ao programa que verifica se um robô tem bateria suficiente para realizar uma missão!
Digite em porcentagem a bateria atual: -9%
Digite a duração prevista da missão, em minutos: 2
Digite o consumo por minuto, em pontos percentuais da bateria: 1
Programa encerrado, motivo: Valor inválido para bateria.
```

## Arquivos do projeto

| Arquivo | Descrição |
| --- | --- |
| `README.md` | Descrição do projeto e instruções de clonagem e execução. |
| `src/missao.py` | Código Python do programa. |
| `imagens/terminal.png` | Captura de tela da execução no terminal Linux. |
