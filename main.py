# UTF-8 Python 3.11

import argparse
import subprocess

parser = argparse.ArgumentParser(description='Exécute un test de ping pour chaque site web du fichier passé en '
                                             'argument, et affiche leur statut en console')
parser.add_argument('file', nargs='?', help='le fichier texte \'websites.txt\'')

args = parser.parse_args()


def main():
    """Vérifie si le nom de fichier entré en argument du script est valide. Si oui, exécute 'print_website_status',
    sinon affiche une erreur."""

    try:
        print_website_status()

    except TypeError:
        print('\033[0;31mVeuillez entrer le nom d\'un fichier.\033[0m')

    except FileNotFoundError:
        print('\033[0;31mLe fichier que vous avez entré n\'existe pas ou est introuvable.\033[0m')


def print_website_status():
    """Ouvre le fichier, parcourt chaque ligne et affiche le nom DNS, ainsi que son état."""

    with open(args.file, 'r') as websites:
        for website in websites:
            try:
                ping(website.rstrip())
                print('\033[0;33m' + website.rstrip(), '\033[0;32mUP\033[0m')

            except subprocess.TimeoutExpired:
                print('\033[0;33m' + website.rstrip(), '\033[0;31mDOWN\033[0m')


def ping(dns_name):
    """Lance un ping du nom DNS en paramètre. Après 5sec, le processus s'arrête."""

    command = ['ping', dns_name]
    subprocess.call(command, timeout=5)


if __name__ == '__main__':
    main()
