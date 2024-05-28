# O QLayout recebe os outros widget dentro dele e posiciona da maneira desejada.

# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QGridLayout, 
                                QPushButton, QWidget)

app = QApplication()
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Titulo da minha janela')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 40px;') # Estilizando o botão com css
# botao1.show() # Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Texto do botão')
botao2.setStyleSheet('font-size: 40px;') # Estilizando o botão com css

botao3 = QPushButton('Texto do botão')
botao3.setStyleSheet('font-size: 40px;') # Estilizando o botão com css
# botao2.show() # Adiciona o widget na hierarquia e exibe a janela


layout = QGridLayout()
central_widget.setLayout(layout)
# linha - coluna - expanção, de onda até onde, da linha e coluna.
layout.addWidget(botao1, 2, 1)
layout.addWidget(botao2, 2, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

def slot_exemple(status_bar):
    status_bar.showMessage('Nova msg na barra de status')

def outro_slot(checked):
    print('Está marcado', checked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

def saudacao():
    print('Hello, World!')

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra de status')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa') 
primeira_acao = primeiro_menu.addAction('Primeira ação')
# Quando for clicado, vai executar a função e exibe um msg.
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))

segunda_action = primeiro_menu.addAction('Segunda ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)
segunda_action.hovered.connect(terceiro_slot(segunda_action))

botao1.clicked.connect(terceiro_slot(segunda_action))
botao2.clicked.connect(saudacao)

window.show() 
app.exec() # O loop da aplicação