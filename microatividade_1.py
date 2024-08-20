import pandas as pd

# Defina o caminho do arquivo CSV
csv_file_path = 'data.csv'

# Leia o conteúdo do arquivo CSV
data = pd.read_csv(csv_file_path, sep=',', engine='python', encoding='utf-8')

# Imprima/exiba em tela os dados da variável
print(data)
