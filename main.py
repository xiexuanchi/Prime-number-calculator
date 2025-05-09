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
        self.setup_styles()

    def setup_styles(self):
        self.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                padding: 10px;  /* 增加内边距 */
                border: 1px solid #ccc;
                border-radius: 4px;
                background: white;
                min-height: 30px;  /* 增加最小高度 */
            }
            QPushButton {
                font-size: 12px;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                background-color: #800080;  /* 紫色主题 */
                color: white;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #4B0082;  /* 深紫色悬停效果 */
            }
            QTextEdit {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background: white;
                min-height: 80px;
            }
        """)

    def initUI(self):
        self.setWindowTitle('质因数分解计算器')
        self.setGeometry(100, 100, 450, 350)  # 增大窗口尺寸
        self.setFixedSize(450, 350)  # 固定窗口大小

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # 设置边距
        layout.setSpacing(15)  # 设置控件间距

        self.label = QLabel('请输入一个整数：')
        layout.addWidget(self.label)

        self.label.setStyleSheet("font-weight: bold; font-size: 15px;")

        # Create buttons first
        self.buttonFactorize = QPushButton('分解')
        self.buttonFactorize.clicked.connect(self.onButtonClick)
        
        self.buttonClear = QPushButton('清除')
        self.buttonClear.clicked.connect(self.onClearButtonClick)

        # Then add to layout
        button_layout = QVBoxLayout()
        button_layout.setSpacing(10)
        button_layout.addWidget(self.buttonFactorize)
        button_layout.addWidget(self.buttonClear)
        layout.addLayout(button_layout)

        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        
        # 添加输入框说明
        input_tip = QLabel("提示：请输入2以上的正整数")
        input_tip.setStyleSheet("color: #666; font-size: 12px; font-style: italic;")
        layout.addWidget(input_tip)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.textEdit)

        # 添加结果框说明
        result_tip = QLabel("说明：分解结果将显示质因数相乘的形式")
        result_tip.setStyleSheet("color: #666; font-size: 12px; font-style: italic;")
        layout.addWidget(result_tip)

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
