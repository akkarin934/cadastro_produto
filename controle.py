
# importando módulo uic para ler o arquivo UI e QtWidgets para montar os elementos
from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produto"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text() # lê o que foi digitado
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked(): # verifica se o botão foi clicado
        print("Categoria Alimento selecionada")
        categoria = "Alimento"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Limpeza selecionada")
        categoria = "Limpeza"
    else:
        print("Categoria Higiene selecionada")
        categoria = "Higiene"

    print("Código:", linha1) # o que foi digitado no "código" na interface gráfica, é recuperado na linha 1, e assim por diante
    print("Nome:", linha2)
    print("Preço:", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produto (codigo, nome, preco, categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
   
    formulario.lineEdit.setText("") # limpa o escrito após enviar
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui") # carrega o arquivo UI
segunda_tela=uic.loadUi("listar_produtos.ui")
formulario.pushButton.clicket.connect(funcao_principal)

formulario.show()
app.exec()


