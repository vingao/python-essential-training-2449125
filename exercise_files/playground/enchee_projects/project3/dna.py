import os
import sys
import csv

def read_dna(dna_filename):
    """
    Reads the DNA file
    This function reads the DNA sequence from the given `dna_filename`
    file. It returns the DNA sequence read from the file as a string.
    Parameters:
      dna_filename      The DNA file name
    Returns:
      str   A string that is the DNA sequence read from the file.
    """
    if os.path.isfile(dna_filename):
        file = open(dna_filename, 'r')
        data = file.read()
        file.close()
        return data
    else:
        sys.exit(f"File {dna_filename} doesn't exist")

def dna_length(dna_filename):
    """
    Returns the length of a DNA sequence in the file `dna_filename`
    Parameters:
      dna_filename     The DNA file name
    Returns:
      int   An integer length of the DNA sequence
    """
    str = read_dna(dna_filename)
    return len(str)

def read_strs(str_filename):
    """
   Reads the STRs from the given `str_filename` file
   The STR file is a CSV file containing STR repeats for certain
   people. An example of this file looks like this:
     name,AGAT,AATG,TATC
     Alice,5,2,8
     Bob,3,7,4
     Charlie,6,1,5
   This function must read the file using the `csv` module and return
   a list of dictionary objects that look like this:
     [{'name': 'Alice', 'AGAT': '5', 'AATG': '2', 'TATC': '8'},
      {'name': 'Bob', 'AGAT': '3', 'AATG': '7', 'TATC': '4'},
      {'name': 'Charlie', 'AGAT': '6', 'AATG': '1', 'TATC': '5'}]
    Parameters:
      str_filename
    Returns:
      list of dicts
    """
    list = []
    with open(str_filename, 'r') as data:
        for line in csv.DictReader(data):
            list.append(line)
        return list

def get_strs(str_profile):
    """
    Returns a tuple of (STR, repeats) pairs
    Given a dictionary representation of an STR profile that looks
    like this:
      {'name': 'Alice', 'AGAT': '5', 'AATG': '2', 'TATC': '8'}
    return a list of tuples that looks like this:
      [('AGAT', 5), ('AATG', 2), ('TATC', 8)]
    Note: the repeat is an `int`, not a `string`.
    Parameters:
    str_profile
    Returns:
    list of tuples
    """
    profile_without_name = str_profile.copy()
    del profile_without_name['name']
    return [(k, int(v)) for k, v in profile_without_name.items()]

def longest_str_repeat_count(str_frag, dna_seq):
    """
    Finds the longest match of a given STR DNA fragment in the given
    DNA sequence.
    This function returns the longest repeated occurance of the given
    STR fragment, `str_frag`, in the DNA sequence `dna_seq`. For
    example, given the STR AGAT and the DNA sequence:
    AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTA
    TCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA
    this function returns 5.
    Hints:
    1. You will want to loop over the `dna_seq` character by
       character using a while loop with an index
    2. You may find using string slicing convenient for this
       function. For example, `dna_seq[i:i+4]` will evaluate to a
       substring of `dna_seq` starting from i to i+4 exclusive.
    3. Do not use the `count` string method. It doesn't return the
       longest match, it returns the count. This would also be
       cheating.
    Parameters:
      str_frag
      dna_seq
    Returns: int
    """

    dna_length = len(dna_seq)
    str_length = len(str_frag)
    count = 0
    max_count = 0
    current_pos = 0
    for c in dna_seq:
        while current_pos + str_length <= dna_length:
            str_in_window = dna_seq[current_pos:current_pos+str_length]
            if str_in_window == str_frag:
                count += 1
                current_pos += str_length
            else:
                current_pos += 1
                count = 0
            max_count = max(max_count, count)

    return max_count

def find_match(str_profile, dna_seq):
    """
    Find a match given a specific STR profile
    This function compares the repeat values for each STR dna fragment
    X in the given `str_profile` to the count of that same X dna
    fragment in the provided DNA sequence `dna_seq`.
    For example, if we have a profile like this (a list of tuples)i
    [('AGAT', 5), ('AATG', 2), ('TATC', 8)]
    We want to determine if the number of repeats for the STR
    fragments AGAT, AATG, and TATC for this profile, which is 5, 2,
    and 8, are the same number of repeats in the DNA sequence. If the
    repeat count in the DNA sequence for AGAT, AATG, and TATC are
    identical to this profile, then we have matched the profile to the
    DNA sequence.
    Hints:
    1. You want to use the `longest_str_repeat_count` function to
      find the longest count of repeats for each STR fragment in
      the DNA sequence. This will require you to iterate over the
      `str_profile` list.
    Parameters:
    str_profile  A list of tuples representing a person's STR
                profile
    Returns:
    boolean      `True` if a match is found; `False` otherwise
    """
    for t in str_profile:
        if longest_str_repeat_count(t[0], dna_seq) != t[1]:
            return False

    return True

def dna_match(str_filename, dna_filename):
    """
    Compares STRs to a DNA sequence
    This function reads the STRs in the `str_filename` file
    and the DNA sequence in the `dna_filename` file and compares
    the STRs to the DNA sequence to determine who the DNA sequence
    likely belongs to.
    Parameters:
      str_filename      The STR file name
      dna_filename      The DNA file name
    Returns:
      str   A string that is either the person's name in the STR file
            that matches the DNA sequence in the DNA file or
            'No match' if a match does not exist.
    """
    profiles = read_strs(str_filename)
    dna_seq = read_dna(dna_filename)
    for profile in profiles:
        if find_match(get_strs(profile), dna_seq):
            return profile['name']
    return 'No match'

def test():
    print(longest_str_repeat_count('AATG', read_dna('dna_my_test.txt')))
    print(read_dna('dna_1.txt'))
    print(dna_length('dna_1.txt'))
    print(read_dna('dna_2.txt'))
    print(dna_length('dna_2.txt'))
    print(read_dna('dna_my_test.txt'))
    print(dna_length('dna_my_test.txt'))
    profiles = read_strs('str_profiles.csv')
    print(profiles)
    print(get_strs(profiles[0]))
    print(get_strs(profiles[0])[0])
    assert(get_strs(profiles[0])[0] == ('AGAT', 5))
    assert(longest_str_repeat_count('AGAT', read_dna('dna_1.txt')) == 5)
    assert(longest_str_repeat_count('AATG', read_dna('dna_1.txt')) == 2)
    assert(longest_str_repeat_count('TATC', read_dna('dna_1.txt')) == 8)
    assert(longest_str_repeat_count('AGAT', read_dna('dna_2.txt')) == 3)
    assert(longest_str_repeat_count('AATG', read_dna('dna_2.txt')) == 7)
    assert(longest_str_repeat_count('TATC', read_dna('dna_2.txt')) == 4)

    assert(longest_str_repeat_count('AATG', read_dna('dna_my_test.txt')) == 3)

    assert(find_match([('AGAT', 2), ('AATG', 3), ('TATC', 3)], read_dna('dna_my_test.txt')))

    assert(find_match([('AGAT', 5), ('AATG', 2), ('TATC', 8)], read_dna('dna_1.txt')))
    assert(not find_match([('AGAT', 5), ('AATG', 2), ('TATC', 7)], read_dna('dna_1.txt')))
    print(dna_match('str_profiles.csv', 'dna_1.txt'))
    print(dna_match('str_profiles.csv', 'dna_2.txt'))

if __name__ == '__main__':
    # test()
    if len(sys.argv) != 3:
        sys.exit('Usage: python dna.py STR_FILE DNA_FILE')
    else:
        print(dna_match(sys.argv[1], sys.argv[2]))
