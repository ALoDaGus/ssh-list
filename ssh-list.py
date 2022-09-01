import json
from termcolor import colored
import subprocess

FILE = "path/to/ssh/list/file.json"


def main():
    f = open(FILE)
    data = json.load(f)


    print()
    print("{:<5} {:<25} {:<65} {:<40}".format("", "instance name", "host", "description"))
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
    print("{:<5} {:<25} {:<65} {:<40}".format(colored(str(i + 1), 'cyan'), server['name'], colored(server['user'], 'green') + colored('@', 'red') + colored(server['ip'] + ' ' + ' '.join(server['args']), 'green'), colored(server['description'], 'grey', 'on_white')))
    if server['hint']:
        print(colored('  hint: ' + server['hint'], 'yellow'))


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
