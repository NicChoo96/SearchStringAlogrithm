import json
import fastaparser
import os.path

file_name = "data2.json"
genome_file_name = "GCF_000195955.2_ASM19595v2_genomic.fna"
override_data = False


def read_data_json_file():
    with open(file_name) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=1, sort_keys=True))


def get_json_data():
    if os.path.isfile('./'+file_name):
        with open(file_name) as json_file:
            return json.load(json_file)['run_history']


def write_data_json_file(records):
    data = {}
    data['run_history'] = []
    # Load in existing file record
    if not override_data:
        if os.path.isfile('./' + file_name):
            with open(file_name) as json_file:
                f_data = json.load(json_file)
                if len(f_data) != 0:
                    data = f_data
    data['run_history'].append(records)

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


def open_genome_file():
    dna_string = ""
    with open(genome_file_name) as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            dna_string += seq.sequence_as_string()
    return dna_string
