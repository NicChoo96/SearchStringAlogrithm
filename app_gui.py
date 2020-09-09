import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import fileWriteReadParser
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def get_chart_data(fname):
    json_data = fileWriteReadParser.get_json_data(fname)
    tc = []
    gl = []
    for i in range(0, len(json_data)):
        tc.append(json_data[i]['comparison'])
        gl.append(json_data[i]['genome_length'])
    x = np.array(gl)
    y = np.array(tc)
    x = np.sort(x)
    y = np.sort(y)

    data = {'Genome_Length': x,
            'Comparison': y
            }
    return data


def show_chart():
    df1 = DataFrame(get_chart_data('data.json'), columns=['Genome_Length', 'Comparison'])
    df2 = DataFrame(get_chart_data('data2.json'), columns=['Genome_Length', 'Comparison'])

    root = tk.Tk()

    figure1 = plt.Figure(figsize=(4, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().pack(side=tk.LEFT,expand=True)
    df1 = df1[['Genome_Length', 'Comparison']].groupby('Genome_Length').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
    ax1.set_title('BFS')

    figure2 = plt.Figure(figsize=(4, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, expand=True)
    df2 = df2[['Genome_Length', 'Comparison']].groupby('Genome_Length').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('FBS')

    plt.ylim(0, 3000)

    root.mainloop()


show_chart()
