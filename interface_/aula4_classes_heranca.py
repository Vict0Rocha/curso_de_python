from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QGridLayout, 
                                QPushButton, QWidget)

class MyWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Titulo da minha janela')

        # Botões
        self.botao1 = self.make_button('1')
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = self.make_button('2')
        self.botao2.clicked.connect(self.saudacao)

        self.botao3 = self.make_button('3')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        # linha - coluna - expanção, de onda até onde, da linha e coluna.
        self.grid_layout.addWidget(self.botao1, 2, 1)
        self.grid_layout.addWidget(self.botao2, 2, 2)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra de status')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Qualquer coisa') 
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        # Quando for clicado, vai executar a função e exibe um msg.
        self.primeira_acao.triggered.connect(self.muda_msg_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_msg_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado', self.segunda_action.isChecked())

    @Slot()
    def saudacao(self):
        print('Hello, World!')

    def make_button(self, text: str):
        button = QPushButton(text)
        button.setStyleSheet('font-size: 40px;')
        return button

if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show() 
    app.exec() # O loop da aplicação