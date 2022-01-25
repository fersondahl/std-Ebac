import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


gas_df = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):

  fig = plt.subplots(figsize=(30/2.4, 20/2.4))
  
  grafico = sns.lineplot(data=gas_df, x='dia', y='venda', color='darkcyan', linewidth=2)
  grafico.set_title('Preço da gasolina por dia', fontdict={"fontsize": 16, 'color': 'black'})

  grafico.set(ylabel="Preço de venda", xlabel='Dia')


  fig_png = grafico.get_figure()
  fig_png.savefig('gasolina.png')