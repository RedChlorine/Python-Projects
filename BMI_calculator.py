# This Python file uses the following encoding: utf-8
#this class is used to calculate the BMI of a user - backend for now
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class BMI_calculator(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class's constructor
        self.initUI()

    def initUI(self):
        #set the layout as a vertical box
        layout = QVBoxLayout()

        #set the height label and height input => add to layout
        self.heightLabel = QLabel("Height (cm):")
        self.heightInput = QLineEdit()
        layout.addWidget(self.heightLabel)
        layout.addWidget(self.heightInput)

        #set the weight label and weight input => add to layout
        self.weightLabel = QLabel("Weight (kg):")
        self.weightInput = QLineEdit()
        layout.addWidget(self.weightLabel)
        layout.addWidget(self.weightInput)

        #set calculate bmi pushbutton => set signal/slot of button => add to layout
        self.calcButton = QPushButton("Calculate BMI")
        self.calcButton.clicked.connect(self.calculateAndDislpay)
        layout.addWidget(self.calcButton)

        #set result of bmi calculation
        self.resultLabel = QLabel("")
        layout.addWidget(self.resultLabel)

        #set the above layout to the window and set window title
        self.setLayout(layout)
        self.setWindowTitle("BMI Calculator")

    def calculateAndDislpay(self):
        try:
            #gets the text from heightInput: float
            height = float(self.heightInput.text())

            #gets the text from weightInput: float
            weight = float(self.weightInput.text())

            #calculate bmi => display the result under result label: float 2 precision
            bmi = weight/(height/100)**2
            self.resultLabel.setText(f"Your BMI is:{bmi:.2f}")

        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Please enter a numeric value")

        except ZeroDivisionError:
            QMessageBox.critical(self, "Error", "Height must be a value greater than zero")


    def calcBMI(self):
        self.bmi = (self.weight) / (self.height / 100)**2
        return self.bmi

    def displayBMI(self):
        print(f"Your current BMI is:{self.bmi}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bmi_calculator = BMI_calculator()
    bmi_calculator.show()
    sys.exit(app.exec())
