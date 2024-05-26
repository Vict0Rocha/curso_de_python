# O QLayout recebe os outros widget dentro dele e posiciona da maneira desejada.

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication()

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 40px;') # Estilizando o botão com css
# botao1.show() # Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Texto do botão')
botao2.setStyleSheet('font-size: 40px;') # Estilizando o botão com css

botao3 = QPushButton('Texto do botão')
botao3.setStyleSheet('font-size: 40px;') # Estilizando o botão com css
# botao2.show() # Adiciona o widget na hierarquia e exibe a janela

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)
# linha - coluna - expanção, de onda até onde, da linha e coluna.
layout.addWidget(botao1, 2, 1)
layout.addWidget(botao2, 2, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show() 
app.exec() # O loop da aplicação