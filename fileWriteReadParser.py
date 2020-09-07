import json
import fastaparser
import os.path


def read_data_json_file():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=1, sort_keys=True))


def get_json_data():
    if os.path.isfile('./data.json'):
        with open('data.json') as json_file:
            return json.load(json_file)['run_history']


def write_data_json_file(records):
    data = {}
    data['run_history'] = []
    # Load in existing file record
    if os.path.isfile('./data.json'):
        with open('data.json') as json_file:
            f_data = json.load(json_file)
            if(len(f_data) != 0):
                data = f_data
    data['run_history'].append(records)
    """
    data['run_history'].append({
        'genome': 'ATCGATCG',
        'strain': 'ATCG',
        'genome_file_type': 'raw',
        'time_executed': 'Today',
        'method': 'Brute Force',
        'time_complexity': 0
    })
    data['run_history'].append({
        'genome': 'GCF_000195955.2_ASM19595v2_genomic.fna',
        'strain': 'ATCG',
        'genome_file_type': 'fna',
        'time_executed': 'Today',
        'method': 'Brute Force',
        'time_complexity': 0
    })
    """

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def open_genome_file():
    dna_string = ""
    with open("GCF_000195955.2_ASM19595v2_genomic.fna") as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            dna_string += seq.sequence_as_string()
    return dna_string
