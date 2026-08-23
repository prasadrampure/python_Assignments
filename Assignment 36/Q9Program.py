from sklearn.metrics import classification_report

def ClassificationReport():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    report = classification_report(actual,predicted)

    print("Classification Report :")
    print(report)
    
def main():
    ClassificationReport()

if __name__ == "__main__":
    main()