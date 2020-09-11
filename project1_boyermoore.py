import fastaparser
import fileWriteReadParser
import algorithmTest

genome = ""
with open("GCF_000195955.2_ASM19595v2_genomic.fna") as fasta_file:
    parser = fastaparser.Reader(fasta_file)
    for seq in parser:
        genome += seq.sequence_as_string()

pattern = "ACTGATTC"


# create bad match table - how much do i need to shift the search string after a mismatch
# takes in pattern string as input and returns a dictionary of lookup values
def bmtable(pattern):
    bad_match = {}

    for i in range(0, len(
            pattern)):  # if character in the pattern, find the shift required to align this character with the nearest occurrence of this same character in the pattern
        bad_match[pattern[i]] = i  # index of lastmost occurrence for a particular character in pattern

    bad_match['*'] = len(
        pattern)  # if character not in the pattern, then shift the entire pattern past the current starting search point
    return bad_match


# create good suffix table - how much do i need to shift the search string after a mismatch that happens after
# takes in pattern string as input and returns a list of lookup values
def gstable(pattern):
    shift = [0] * (len(pattern) + 1)  # initialise the shift list

    # how do we compute shift
    # a few scenarios
    # 1. we find a matching prefix and shift the prefix to the current matching substring
    # 2. we can't find a match and we shift past the current starting position
    # 3. we can't find a match but the end of the substring matches with the start of the pattern so we shift the start of the pattern to the matching portion

    index = len(pattern)
    shift[index] = 1  # mismatch of the last element will always have a shift of 1
    index -= 1

    while index > 0:
        for shifted_index in range(index - 1, 0,
                                   -1):  # iterate from index-1 to 1, don't need 0 cos this scenario accounted for later
            if (pattern[index:] == pattern[shifted_index:shifted_index + len(pattern[index:])] and pattern[index - 1] !=
                    pattern[
                        shifted_index - 1]):  # check if prefix and suffix match and that character in front does not
                shift[index] = index - shifted_index

        if shift[index] == 0:  # scenarios 2 and 3
            prefix_check_index = len(pattern[
                                     index:]) - 1  # check whether scenario 3, the matching prefix to the matched substring cannot be larger than that of the substring itself
            while prefix_check_index >= 0:  # while the last element can be found in the range of matching prefix
                if pattern[prefix_check_index] == pattern[len(pattern) - 1]:
                    prefix_check = True
                    for count in range(1, prefix_check_index + 1):
                        if pattern[prefix_check_index - count] != pattern[len(pattern) - 1 - count]:
                            prefix_check = False
                            break
                    if prefix_check:
                        shift[index] = len(pattern) - 1 - prefix_check_index
                        break
                prefix_check_index -= 1
            if shift[index] == 0:
                shift[index] = len(pattern)  # if not scenario 3, then must be scenario 2

        index -= 1

    shift.remove(
        0)  # created a list that contains the distance that the pattern will shift if mismatch occurs at position i-1 and wanted to translate it to position i
    return shift


def boyermooresearch(genome, pattern):
    timeComplexity = 0

    bad_match = bmtable(pattern)  # preprocessing for bad match table
    print(bad_match)
    shift = gstable(pattern)  # preprocessing for good suffix rule
    print(shift)
    ind = 0
    result = []
    while ind <= (len(genome) - len(pattern)):
        boolean = True
        for i in range(len(pattern) - 1, -1,
                       -1):  # the comparison happens from the end of the search string to the front - backwards direction
            timeComplexity += 1
            if pattern[i] != genome[ind + i]:  # if mismatch occurs
                boolean = False
                timeComplexity += len(bad_match)
                if genome[ind + i] not in bad_match:  # first scenario: character not in query
                    jump = max(i + 1, shift[i])
                    break

                else:  # second scenario: character in query
                    jump = max(i - bad_match[genome[ind + i]], shift[i])
                    break
            else:  # if no mismatch
                jump = 1  ### KIV

        if boolean:
            result.append(ind)

        ind += jump


    fileWriteReadParser.write_data_json_file(
        algorithmTest.algorithm_analysis_data_schema("fna", pattern, len(genome), len(pattern), "fna",
                                                     algorithmTest.get_date_time_now(),
                                                     "Boyer's Moore",
                                                     timeComplexity, result))
    return result


###########################################################MAIN#############################################################################

