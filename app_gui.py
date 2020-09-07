import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import fileWriteReadParser
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_chart():
    json_data = fileWriteReadParser.get_json_data()

    tc = []
    gl = []

    for i in range(0, len(json_data)):
        tc.append(json_data[i]['time_complexity'])
        gl.append(json_data[i]['genome_length'])

    x = np.array(gl)
    y = np.array(tc)

    x = np.sort(x)
    y = np.sort(y)


    data2 = {'Genome_Length': x,
             'Time_Complexity': y
             }
    df2 = DataFrame(data2, columns=['Genome_Length', 'Time_Complexity'])

    root = tk.Tk()

    figure2 = plt.Figure(figsize=(5, 4), dpi=200)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Genome_Length', 'Time_Complexity']].groupby('Genome_Length').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Algo Genome_Length Vs. Time_Complexity')

    root.mainloop()

# show_chart()
