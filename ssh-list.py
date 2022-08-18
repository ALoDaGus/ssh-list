import json
from termcolor import colored
import subprocess

FILE = "/Users/tp/Documents/code/ssh-list/ssh-list.json"

def main():
    f = open('/Users/tp/Documents/code/ssh-list/ssh-list.json')
    data = json.load(f)


    print()
    for i, server in enumerate(data['servers']):

        print_server_description(i, server)

        print()

    index = choose_server(data)

    user = data['servers'][index - 1]['user']
    ip = data['servers'][index - 1]['ip']
    args = data['servers'][index - 1]['args']

    print('ssh ' + user + '@' + ip + ' ' + ' '.join(args))
    subprocess.run([ 'ssh' , user  + '@' + ip] + (args if len(args) > 0 else []))

    f.close()


def print_server_description(i, server):
    print(colored(str(i + 1), 'cyan') + ' ' + server['name'], end='\t\t')
    print(colored(server['user'], 'green') + colored('@', 'red') + colored(server['ip'] + ' ' + ' '.join(server['args']), 'green'), end='\t')
    print(colored(server['description'], 'grey', 'on_white'))
    if server['hint']:
        print('\t' + colored('hint: ' + server['hint'], 'yellow'))


def choose_server(data):
    index = 0
    while type(index) != int or index <= 0 or index > len(data['servers']):
        try:
            index = int(input(colored('number: ', 'green')))
        except ValueError:
            print(colored('try again', 'red'))
    return index


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
