import fileWriteReadParser
from datetime import datetime
import random
import app_gui

# https://pypi.org/project/fastaparser/

# dna_string = fileWriteReadParser.open_genome_file()

# print(dna_string)

timeComplexity = 0


def algorithm_analysis_data_schema(genome, strain, gLength, dLength, genome_file_type, time_executed, method,
                                   time_complexity, positions):
    data = {
        "genome": genome,
        "genome_length": gLength,
        "dna_strain": strain,
        "dna_strain_length": dLength,
        "genome_file_type": genome_file_type,
        "time_executed": time_executed,
        "method": method,
        "time_complexity": time_complexity,
        "position found": positions
    }
    return data


# algorithm_analysis_data_schema("abcd", "abc", 4, 3, "fna", 0, "Brute Force", 0, [1,2,3])


def algo_method(genome, dnaStrain):
    position = []
    global timeComplexity
    gLength = len(genome)
    dLength = len(dnaStrain)
    succession = 0
    timeComplexity = 0
    print("Genome: " + genome)
    print("DNA Strain: " + dnaStrain)
    print("Genome Length: " + str(gLength))
    print("DNA Length: " + str(dLength))
    if dLength == 0:
        return position
    for i in range(0, gLength):
        succession = 0
        timeComplexity += 1
        if dLength + i == gLength:
            return position
        # Check last letter of dna_strain in genome
        if dnaStrain[dLength - 1] == genome[i+dLength-1]:
            succession += 1
            timeComplexity += 1
            # Check first letter of dna_strain in genome
            if dnaStrain[0] == genome[i]:
                succession += 1
                timeComplexity += 1
                # Check all the middle letters
                for j in range(1, dLength-1):
                    timeComplexity += 1
                    if dnaStrain[j] == genome[i + j]:
                        succession += 1
                    else:
                        break
                if succession == dLength:
                    position.append(i)
    return position


def brute_force_search(genome, dnaStrain):
    position = []
    global timeComplexity
    gLength = len(genome)
    dLength = len(dnaStrain)
    succession = 0
    timeComplexity = 0
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
    # dnaStrain = random_generate_string(dnaLength)
    dnaStrain = "ACG"
    genome = random_generate_string(genomeLength)

    position = []
    #position = brute_force_search(genome, dnaStrain)
    position = algo_method(genome, dnaStrain)
    print("Position Found: ")
    for i in range(0, len(position)):
        print(str(position[i]) + " ")

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # algorithm_analysis_data_schema(genome, strain, gLength, dLength, genome_file_type, time_executed, method, time_complexity, positions)
    fileWriteReadParser.write_data_json_file(
        algorithm_analysis_data_schema(genome, dnaStrain, len(genome), len(dnaStrain), "raw", dt_string, "Algo",
                                       timeComplexity, position))

    # fileWriteReadParser.write_data_json_file(
    #    algorithm_analysis_data_schema("", "", len(genome), len(dnaStrain), "raw", dt_string, "Brute Force", timeComplexity, position))

    print("Time Complexity: " + str(timeComplexity) + "\n")
    print("Dna Strain:" + dnaStrain + "\n")
    print("Position Size: " + str(len(position)) + "\n")


# run_test(20, 2)


def main():
    for i in range(1, 50):
        run_test((i * 10), 5)
    # fileWriteReadParser.read_data_json_file()


# main()
app_gui.show_chart()
