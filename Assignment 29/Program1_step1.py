import math
import numpy as np

def KNNClassifier():
    border = "-"*50

    Data =[
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 6, "Y" : 5, "ladel" : "Blue"}
    ]

    print(border)
    print("KNNClassifier")
    print(border)

    for i in Data:
        print(i)

def main():
    KNNClassifier()

if __name__ == "__main__":
    main()