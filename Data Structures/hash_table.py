def hashingDivision(key, mod):
    return key % mod

if __name__ == "__main__":
    dictionary = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

    print(dictionary)

    # Insertion
    dictionary['e'] = 5
    print(dictionary)

    # Deletion
    del dictionary['a']
    print(dictionary)

    # Search
    print(dictionary['c'])

    # key = 50, table size = 13
    k = 50
    m = 13
    print(f'Hash of 50 with table size 13 --> {hashingDivision(k, m)}')