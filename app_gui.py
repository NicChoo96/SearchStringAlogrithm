import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import fileWriteReadParser
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Algorithm_Lab1
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")


def get_chart_data(fname):
    json_data = fileWriteReadParser.get_json_data(fname)
    tc = []
    gl = []
    for i in range(0, len(json_data)):
        gl.append(json_data[i]['dna_strain_length'])
        tc.append(json_data[i]['comparison'])
    x = np.array(gl)
    y = np.array(tc)
    x = np.sort(x)
    y = np.sort(y)

    data = {'Strain_Length': x,
            'Comparison': y
            }
    return data


def show_chart():
    files = Algorithm_Lab1.genome_run_file

    root = tk.Tk()
    for i in range(0, len(files)):
        df = DataFrame(get_chart_data(files[i]), columns=['Strain_Length', 'Comparison'])
        if i == 0:
            figure = plt.Figure(figsize=(5, 4), dpi=100)
            ax = figure.add_subplot(111)
            ax.set_title(files[i])
            ax.set_ylim(bottom=0)
            ax.set_ylim(top=100000000)
            line = FigureCanvasTkAgg(figure, root)
            line.get_tk_widget().pack(side=tk.LEFT, expand=False)
        df = df[['Strain_Length', 'Comparison']].groupby('Strain_Length').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r', marker='', fontsize=10)
        
    for i in range(0, len(files)):
        df = DataFrame(get_chart_data(files[i]), columns=['Strain_Length', 'Comparison'])
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        ax.set_title(files[i])
        line = FigureCanvasTkAgg(figure, root)
        line.get_tk_widget().pack(side=tk.LEFT, expand=True)
        df = df[['Strain_Length', 'Comparison']].groupby('Strain_Length').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r', marker='', fontsize=10)

    root.mainloop()


show_chart()
# root = tk.Tk()


# root.mainloop()
