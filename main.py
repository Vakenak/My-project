from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox
from random import *
class Question():
    def __init__(self, question, right_answer, wrong, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong = wrong
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo card')
main_win.resize(500,400)
text = QLabel('Вопрос')
group = QGroupBox('Варианты:')
button1 = QRadioButton('Вариант 1')
button2 = QRadioButton('Вариант 2')
button3 = QRadioButton('Вариант 3')
button4 = QRadioButton('Вариант 4')
button = QPushButton('Ответить')
layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout1.setSpacing(30)
layout2.addWidget(button1)
layout2.addWidget(button2)
layout3.addWidget(button3)
layout3.addWidget(button4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
text1 = QLabel('Самый сложный вопрос в мире!')
text2 = QLabel('прав ты или нет')
text3 = QLabel('ответ будет тут!')
group2 = QGroupBox('Результаты теста:')
layout5 = QHBoxLayout()
layout6 = QVBoxLayout()
layout7 = QVBoxLayout()
layout6.addWidget(text2, alignment = Qt.AlignLeft|Qt.AlignTop)
layout7.addWidget(text3)
layout5.addLayout(layout6)
layout5.addLayout(layout7)
group2.setLayout(layout5)
group.setLayout(layout1)
def show_question():
    group.hide()
    group2.show()
    button.setText('Показать ответы')
def show_results():
    group2.hide()
    group.show()
    button.setText('Ответить')
def start_test():
    if button.text() == 'Показать ответы':
        show_results()
        next_questions()
    elif button.text() == 'Ответить':
        check_answer()
        show_question()
button.clicked.connect(start_test)
answer = [button1, button2, button3, button4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
questions = []
q = Question('пон', 'ок', 'ок', 'ок', 'ок')
q1 = Question('rfr', 'rr', 'rr', 'rr', 'rr')
q3 = Question('re3e3fr', 'e3err', 're3er', 'rre3e', 're3er')
q4 = Question('yui', 'tt', 't', 'ttt', 'ttt')
questions.append(q)
questions.append(q1)
questions.append(q3)
questions.append(q4)
main_win.sp2 = 0
def click_ok():
    if button.setText() == 'Ответить':
        main_win.sp2 += 1
        next_questions()
    elif button.setText() == 'Показать ответы':
        check_answer()
main_win.sp1 = 0
main_win.sp = 0
def check_answer():
    if main_win.sp1 + main_win.sp == len(questions):
        print1()
    if answer[0].isChecked():
        main_win.sp += 1
        show_correct('Верно')
    if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        main_win.sp1 += 1
        show_correct('Неверно')
SH = 0
def next_questions():
    number = 3
    app.schetchik = randint(0, number)
    ask(questions[app.schetchik])
def show_correct(res):
    text2.setText(res)
check_answer()
layout.addWidget(text, alignment = Qt.AlignCenter)
layout.addWidget(group)
layout.addWidget(group2)
group2.hide()
layout.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(layout)
def print1():
    print('правильные ответы:', main_win.sp)
    print('неправильные ответы:', main_win.sp1)
    print('отвечено:', main_win.sp2)
    raiting = main_win.sp2 / main_win.sp * 100
    print(raiting, '- рейтинг')


main_win.show()
app.exec_()
