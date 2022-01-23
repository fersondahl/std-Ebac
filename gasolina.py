import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gas_df = pd.read_csv('/content/std-Ebac/gasolina.csv')



with sns.axes_style('whitegrid'):

  fig = plt.subplots(figsize=(30/2.4, 20/2.4))

  grafico = sns.lineplot(data=gas_df, x='dia', y='venda', color='darkcyan')
  grafico.set_title('Preço da gasolina por dia', fontdict={'fontsize': 16})

  fig_png = grafico.get_figure()
  fig_png.savefig('gasolina.png')