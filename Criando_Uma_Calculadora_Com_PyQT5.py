import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton   # Botão
from PyQt5.QtWidgets import QLineEdit   # Display da calculadora   / LineEdit é na vdd um input
from PyQt5.QtWidgets import QSizePolicy   # Para os botões se encaixarem automaticamente no grid
from PyQt5 import QtGui   # Para definir ícone da janela


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)   # Executando o inicializador da QMainWindow
        self.setWindowTitle('Calculator By Traxr')   # Definindo titulo da Janela
        self.setWindowIcon(QtGui.QIcon('images\icon.png'))   # Definindo ícone para a janela
        self.setFixedSize(320, 500)   # Definindo um tamanho fixo para a janela
        self.cw = QWidget()   # Central Widget
        self.grid = QGridLayout(self.cw)   # Grid com central Widget

        # Definindo estilo global da calculadora
        self.setStyleSheet('background: #242424; border: 1px solid; color: #C8C8C8;')

        self.display = QLineEdit()   # Criando o Display da Calculadora
        self.grid.addWidget(self.display, 0, 0, 1, 4)   # adc display ao grid na ln 0, cl 0, ocupando 1 ln e 5 cl
        self.display.setDisabled(True)   # Desativando o input (Tornando-o um display)

        # Definindo estilo do display
        self.display.setStyleSheet(
            '* {background: #2b2b2b; color: #C8C8C8; font-size: 40px;}'   # CSS
        )
        # Configurando o display para se expandir de acordo com o espaço que existe no grid
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Adicionando os botões
        self.add_btn(QPushButton('*'), 1, 0, 1, 1)
        self.add_btn(QPushButton('/'), 1, 1, 1, 1)
        self.add_btn(QPushButton('%'), 1, 2, 1, 1)   # unscheduled
        self.add_btn(QPushButton('<<'), 1, 3, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]),
                     'QPushButton { background: #2541d6;')   # Apagando o ultimo caractere

        self.add_btn(QPushButton('7'), 3, 0, 1, 1)
        self.add_btn(QPushButton('8'), 3, 1, 1, 1)
        self.add_btn(QPushButton('9'), 3, 2, 1, 1)
        # Definindo o conteúdo do display como Vazio
        self.add_btn(QPushButton('C'), 3, 3, 1, 1, lambda: self.display.setText(''),
                     'QPushButton { background: #2541d6; font-weight: 500;')

        self.add_btn(QPushButton('4'), 4, 0, 1, 1)
        self.add_btn(QPushButton('5'), 4, 1, 1, 1)
        self.add_btn(QPushButton('6'), 4, 2, 1, 1)
        self.add_btn(QPushButton('-'), 4, 3, 1, 1)

        self.add_btn(QPushButton('1'), 5, 0, 1, 1)
        self.add_btn(QPushButton('2'), 5, 1, 1, 1)
        self.add_btn(QPushButton('3'), 5, 2, 1, 1)
        self.add_btn(QPushButton('+'), 5, 3, 1, 1)

        self.add_btn(QPushButton('+/-'), 6, 0, 1, 1)   # unscheduled
        self.add_btn(QPushButton('0'), 6, 1, 1, 1)
        self.add_btn(QPushButton('.'), 6, 2, 1, 1)
        # Passando o método sem executar (Sem o ())
        self.add_btn(QPushButton('='), 6, 3, 1, 1, self.eval_igual, 'background: #2541d6;')

        self.setCentralWidget(self.cw)   # Definindo o Widget central como o cw definido anteriormente

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        """
        btn: Botão
        row: Linha
        col: Coluna
        rowspan: Quantidade de linhas ocupadas pelo botão
        colspan: Quantidade de colunas ocupadas pelo botão
        """
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:   # Se não receber função
            btn.clicked.connect(   # Definindo procedimento para quando o botão é clicado
                lambda: self.display.setText(   # Função que concatena o texto do display com o texto do btn pressionado
                    self.display.text() + btn.text()
                )
            )
        else:   # Se receber função
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(f'{style} border: 1px solid; border-color: black; font-size: 20px;' + '}' +
                              'QPushButton::pressed'   # Definindo nova cor quando o botão é pressionado
                              '{ background-color: #2541a9; }'
                              'QPushButton:hover:!pressed'  # Definindo cor quando o ponteiro passa por cima do botão
                              '{ background: #2541a9; }')
        else:
            btn.setStyleSheet('QPushButton'
                              '{ background: #2b2b2b; border: 1px solid; border-color: black; font-size: 20px; }'
                              'QPushButton::pressed'   # Definindo nova cor quando o botão é pressionado
                              '{ background-color: #404040; }'
                              'QPushButton:hover:!pressed'   # Definindo cor quando o ponteiro passa por cima do botão
                              '{ background: #404040; }')

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))   # eval() verifica a expressão e se valido retorna o resultado
            )
        except Exception as e:
            self.display.setText('error')


if __name__ == '__main__':
    qt = QApplication(sys.argv)   # Instanciando QApplication
    calc = Calculadora()   # Instanciando Calculadora
    calc.show()   # Mostrando a janela
    qt.exec_()   # inicia o event loop (um loop que verifica eventos que ocorrem na janela)
