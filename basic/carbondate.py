import math
K = -8266.64258429376
def main():
    calculate_age_single_sample()
def calculate_age_single_sample():
    #The percent of c14 left in sample
    c14 = float(input("% of natural c14 "))
    age = K * math.log(c14/100)
    print("The sample is "+str(age)+" year old.")
if __name__ == '__main__':
    main()