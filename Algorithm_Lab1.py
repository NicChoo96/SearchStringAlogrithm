import fileWriteReadParser
from datetime import datetime
import random

# https://pypi.org/project/fastaparser/

# dna_string = fileWriteReadParser.open_genome_file()

# print(dna_string)

timeComplexity = 0


def algorithm_analysis_data_schema(genome, strain, genome_file_type, time_executed, method, time_complexity, positions):
    data = {
        "genome": genome,
        "genome_length": len(genome),
        "dna_strain": strain,
        "dna_strain_length": len(strain),
        "genome_file_type": genome_file_type,
        "time_executed": time_executed,
        "method": method,
        "time_complexity": time_complexity,
        "position found": positions
    }
    return data


# algorithm_analysis_data_schema("abc", "abc", "fna", 0, "Brute Force", 0, [1,2,3])

def brute_force_search(genome, dnaStrain):
    position = []
    global timeComplexity
    gLength = len(genome)
    dLength = len(dnaStrain)
    succession = 0
    print("Genome Length: " + str(gLength))
    print("DNA Length: " + str(dLength))

    for i in range(0, gLength):
        succession = 0
        timeComplexity += 1
        for j in range(0, dLength):
            timeComplexity += 1
            if i + j < gLength:
                if genome[i + j] == dnaStrain[j]:
                    timeComplexity += 1
                    succession += 1
            else:
                break
        if succession == dLength:
            timeComplexity += 1
            position.append(i)
    return position


def random_generate_string(length):
    randStr = ""
    letters = ["A", "T", "C", "G"]

    for i in range(0, length):
        randStr += letters[random.randint(0, len(letters) - 1)]
    return randStr


def run_test(genomeLength, dnaLength):
    global timeComplexity
    dnaStrain = random_generate_string(dnaLength)
    genome = random_generate_string(genomeLength)

    position = []
    position = brute_force_search(genome, dnaStrain)

    print("Position Found: ")
    for i in range(0, len(position)):
        print(str(position[i]) + " ")

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # algorithm_analysis_data_schema(genome, strain, genome_file_type, time_executed, method, time_complexity, positions)
    fileWriteReadParser.write_data_json_file(
        algorithm_analysis_data_schema(genome, dnaStrain, "raw", dt_string, "Brute Force", timeComplexity, position))

    print("Time Complexity: " + str(timeComplexity) + "\n")
    print("Dna Strain:" + dnaStrain + "\n")
    print("Position Size: " + str(len(position)) + "\n")


def main():
    for i in range(1, 40):
        run_test(i * 10, i % 10)
    # fileWriteReadParser.read_data_json_file()





main()
