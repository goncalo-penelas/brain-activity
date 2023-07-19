# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:40:29 2022

@author: tiago
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

df = pd.read_csv("all_data.csv")

funcao = {"Movimento" : [1,2,19,20,25,26,69,70,71,72,73,74,75,76],
          "Memória" : [3,4,5,6,23,24,35,36,37,38,39,67,68,81,85,86,87,88],
          "Processamento de linguagem do cérebro" : [9,10,15,16,61],
          "Fala" : [11,12,13,14],
          "Paladar" : [17,18,29,30,77,78],
          "Olfato" : [21,22,77,78],
          "Emoções" : [31,32,33,34,41,42],
          "Visão" : [43,44,45,46,47,48,51,52,77,78],
          "Reconhecimento" : [49,50,53,54,55,56,89,90],
          "Tato" : [57,58,77,78],
          "Audição" : [63,77,78,79,80,82,83,84]
          }

def line_col(x):
    return x//90, x-(90*(x//90))

# conexoes = []
# for elem in df.drop(["index", "education", "sex", "age"], axis=1):
#     (a,b) = line_col(int(elem))
#     if (b,a) in conexoes or a == b:
#         df.drop(elem, axis=1, inplace=True)
#     else:
#         conexoes.append((a,b))


# df.to_csv("all_data_simple.csv", index=False)


data = {}
data["M"] = df[df["sex"] == 0]
data["F"] = df[df["sex"] == 1]


graphic = {}

for func in funcao.keys():
    print(func + " M")
    graphic[func] = ({int(idade) : 0 for idade in df["age"].unique()}, {int(idade) : 0 for idade in df["age"].unique()})
    for elem in data["M"].drop(["index", "education", "sex", "age"], axis=1):
        zona, _ = line_col(int(elem))
        if zona in funcao[func]:
            for idade in df["age"].unique():
                graphic[func][0][idade] += data["M"][data["M"]["age"] == idade][str(zona)].sum()
    print(func + " F")
    for elem in data["F"].drop(["index", "education", "sex", "age"], axis=1):
        zona, _ = line_col(int(elem))
        if zona in funcao[func]:
            for idade in df["age"].unique():
                graphic[func][1][idade] += data["F"][data["F"]["age"] == idade][str(zona)].sum()




def makeGraphic(data, title):
    # Change the style of plot
    plt.style.use('seaborn-darkgrid')
     
    # Create a color palette
    palette = plt.get_cmap('Set1')
    
    num = 0
    for elem in data:
        elem = dict(sorted(elem.items()))
        num += 1
        if num == 1:
            plt.plot(elem.keys(), elem.values(), marker='', color=palette(num), linewidth=1, alpha=0.9, label = "Masculino")
        else:
            plt.plot(elem.keys(), elem.values(), marker='', color=palette(num), linewidth=1, alpha=0.9, label = "Feminino")
    
    # Add legend
    plt.legend(loc=2, ncol=2)
     
    # Add titles
    plt.title(title, loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Idade")
    plt.ylabel("Ligações")

    
    plt.savefig('Gráficos/Brain_' + title + '.png')
    plt.show()
    
 

for func in graphic.keys():
    makeGraphic(graphic[func], func)