import argparse
import sys


def check_args(args=None):
    parser = argparse.ArgumentParser(description='A Script to check if a combo inside a combolist follows password rules.')
    parser.add_argument('-on', '--only-numbers', type=bool, help='Can it contain only numbers ?', required=False, default=False)
    parser.add_argument('-ol', '--only-letters', type=bool, help='Can it contain only letters ?', required=False, default=False)
    parser.add_argument('-sc', '--special-char', type=bool, help='Does it have to contain special characters ? (!@#$%^&*())', required=False, default=True)
    parser.add_argument('-cl', '--capital-letters', type=bool, help='Does it have to contain capital letters?', required=False, default=True)
    parser.add_argument('-min', '--min-chars', type=int, help='Minimum characters allowed.', required=False, default=8)
    parser.add_argument('-max', '--max-chars', type=int, help='Maximum characters allowed.', required=False, default=24)
    parser.add_argument('-file', '--file-path', type=str, help='Path of the file (if its in the same folder simply insert the filename)', required=True)

    results = parser.parse_args(args)
    return (results.only_numbers, results.only_letters, results.special_char,
            results.special_char, results.min_chars, results.max_chars, results.file_path)


def check(password):
    if len(password) >= min_length and len(password) <= max_length:
        return True
    return False


if __name__ == "__main__":

    loaded = 0
    out = 0

    only_numbers, only_letters, special_char, capital_letters, min_length, max_length, file = check_args(sys.argv[1:])

    try:
        with open(file, 'r') as input:
            print('[+] Starting ...')
            with open('newfile.txt', "w") as output:
                for line in input:
                    loaded += 1
                    try:
                        uname = line.split(':')[0]
                        password = line.split(':')[1]
                        if check(password):
                            out += 1
                            output.write(uname + ':' + password)

                    except Exception as e:
                        pass

        print('[+] ' + str(loaded) + ' Accounts loaded .')
        print('[+] ' + str(out) + ' Accounts exported according password rules .')

    except Exception as e:
        print('[!] {} \n[!] Please specify correct file name or full file path.'.format(e))