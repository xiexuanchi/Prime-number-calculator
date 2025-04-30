import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

def factorize(n):
    factors = []
    divisor = 2
    while n >= divisor ** 2:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors

class FactorizationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('质因数分解计算器')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('请输入一个整数：')
        layout.addWidget(self.label)

        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)

        self.buttonFactorize = QPushButton('分解')
        self.buttonFactorize.clicked.connect(self.onButtonClick)
        layout.addWidget(self.buttonFactorize)

        self.buttonClear = QPushButton('清除')
        self.buttonClear.clicked.connect(self.onClearButtonClick)
        layout.addWidget(self.buttonClear)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

    def onButtonClick(self):
        try:
            number = int(self.lineEdit.text())
            if number < 2:
                self.textEdit.setText('请输入大于1的整数！')
                return
            factors = factorize(number)
            result = f"{number} 的质因数分解是: {' * '.join(map(str, factors))}"
            self.textEdit.setText(result)
        except ValueError:
            self.textEdit.setText('请输入有效的整数！')

    def onClearButtonClick(self):
        self.lineEdit.clear()
        self.textEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    factorizationApp = FactorizationApp()
    factorizationApp.show()
    sys.exit(app.exec())
