import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of the dog"
)
parser.add_argument("-c", "--c", metavar="color", required=True,help="The color to search for")
args = parser.parse_args()
print(args.color)