import pandas as pd
import numpy as np

# Defina o caminho do arquivo CSV
csv_file_path = 'data.csv'

# Leia o conteúdo do arquivo CSV com o separador correto
data = pd.read_csv(csv_file_path, sep=';', engine='python', encoding='utf-8')

# Imprima informações gerais sobre o conjunto de dados
print("Informações gerais sobre o conjunto de dados:")
data.info()

# Imprima as primeiras N linhas do conjunto de dados
N = 5
print(f"\nPrimeiras {N} linhas do conjunto de dados:")
print(data.head(N).to_string(index=False))

# Imprima as últimas N linhas do conjunto de dados
print(f"\nÚltimas {N} linhas do conjunto de dados:")
print(data.tail(N).to_string(index=False))

# Crie uma nova variável contendo uma cópia do conjunto de dados original
copied_data = data.copy()

# Substitua todos os valores nulos da coluna 'Calories' por 0
copied_data = copied_data.assign(Calories=copied_data['Calories'].fillna(0))

# Imprima o conjunto de dados para verificar se a mudança foi aplicada com sucesso
print(
  "\nConjunto de dados após substituir valores nulos da coluna 'Calories' por 0:")
print(copied_data.to_string(index=False))

# Substitua os valores nulos da coluna 'Date' por '1900/01/01'
copied_data = copied_data.assign(Date=copied_data['Date'].fillna('1900/01/01'))

# Imprima o conjunto de dados para verificar se a mudança foi aplicada com sucesso
print(
  "\nConjunto de dados após substituir valores nulos da coluna 'Date' por '1900/01/01':")
print(copied_data.to_string(index=False))

# Substitua '1900/01/01' por NaN e transforme a coluna 'Date' para datetime
copied_data = copied_data.assign(
  Date=copied_data['Date'].replace("1900/01/01", np.nan))

# Tente transformar a coluna 'Date' para datetime
print("\nTentativa de transformação para datetime:")
copied_data['Date'] = pd.to_datetime(copied_data['Date'], format="%Y/%m/%d")

# Imprima o conjunto de dados para verificar se a mudança foi aplicada com sucesso
print(copied_data.to_string(index=False))

# Corrija o formato especifico do valor '20201226'
copied_data['Date'] = copied_data['Date'].replace('20201226', '2020-12-26')

# Tente novamente transformar a coluna 'Date' para datetime
copied_data['Date'] = pd.to_datetime(copied_data['Date'])

# Imprima o conjunto de dados para verificar se as mudanças foram aplicadas com sucesso
print("\nConjunto de dados após transformação para datetime:")
print(copied_data.to_string(index=False))

# Remova os registros contendo valores nulos na coluna 'Date'
cleaned_data = copied_data.dropna(subset=['Date'])

# Imprima o conjunto de dados final para verificar se todas as transformações foram executadas com sucesso
print("\nConjunto de dados final após remoção de valores nulos na coluna 'Date':")
print(cleaned_data.to_string(index=False))
