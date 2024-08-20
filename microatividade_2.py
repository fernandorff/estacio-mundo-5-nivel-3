import pandas as pd

# Defina o caminho do arquivo CSV
csv_file_path = 'data.csv'

# Leia o conteúdo do arquivo CSV com o separador correto
data = pd.read_csv(csv_file_path, sep=';', engine='python', encoding='utf-8')

# Crie uma variável contendo um subconjunto de dados com apenas 3 colunas
subset_data = data[['Date', 'Pulse', 'Calories']]

# Imprima/exiba em tela os dados da variável original
print("Dados completos:")
print(data.to_string(index=False))

# Imprima/exiba em tela os dados da nova variável
print("\nSubconjunto de dados com 3 colunas:")
print(subset_data.to_string(index=False))
