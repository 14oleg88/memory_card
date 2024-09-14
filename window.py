from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QSpinBox, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout


window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(500, 400)
window.move(200,200)

menu_btn = QPushButton("меню")
rest_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_label = QLabel("Хвилин")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addWidget(rest_btn)
row1.addWidget(time_box)
row1.addWidget(time_label)

question_text = QLabel("mouse")


main_line = QVBoxLayout()
main_line.addLayout(row1)
main_line.addWidget(question_text, alignment=Qt.AlignCenter)

btn1 = QRadioButton("миша")
btn2 = QRadioButton("щур")
btn3 = QRadioButton("мишок")
btn4 = QRadioButton("мус")

answer_btn = QPushButton("Відповісти")

window.setLayout(main_line)