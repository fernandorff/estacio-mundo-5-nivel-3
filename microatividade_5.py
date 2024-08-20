import pandas as pd

# Defina o caminho do arquivo CSV
csv_file_path = 'data.csv'

# Definir a propriedade max_rows para 9999
pd.set_option('display.max_rows', 9999)

# Leia o conteúdo do arquivo CSV com o separador correto
data = pd.read_csv(csv_file_path, sep=';', engine='python', encoding='utf-8')

# Imprima informações gerais sobre o conjunto de dados
print("Informações gerais sobre o conjunto de dados:")
data_info = data.info()

# Imprima o total de linhas
total_linhas = data.shape[0]
print(f"\nTotal de linhas: {total_linhas}")

# Imprima o total de colunas
total_colunas = data.shape[1]
print(f"Total de colunas: {total_colunas}")

# Imprima a quantidade de dados nulos, se existirem
print("\nQuantidade de dados nulos por coluna:")
print(data.isnull().sum())

# Imprima o tipo de dado de cada coluna
print("\nTipos de dados de cada coluna:")
print(data.dtypes)

# Imprima a quantidade de memória utilizada pelo conjunto de dados
print("\nQuantidade de memória utilizada pelo conjunto de dados:")
print(data.memory_usage(deep=True))