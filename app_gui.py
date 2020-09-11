import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import fileWriteReadParser
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Algorithm_Lab1
import json


def get_chart_data(fname):
    json_data = fileWriteReadParser.get_json_data(fname)
    tc = []
    gl = []
    for i in range(0, len(json_data)):
        gl.append(json_data[i]['dna_strain_length'])
        tc.append(json_data[i]['comparison'])
    x = np.array(gl)
    y = np.array(tc)

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
            ax.set_title("BruteForce vs FrontBack")
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


root = tk.Tk()


def generate_algorithm():
    Algorithm_Lab1.main()


def show_file():
    data = fileWriteReadParser.get_json_data(Lb1.get(tk.ANCHOR))
    # data = data[['genome', 'genome_length', 'dna_strain', 'dna_strain_length', 'time_executed', 'method', 'comparison', 'matches']]
    text.configure(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, json.dumps(data, indent=1, sort_keys=True))
    text.configure(state=tk.DISABLED)


# show_chart()
var = tk.StringVar()
generate_algorithm_button = tk.Button(root, text="Process Algorithm", command=generate_algorithm)
show_file_button = tk.Button(root, text="Show File", command=show_file)
show_chart_button = tk.Button(root, text="Show Chart", command=show_chart)

text = tk.Text(root, state=tk.DISABLED)

scroll = tk.Scrollbar(root)
text.pack()

scroll.pack(side=tk.RIGHT, fill=tk.Y)
scroll.config(command=text.yview)

generate_algorithm_button.pack()
show_file_button.pack()
show_chart_button.pack()


def selectAlgo0():
    Algorithm_Lab1.algorithm_selector = 0


def selectAlgo1():
    Algorithm_Lab1.algorithm_selector = 1


def toggleGenome():
    if Algorithm_Lab1.use_genome_file:
        Algorithm_Lab1.use_genome_file = False
    else:
        Algorithm_Lab1.use_genome_file = True


def main_gui():
    root = tk.Tk()

    var = tk.IntVar()
    R1 = tk.Radiobutton(root, text="Brute Force", variable=var, value=1,
                        command=selectAlgo0)
    R1.pack(anchor=tk.W, side=tk.LEFT)
    R1.select()

    R2 = tk.Radiobutton(root, text="Front Back", variable=var, value=2,
                        command=selectAlgo1)
    R2.pack(anchor=tk.W, side=tk.LEFT)

    CheckVar1 = tk.IntVar()
    C1 = tk.Checkbutton(root, text="Use Genome File", variable=CheckVar1,
                        onvalue=1, offvalue=0, height=5,
                        width=20, command=toggleGenome)
    C1.pack(side=tk.LEFT)

    dnaStrain_label = tk.Label(root, text="DNA Strain")
    dnaStrain_label.pack(side=tk.LEFT)
    dnaStrain_entry = tk.Entry(root, bd=5)
    dnaStrain_entry.pack(side=tk.LEFT)

    file_label = tk.Label(root, text="File Name")
    file_label.pack(side=tk.LEFT)

    Lb1 = tk.Listbox(root, selectmode=tk.SINGLE)
    for i in range(1, len(Algorithm_Lab1.all_file)):
        Lb1.insert(i, Algorithm_Lab1.all_file[i])

    Lb1.pack()

    root.mainloop()


# main_gui()

def show_chart_single():
    files = "boyer_moore.json"

    root = tk.Tk()

    df = DataFrame(get_chart_data(files), columns=['Strain_Length', 'Comparison'])
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.set_title(files)
    line = FigureCanvasTkAgg(figure, root)
    line.get_tk_widget().pack(side=tk.LEFT, expand=True)
    df = df[['Strain_Length', 'Comparison']].groupby('Strain_Length').sum()
    df.plot(kind='line', legend=True, ax=ax, color='r', marker='', fontsize=10)

    root.mainloop()


show_chart_single()
