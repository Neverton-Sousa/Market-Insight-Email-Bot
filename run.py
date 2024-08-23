#importar as bibliotecas
import pandas as pd

emails = pd.read_excel(r"Bases de Dados\Emails.xlsx")
lojas = pd.read_csv(r'Bases de Dados\Lojas.csv')
vendas = pd.read_excel(r'Bases de Dados\Vendas.xlsx')

display(emails)