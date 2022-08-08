def main():
    meters = float(input("Enter meter"))
    result = meters_to_cm(meters)
    print(result)
def meters_to_cm(meters):
    return 100 * meters
if __name__ == "__main__":
    main()