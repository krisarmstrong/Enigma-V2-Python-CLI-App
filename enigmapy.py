from builtins import print
__author__ = 'krisarmstrong'

# Global Variables
n0, n9, nA = b'09A'


def calc_checksum(in_string):
    # Gets the length of in_string which should be == 16
    key_length = len(in_string)

    # in_string is a str converting in_string to bytes in m_key_code
    m_key_code = str.encode(in_string)

    # print("DEBUG: Key Length: ", key_length)

    # Calculating check_sum
    # n0, n9, nA = b'09A'

    check_sum = 1
    for idx, n in enumerate(m_key_code[2:], 2):
        if n0 <= n <= n9:
            temp_sum = n - n0
        else:
            temp_sum = n - nA
        check_sum += idx + temp_sum + (idx * temp_sum)
    check_sum = ((100 - check_sum) % 100)
    dummy = [n0 + (check_sum % 10), n0 + ((check_sum // 10) % 10)]
    m_key_code = bytes(dummy) + m_key_code[2:]

    calc_option_code(m_key_code)


def calc_option_code(m_key_code):

    # Rotors used to calculate Option Key
    e_rotor_10 = bytes([5, 4, 1, 8, 7, 3, 0, 2, 9, 6])
    e_rotor_26 = bytes([16, 8, 25, 5, 23, 21, 18, 17, 2, 1, 7, 24, 15, 11, 9, 6, 3, 0, 19, 12, 22, 14, 10, 4, 20, 13])

    # Setting max check sum size to 26000
    max_check_sum = 26000

# Encipher Key
    option_key = []
    checksum = 0
    for idx, n in enumerate(m_key_code[:]):
        if n0 <= n <= n9:
            temp_sum = (n - n0)
            m_key_code = (e_rotor_10[(temp_sum + max_check_sum - checksum) % 10] + 0)
        else:
            temp_sum = n - nA
            m_key_code = (e_rotor_26[(temp_sum + max_check_sum - checksum) % 26] + nA)

        checksum += idx + temp_sum + (idx * temp_sum)

        option_key.append(int(m_key_code))

    opt_code = (''.join(map(str, option_key)))
    print("Option Code: ", opt_code)


def main():
    serial_number = input("Enter your 7 digit serial Number :")
    product_code = input("Enter your 4 digit Product Code (1TAT = , LRAT = , ES/MS =, LRPro/Duo (7001) : ")
    option_code = input("Enter your 3 digit Option Code :")

    temp_check_sum = '00'
    in_string = temp_check_sum + product_code + serial_number + option_code

    calc_checksum(in_string)

if __name__ == "__main__":
    main()