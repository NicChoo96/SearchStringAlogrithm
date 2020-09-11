from python_src import algorithm_data_formatter, fileWriteReadParser


def search(genome, dnaStrain):
    position = []
    g_length = len(genome)
    d_length = len(dnaStrain)
    comparison = 0
    i = 0
    if d_length == 0:
        return
    while i < g_length:
        succession = 0
        comparison += 1
        if d_length + i >= g_length:
            break
        # Check if Dna strain is a letter
        if d_length == 1 and genome[i] == dnaStrain:
            comparison += 1
            position.append(i)
        # Check last letter of dna_strain in genome
        comparison += 1
        if dnaStrain[d_length - 1] == genome[i + d_length - 1]:
            succession += 1
            comparison += 1
            # Check first letter of dna_strain in genome
            if dnaStrain[0] == genome[i]:
                succession += 1
                # Check all the middle letters
                for j in range(1, d_length - 1):
                    comparison += 1
                    if dnaStrain[j] == genome[i + j]:
                        succession += 1
                    else:
                        break
                comparison += 1
                if succession == d_length:
                    position.append(i)
                    i += d_length
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1

    fileWriteReadParser.write_data_json_file(
        algorithm_data_formatter.algorithm_analysis_data_schema(genome, dnaStrain, g_length, d_length,
                                                                "raw",
                                                                algorithm_data_formatter.get_date_time_now(),
                                                                "Front Back Search",
                                                                comparison, position))
