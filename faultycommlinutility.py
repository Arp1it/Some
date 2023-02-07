import argparse
import sys

def faucalc(ar):
    if ar.xx == 45.0 and ar.y == 3.0 and ar.op == "*":
        return 555

    if ar.xx == 56.0 and ar.y == 9.0 and ar.op == "+":
        return 77

    if ar.xx == 56.0 and ar.y == 6.0 and ar.op == "/":
        return 4

    if ar.op == "+":
        return ar.xx + ar.y

    if ar.op == "-":
        return ar.xx - ar.y

    if ar.op == "*":
        return ar.xx * ar.y

    if ar.op == "/":
        return ar.xx / ar.y

    if ar.op == "**":
        return ar.xx ** ar.y

    else:
        return "Something wernt wrong"

if __name__ == '__main__':
    prser = argparse.ArgumentParser()

    prser.add_argument("-xx", type = float, default = 0.0, help = "Enter first number: ")

    prser.add_argument("-y", type = float, default = 0.0, help = "Enter second number")

    prser.add_argument("-op", type = str, default = "+", help = "Enter operational value like for multyply (*), for add (+), for subtract (-), for divide (/) and for power (**)")

    argg = prser.parse_args()

    sys.stdout.write(str(faucalc(argg)))

# & 'F:\codewitharryyy\faultycommlinutility.py'