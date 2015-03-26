__author__ = 'krisarmstrong'


    print("DEBUG: Enigma String: ", in_string)

    '''
    Creates a list called m_key_code

    Takes in_string and converts it to a list of ints in order to calc
    checksum. Adds the ints to the m_key_code list
    '''
    m_key_code = []

    for idx in in_string:
        if idx.isdigit():
            print("DEBUG: {0} is a digit".format(idx))
            m_key_code.append("{0}".format(idx))

    print(type(in_string))
    print(type(m_key_code))

    # Debug Loop
    for idx in m_key_code:
        print("DEBUG: ", idx)