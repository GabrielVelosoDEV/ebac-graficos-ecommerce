import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho absoluto do arquivo
caminho_arquivo = r"C:\Users\Administrator\Documents\Estudos_Python\ecommerce_estatistica.csv"

# Carregar o arquivo CSV
data = pd.read_csv(caminho_arquivo)

# Exibir os nomes das colunas para verificar
print("Colunas disponíveis no dataset:", data.columns)

# Limpeza da coluna 'Qtd_Vendidos' para remover símbolos e convertê-la para numérico
data['Qtd_Vendidos'] = data['Qtd_Vendidos'].replace({'mil': '000'}, regex=True)
data['Qtd_Vendidos'] = data['Qtd_Vendidos'].replace({'\+': ''}, regex=True)  # Remove o '+'
data['Qtd_Vendidos'] = pd.to_numeric(data['Qtd_Vendidos'], errors='coerce')  # Converte para número

# Configuração geral para gráficos
plt.style.use('ggplot')  # Estilo de gráfico

# Histograma - Distribuição de Notas
plt.figure(figsize=(10, 6))
sns.histplot(data['Nota'], bins=15, kde=True, color='skyblue')
plt.title('Distribuição de Notas dos Produtos', fontsize=16)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.show()

# Gráfico de dispersão - Preço vs. Avaliações
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Preço', y='N_Avaliações', data=data, hue='Marca', palette='viridis')
plt.title('Dispersão: Preço vs Avaliações', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Número de Avaliações', fontsize=12)
plt.legend(title='Marca')
plt.show()

# Mapa de calor - Correlação entre variáveis numéricas
plt.figure(figsize=(10, 8))
correlacao = data[['Nota', 'Preço', 'Qtd_Vendidos', 'N_Avaliações']].corr()
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Mapa de Calor das Correlações', fontsize=16)
plt.show()

# Gráfico de barra - Média de preço por Material
plt.figure(figsize=(10, 6))
media_preco_material = data.groupby('Material')['Preço'].mean().sort_values()
sns.barplot(x=media_preco_material.values, y=media_preco_material.index, palette='pastel')
plt.title('Média de Preço por Material', fontsize=16)
plt.xlabel('Preço Médio', fontsize=12)
plt.ylabel('Material', fontsize=12)
plt.show()

# Gráfico de pizza - Proporção de Vendas por Gênero
plt.figure(figsize=(8, 8))
vendas_por_genero = data['Gênero'].value_counts()
plt.pie(vendas_por_genero, labels=vendas_por_genero.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Proporção de Vendas por Gênero', fontsize=16)
plt.show()

# Gráfico de densidade - Densidade do preço
plt.figure(figsize=(10, 6))
sns.kdeplot(data['Preço'], shade=True, color='blue')
plt.title('Densidade do Preço dos Produtos', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.show()

# Gráfico de regressão - Preço vs Quantidade Vendida
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Qtd_Vendidos', data=data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Regressão: Preço vs Quantidade Vendida', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.show()
