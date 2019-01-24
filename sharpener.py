import argparse
import sys


def check_args(args=None):
    parser = argparse.ArgumentParser(description='A Script to check if a combo inside a combolist follows password rules.')
    parser.add_argument('-on', '--only-numbers', type=str2bool, help='Can it contain only numbers ?',  default=False)
    parser.add_argument('-ol', '--only-letters', type=str2bool, help='Can it contain only letters ?',  default=False)
    parser.add_argument('-sc', '--special-char', type=str2bool, help='Does it have to contain special characters ?', default=True)
    parser.add_argument('-cl', '--capital-letters', type=str2bool, help='Does it have to contain capital letters?', default=True)
    parser.add_argument('-min', '--min-chars', type=int, help='Minimum characters allowed.',  default=8)
    parser.add_argument('-max', '--max-chars', type=int, help='Maximum characters allowed.', default=24)
    parser.add_argument('-f', '--file', type=str, help='Path of the file (if its in the same folder simply insert the filename)', required=True)

    results = parser.parse_args(args)
    return (results.only_numbers, results.only_letters, results.special_char,
            results.special_char, results.min_chars, results.max_chars, results.file)


def check(password):
    if len(password) >= min_length and len(password) <= max_length:
        return True
    return False


def str2bool(arg):
    if arg.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif arg.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


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

        print('[+] {} Accounts loaded .'.format(loaded))
        print('[+] {} Accounts exported according to password rules .'.format(out))

    except Exception as e:
        print('[!] {} \n[!] Please specify correct file name or full file path.'.format(e))
