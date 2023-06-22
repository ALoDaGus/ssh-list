import json
from termcolor import colored
import subprocess

FILE = "/Users/tp/Documents/code/ssh-list/ssh-list.json"
INDENT = "{:<5} {:<25} {:<65} {:<40}"

def main():
    f = open(FILE)
    data = json.load(f)


    print()
    print(INDENT.format("", "instance name", "host", "description"))
    for i, server in enumerate(data['servers']):

        print_server_description(i, server)

        print()

    index = choose_server(data)

    user = data['servers'][index - 1]['user']
    ip = data['servers'][index - 1]['ip']
    args = data['servers'][index - 1]['args']
    password = data['servers'][index - 1]['password']
    sshpass = ['sshpass', '-p', password]


    print('ssh ' + user + '@' + ip + ' ' + ' '.join(args))

    subprocess.run((sshpass if len(password) > 0 else []) + ['ssh' , user  + '@' + ip] + (args if len(args) > 0 else []))

    f.close()


def print_server_description(i, server):
    print(INDENT.format(colored(str(i + 1), 'cyan'), server['name'], colored(server['user'], 'green') + colored('@', 'red') + colored(server['ip'] + ' ' + ' '.join(server['args']), 'green'), colored(server['description'], 'grey', 'on_white')))
    if server['hint']:
        print(colored('  hint: ', 'yellow' ) , server['hint'])
        #print(colored('  hint: ', 'yellow' ) , colored( server['hint'], 'grey'))


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
