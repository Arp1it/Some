import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y

    elif args.o == "mu":
        return args.x * args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "div":
        return args.x / args.y

    else:
        return "something went wrong"

if __name__ == "__main__":
    parsee = argparse.ArgumentParser()
    parsee.add_argument("--x", type = float, default = 0.0, help = "Enter first number. This a utility for calculation. Please contact arpit aand harry bhai.")

    parsee.add_argument("--y", type = float, default = 0.0, help = "Enter second number. This a utility for calculation. Please contact arpit aand harry bhai.")

    parsee.add_argument("--o", type = str, default = "add", help = "Enter first number. This a utility for calculation. Please contact arpit aand harry bhai for more.")

    arg = parsee.parse_args()

    sys.stdout.write(str(calc(arg)))

# & 'F:\codewitharryyy\commandlineutility'