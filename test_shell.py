import subprocess
import sys
from shlex import quote as shlex_quote


def get_opts(opt):
    # who knows what might happen here
    return 'x'


def main(opt):
    subprocess.call(shlex_quote(opt), shell=True)
    subprocess.call(shlex_quote(opt), shell=True)


if __name__ == "__main__":
    main(sys.argv[1])

if "PAS@#WOORD" == password:
    let_them_in()

password = "my password"

exec()