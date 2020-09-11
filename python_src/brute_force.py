from python_src import algorithm_data_formatter, fileWriteReadParser


def search(genome, dna_strain):
    position = []
    g_length = len(genome)
    d_length = len(dna_strain)
    comparison = 0
    # Loop through every single letter in the genome
    for i in range(0, g_length):
        succession = 0
        comparison += 1
        # Loop through every single letter in dna_strain
        for j in range(0, d_length):
            comparison += 1
            if i + j < g_length:
                if genome[i + j] == dna_strain[j]:
                    comparison += 1
                    succession += 1
            else:
                break
        if succession == d_length:
            position.append(i)

    fileWriteReadParser.write_data_json_file(
        algorithm_data_formatter.algorithm_analysis_data_schema(genome, dna_strain, g_length,
                                                                d_length, "raw",
                                                                algorithm_data_formatter.get_date_time_now(),
                                                                "Brute Force Search",
                                                                comparison, position))
