import pandas as pd

# Defina o caminho do arquivo CSV
csv_file_path = 'data.csv'

# Definir a propriedade max_rows para 9999
pd.set_option('display.max_rows', 9999)

# Leia o conteúdo do arquivo CSV com o separador correto
data = pd.read_csv(csv_file_path, sep=';', engine='python', encoding='utf-8')

# Crie uma variável contendo um subconjunto de dados com apenas 3 colunas
subset_data = data[['Date', 'Pulse', 'Calories']]

# Imprima as primeiras 10 linhas do conjunto de dados original
print("\nPrimeiras 10 linhas do conjunto de dados original:")
print(data.head(10).to_string(index=False))

# Imprima as últimas 10 linhas do conjunto de dados original
print("\nÚltimas 10 linhas do conjunto de dados original:")
print(data.tail(10).to_string(index=False))
