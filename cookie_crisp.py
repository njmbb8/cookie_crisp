#! /usr/bin/python

import sys, argparse, requests

def main(argv):
    arg_parser = argparse.ArgumentParser(prog='Cookie Crisp', 
                                            description='Script to bruteforce cookies',
                                            usage='cookie_crisp.py -u <URL> -c <Path to cookie wordlist> -v <Path to file containing values>'
                                            )
    arg_parser.add_argument('-u', type=str, help="URL to test against", required=True)
    arg_parser.add_argument('-c', type=str, help="Wordlist to pull cookies from", required=True)
    arg_parser.add_argument('-v', type=str, help="Wordlist to pull values from", required=True)
    args = arg_parser.parse_args()

    with open(args.c, 'r') as file:
        cookie_file = file.readlines()

    with open(args.v, 'r') as file:
        value_file = file.readlines()

    for cookie in cookie_file:
        cookie = cookie.rstrip('\n')
        for value in value_file:
            value = value.rstrip('\n')
            req = requests.post(args.u, cookies={cookie: value})
            print(f'cookie: {cookie}, value: {value}, result: {req.status_code}')

if __name__ == "__main__":
    main(sys.argv[1:])