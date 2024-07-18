def get_minimum_coins(configuration, change):
  # Configurações de moedas
  coin_configurations = {
      1: [1, 2, 5, 10, 25, 50, 100],
      2: [1, 5, 10, 20, 50, 100],
      3: [1, 2, 5, 10, 20, 50, 100],
      4: [1, 5, 12, 24, 50, 100] 
  }

  # Seleciona a configuração de moedas
  coins = coin_configurations[configuration]

  # Ordena as moedas da maior para a menor
  coins.sort(reverse=True)

  # Dicionário para armazenar a quantidade de moedas de cada valor
  coin_count = {coin: 0 for coin in coins}

  # Calcula a quantidade mínima de moedas
  total_coins = 0
  for coin in coins:
      while change >= coin:
          change -= coin
          coin_count[coin] += 1
          total_coins += 1

  # Exibe o resultado
  result = []
  for coin in coins:
      if coin_count[coin] > 0:
          result.append(f"{coin_count[coin]} moeda(s) de {coin} centavo(s)")

  result.append(f"Total de moedas: {total_coins}")

  return result

def main():
  # Solicita ao usuário a configuração desejada
  print("Escolha a configuração de moedas:")
  print("1: Moedas de 1, 2, 5, 10, 25, 50 e 100 centavos")
  print("2: Moedas de 1, 5, 10, 20, 50 e 100 centavos")
  print("3: Moedas de 1, 2, 5, 10, 20, 50 e 100 centavos")
  print("4: Moedas de 1, 5, 12, 24, 50 e 100 centavos")

  configuration = int(input("Digite o número da configuração desejada: "))

  # Solicita ao usuário o valor do troco
  change = int(input("Digite o valor do troco (em centavos): "))

  # Calcula a quantidade mínima de moedas
  result = get_minimum_coins(configuration, change)

  # Exibe o resultado
  print("Resultado:")
  for line in result:
      print(line)

# Executa o programa
main()
