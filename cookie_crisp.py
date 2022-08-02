#! /usr/bin/python

import sys, argparse, requests

def main(argv):
    value_file = ''
    cookie_file = ''
    url = ''
    
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-u', type=str, required=True)
    arg_parser.add_argument('-c', type=str, required=True)
    arg_parser.add_argument('-v', type=str, required=True)
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