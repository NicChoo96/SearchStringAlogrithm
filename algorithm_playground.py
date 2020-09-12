import random
import tkinter as tk
import brute_force as bfs
import boyer_moore as bms
import front_back as fbs
import algorithm_data_formatter as data_formatter
import fileWriteReadParser as file_parser

use_genome_file = False
# 0 - Brute Force, 1 - Front Back
algorithm_selector = 0
random_genome_length = 400000
min_strain_length = 4
max_strain_length = 20
text_output = tk
root = tk

genome_run_file = ["brute_force.json", "front_back.json", "boyer_moore.json"]
genome_run_file_single = ["brute_force_single_test.json", "front_back_single_test.json", "boyer_moore_single_test.json"]
multi_run_file = ["BFS_rand.json", "FBS_rand.json", "boyer_moore_rand.json"]
multi_run_file_single = ["BFS_rand_single_test.json", "FBS_rand_single_test.json", "boyer_moore_rand_single_test.json"]
file_parser.genome_file_name = "GCF_000195955.2_ASM19595v2_genomic.fna"


def random_generate_string(length):
    randStr = ""
    letters = ["A", "T", "C", "G"]

    for i in range(0, length):
        randStr += letters[random.randint(0, len(letters) - 1)]
    return randStr


def algorithmRun(genome, dnaStrain):
    if algorithm_selector == 0:
        bfs.search(genome, dnaStrain)
    elif algorithm_selector == 1:
        fbs.search(genome, dnaStrain)
    elif algorithm_selector == 2:
        bms.search(genome, dnaStrain)


def run_multiple_test(genomeLength, dna_strain):
    genome = random_generate_string(genomeLength)
    algorithmRun(genome, dna_strain)


def run_genome_test(dnaStrain):
    genome = file_parser.open_genome_file()
    data_formatter.is_record_genome = False
    algorithmRun(genome, dnaStrain)


def getAlgoName():
    if algorithm_selector == 0:
        return "Brute Force"
    elif algorithm_selector == 1:
        return "Front Back"
    elif algorithm_selector == 2:
        return "Boyer's Moore"


def main_test():
    print_gui(getAlgoName() + " test run Started")
    if use_genome_file:
        file_parser.clear_data_file(genome_run_file[algorithm_selector])
        file_parser.file_name = genome_run_file[algorithm_selector]
        for i in range(min_strain_length, max_strain_length + 1):
            dna_strain = random_generate_string(i)
            run_genome_test(dna_strain)
            print_gui(str(((i - 4) / (max_strain_length - min_strain_length)) * 100) + "%")
    else:
        file_parser.clear_data_file(multi_run_file[algorithm_selector])
        file_parser.file_name = multi_run_file[algorithm_selector]
        for i in range(min_strain_length, max_strain_length + 1):
            dna_strain = random_generate_string(i)
            run_multiple_test(random_genome_length, dna_strain)
            print_gui(str(((i - 4) / (max_strain_length - min_strain_length)) * 100) + "%")
    print_gui(getAlgoName() + " test run Completed")
    print_gui("Output File: " + file_parser.file_name)


def single_test_run(dna_strain):
    print_gui(getAlgoName() + " single test run Started")
    if use_genome_file:
        file_parser.clear_data_file(genome_run_file_single[algorithm_selector])
        file_parser.file_name = genome_run_file_single[algorithm_selector]
        run_genome_test(dna_strain)
    else:
        file_parser.clear_data_file(multi_run_file_single[algorithm_selector])
        file_parser.file_name = multi_run_file_single[algorithm_selector]
        run_multiple_test(random_genome_length, dna_strain)
    print_gui(getAlgoName() + " single test run Completed")
    print_gui("Output File: " + file_parser.file_name)


def print_gui(new_text):
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, new_text + "\n")
    text_output.config(state=tk.DISABLED)
    root.update()
    print(new_text)
