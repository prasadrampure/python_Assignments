from sklearn.preprocessing import StandardScaler

def CalculateStandardScaler():
    Data = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(Data)

    print("Original Dataset :")
    print(Data)

    print("\n Scaled Dataset :")
    print(scaled_data)
    
def main():
    CalculateStandardScaler()

if __name__ == "__main__":
    main()