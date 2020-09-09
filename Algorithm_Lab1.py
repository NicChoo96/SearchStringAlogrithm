import random
import app_gui
import warnings
import algorithmTest
import fileWriteReadParser

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

is_genome_file = True
algorithmSelector = 0
front_back_file = "front_back.json"
brute_force_file = "brute_force.json"


def random_generate_string(length):
    randStr = ""
    letters = ["A", "T", "C", "G"]

    for i in range(0, length):
        randStr += letters[random.randint(0, len(letters) - 1)]
    return randStr


def algorithmRun(genome, dnaStrain):
    if algorithmSelector == 0:
        fileWriteReadParser.file_name = brute_force_file
        algorithmTest.brute_force_search(genome, dnaStrain)
    elif algorithmSelector == 1:
        fileWriteReadParser.file_name = front_back_file
        algorithmTest.front_back_search(genome, dnaStrain)


def run_multiple_test(genomeLength, dnaLength):
    # dnaStrain = random_generate_string(dnaLength)
    dnaStrain = "ATGC"
    genome = random_generate_string(genomeLength)
    algorithmRun(genome, dnaStrain)


def run_genome_test():
    dnaStrain = "ATGC"
    genome = fileWriteReadParser.open_genome_file()
    algorithmTest.is_record_genome = False
    algorithmRun(genome, dnaStrain)


def main():
    if algorithmSelector == 0:
        fileWriteReadParser.clear_data_file(brute_force_file)
    elif algorithmSelector == 1:
        fileWriteReadParser.clear_data_file(front_back_file)

    if is_genome_file:
        run_genome_test()
    else:
        for i in range(1, 100):
            run_multiple_test((i * 10), 5)

#main()
