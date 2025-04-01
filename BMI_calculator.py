# This Python file uses the following encoding: utf-8
#this class is used to calculate the BMI of a user - backend for now


class BMI_calculator:
    def __init__(self, userHeight, userWeight):
        self.height = userHeight
        self.weight = userWeight
        self.bmi = 0

    def calcBMI(self):

        self.bmi = (self.weight) / (self.height / 100)**2
        return self.bmi

    def displayBMI(self):
        print(f"Your current BMI is: {self.bmi}")

