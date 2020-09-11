import random
import algorithmTest
import fileWriteReadParser
import project1_boyermoore

use_genome_file = True
# 0 - Brute Force, 1 - Front Back
algorithm_selector = 2
min_random_genome_length = 400000
min_strain_length = 4
max_strain_length = 20

genome_run_file = ["brute_force.json", "front_back.json", "boyer_moore.json"]
multi_run_file = ["BFS_rand.json", "FBS_rand.json", "boyer_moore_rand.json"]
all_file = ["brute_force.json", "front_back.json", "BFS_rand.json", "FBS_rand.json", "data.json", "data2.json"]
fileWriteReadParser.genome_file_name = "GCF_000195955.2_ASM19595v2_genomic.fna"


def random_generate_string(length):
    randStr = ""
    letters = ["A", "T", "C", "G"]

    for i in range(0, length):
        randStr += letters[random.randint(0, len(letters) - 1)]
    return randStr


def algorithmRun(genome, dnaStrain):
    if algorithm_selector == 0:
        algorithmTest.brute_force_search(genome, dnaStrain)
    elif algorithm_selector == 1:
        algorithmTest.front_back_search(genome, dnaStrain)
    elif algorithm_selector == 2:
        project1_boyermoore.boyermooresearch(genome, dnaStrain)


def run_multiple_test(genomeLength, dnaLength):
    dnaStrain = random_generate_string(dnaLength)
    genome = random_generate_string(genomeLength)
    algorithmTest.is_record_genome = False
    algorithmRun(genome, dnaStrain)


def run_genome_test(dnaLength):
    genome = fileWriteReadParser.open_genome_file()
    dnaStrain = random_generate_string(dnaLength)
    algorithmTest.is_record_genome = False
    algorithmRun(genome, dnaStrain)


def main():
    print("Test run Started")
    if use_genome_file:
        fileWriteReadParser.clear_data_file(genome_run_file[algorithm_selector])
        fileWriteReadParser.file_name = genome_run_file[algorithm_selector]
        for i in range(min_strain_length, max_strain_length + 1):
            run_genome_test(i)
            print(str(((i - 4) / (max_strain_length - min_strain_length)) * 100) + "%")
    else:
        fileWriteReadParser.clear_data_file(multi_run_file[algorithm_selector])
        fileWriteReadParser.file_name = multi_run_file[algorithm_selector]
        for i in range(min_strain_length, max_strain_length + 1):
            run_multiple_test(min_random_genome_length, i)
            print(str(((i - 4) / (max_strain_length - min_strain_length)) * 100) + "%")
    print("Test run Completed")


#main()
