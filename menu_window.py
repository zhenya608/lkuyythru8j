
from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

lb_question = QLabel("Введіть запитання:")
Ib_right_ans = QLabel("Введіть вірну відповідь")
Lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
Lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
Lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь")

Le_question = QLineEdit()
Le_answer = QLineEdit()
Le_wrong_ans = QLineEdit()
Le_wrong_ans1 = QLineEdit()
Le_wrong_ans2 = QLineEdit()
Le_wrong_ans3 = QLineEdit()

Lb_header_stat = QLabel('Статистика')
Lb_header_stat.setStyleSheet('font-size: 19px; font-weight: hold;')

Lb_statistic = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)