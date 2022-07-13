import pandas as pd
import seaborn as sns

fonte = pd.read_csv('gasolina.csv', sep=',')


with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=fonte, x="dia", y="venda", palette="Set2")
  grafico.set(title='Preço da gasolina por dia', xlabel=' Dia', ylabel='Preçco em reais');

grafico.figure.savefig(fname="gasolina.png", bbox_inches="tight")