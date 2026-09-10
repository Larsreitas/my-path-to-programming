import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if len(parser._actions) < 4:
    print("Incorrect parameters")
    exit()
elif args.type is None:
    print("Incorrect parameters")
    exit()
elif args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
    exit()
elif args.interest is None:
    print("Incorrect parameters")
    exit()
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

TYPE = args.type
PAYMENT = args.payment
PRINCIPAL = args.principal
PERIODS = args.periods
INTEREST = args.interest

if PAYMENT is not None:
    if PAYMENT < 0:
        print("Incorrect parameters")
        exit()
if PRINCIPAL is not None:
    if PRINCIPAL < 0:
        print("Incorrect parameters")
        exit()
if PERIODS is not None:
    if PERIODS < 0:
        print("Incorrect parameters")
        exit()
if INTEREST is not None:
    if INTEREST < 0:
        print("Incorrect parameters")
        exit()


try:
    nom_interest = float((args.interest / 100) / (12 * 1))
    total = 0
    if args.type == "annuity":
        if args.payment is None:
            payment = math.ceil(args.principal * ((nom_interest * math.pow(1 + nom_interest, args.periods)) / (math.pow(1 + nom_interest, args.periods) - 1)))
            total = payment * args.periods
            print(f"Your monthly payment = {payment}!")
            print(f"Overpayment = {total - args.principal}")
        elif args.periods is None:
            periods = math.ceil(math.log(args.payment / (args.payment - nom_interest * args.principal), 1 + nom_interest))
            if periods < 12:
                total = args.payment * periods
                print(f"It will take {periods} months to repay this loan!")
                print(f"Overpayment = {total - args.principal}")
            elif periods % 12 == 0:
                years = periods // 12
                total = args.payment * periods
                print(f"It will take {years} years to repay this loan!")
                print(f"Overpayment = {total - args.principal}")
            else:
                years = periods // 12
                months = int(periods % 12)
                total = args.payment * periods
                print(f"It will take {years} years and {months} months to repay this loan!")
                print(f"Overpayment = {total - args.principal}")
        elif args.principal is None:
            principal = args.payment / ((nom_interest * math.pow(1 + nom_interest, args.periods)) / (math.pow(1 + nom_interest, args.periods) - 1))
            total = args.payment * args.periods
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {total - principal}")

    elif args.type == "diff":
        for current_month in range(1, args.periods + 1):
            diff_payment = math.ceil(args.principal / args.periods + nom_interest * (args.principal - ((args.principal * (current_month - 1)) / args.periods)))
            total += diff_payment
            print(f"Month {current_month}: payment is {diff_payment}")
        print(f"Overpayment = {total - args.principal}")

except TypeError, AssertionError:
    print("Incorrect parameters")
