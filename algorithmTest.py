import fileWriteReadParser
from datetime import datetime

is_record_genome = True


def get_date_time_now():
    now = datetime.now()
    # dd/mm/YY H:M:S
    return now.strftime("%d/%m/%Y %H:%M:%S")


def algorithm_analysis_data_schema(genome, strain, gLength, dLength, genome_file_type, time_executed, method,
                                   comparison, positions):
    if is_record_genome:
        data = {
            "genome": genome,
            "genome_length": gLength,
            "dna_strain": strain,
            "dna_strain_length": dLength,
            "genome_file_type": genome_file_type,
            "time_executed": time_executed,
            "method": method,
            "comparison": comparison,
            "matches": len(positions),
            "position found": positions
        }
    else:
        data = {
            "genome": "fna file",
            "genome_length": gLength,
            "dna_strain": strain,
            "dna_strain_length": dLength,
            "genome_file_type": "fna",
            "time_executed": time_executed,
            "method": method,
            "comparison": comparison,
            "matches": len(positions),
            "position found": positions
        }
    return data


# algorithm_analysis_data_schema(genome, strain, gLength, dLength, genome_file_type,
# time_executed, method, time_complexity, positions)
def front_back_search(genome, dnaStrain):
    position = []
    gLength = len(genome)
    dLength = len(dnaStrain)
    comparison = 0
    i = 0
    if dLength == 0:
        return
    while i < gLength:
        succession = 0
        comparison += 1
        if dLength + i >= gLength:
            break
        #Check if Dna strain is a letter
        if dLength == 1 and genome[i] == dnaStrain:
            comparison += 1
            position.append(i)
        # Check last letter of dna_strain in genome
        comparison += 1
        if dnaStrain[dLength - 1] == genome[i + dLength - 1]:
            succession += 1
            comparison += 1
            # Check first letter of dna_strain in genome
            if dnaStrain[0] == genome[i]:
                succession += 1
                # Check all the middle letters
                for j in range(1, dLength - 1):
                    comparison += 1
                    if dnaStrain[j] == genome[i + j]:
                        succession += 1
                    else:
                        break
                comparison += 1
                if succession == dLength:
                    position.append(i)
                    i += dLength
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1

    fileWriteReadParser.write_data_json_file(
        algorithm_analysis_data_schema(genome, dnaStrain, len(genome), len(dnaStrain), "raw", get_date_time_now(),
                                       "Front Back Search",
                                       comparison, position))


def brute_force_search(genome, dnaStrain):
    position = []
    gLength = len(genome)
    dLength = len(dnaStrain)
    comparison = 0
    for i in range(0, gLength):
        succession = 0
        comparison += 1
        for j in range(0, dLength):
            comparison += 1
            if i + j < gLength:
                if genome[i + j] == dnaStrain[j]:
                    comparison += 1
                    succession += 1
            else:
                break
        if succession == dLength:
            position.append(i)

    fileWriteReadParser.write_data_json_file(
        algorithm_analysis_data_schema(genome, dnaStrain, len(genome), len(dnaStrain), "raw", get_date_time_now(),
                                       "Brute Force Search",
                                       comparison, position))
