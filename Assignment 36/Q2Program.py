import numpy as np

def CalculateMean():
    Data = [6,7,8,9,10,11,12]

    Mean = np.mean(Data)

    print("Dataset :",Data)
    print("Mean :",Mean)

    Variance = np.var(Data)

    StandardDaviation = np.std(Data)

    print("Variance :",Variance)
    print("Standard Daviation :",StandardDaviation)
    
def main():
    CalculateMean()
if __name__ == "__main__":
    main()