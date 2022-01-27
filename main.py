from PyQt5 import uic, QtWidgets
import random
import string
import clipboard as c
from PyQt5.QtWidgets import QMessageBox

def escolha():

    tamanhoSenha = telaInicial.spinBox.value()
    if telaInicial.checkBox.isChecked():
        gerarSenhaCaracteres(tamanhoSenha)
    else:
        gerarSenha(tamanhoSenha)


def embaralharSenha(senha,tamanhoSenha):

    random.shuffle(senha)
    random.shuffle(senha)
    senha = senha[:tamanhoSenha]
    senha = str(senha)
    senha = senha.replace('[','')
    senha = senha.replace(']','')
    senha = senha.replace("'",'')
    senha = senha.replace(",",'')
    senha = senha.split()
    senha = ''.join(senha)
    telaInicial.labelSenha.setText(senha)
    telaInicial.labelOk.setText('Senha Gerada Com Sucesso! ✔️')
    copiar(senha)


def gerarSenhaCaracteres(tamanhoSenha):

    c = 1
    senhaComCaracteres = []
    while c <= tamanhoSenha:
        senhaComCaracteres.append(random.choice(['/','*','-','_','.','(',')']))
        senhaComCaracteres.append(random.choice(string.ascii_letters))
        senhaComCaracteres.append(random.randint(0, 9))
        c += 1
    embaralharSenha(senhaComCaracteres,tamanhoSenha)


def gerarSenha(tamanhoSenha):

    c = 1
    senhaSemCaracteres = []
    while c <= tamanhoSenha:
        senhaSemCaracteres.append(random.choice(string.ascii_letters))
        senhaSemCaracteres.append(random.randint(0, 9))
        c += 1
    embaralharSenha(senhaSemCaracteres,tamanhoSenha)


def copiar(senha):

    if senha == '':
        senha = ''
    c.copy(senha)
    c.paste()
    msgBox = QMessageBox()
    msgBox.setWindowTitle('Alerta')
    msgBox.setText('Senha salva na área de transferência')
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setStyleSheet('QMessageBox{background-color:rgb(49,57,101);font-family: Arial black; font-size:14px;}QLabel{color: White;}')
    msgBox.exec_()


# Interface Grafica
app = QtWidgets.QApplication([])
telaInicial = uic.loadUi('tela_inicial.ui')
telaInicial.show()
telaInicial.pushButtonGerar.clicked.connect(escolha)
app.exec()
