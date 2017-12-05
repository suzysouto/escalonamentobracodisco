#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
caminhoArquivo =""

#caminhoArquivo = 'C:/Users/Davi/Desktop/Sistema operacionais/arqSO.txt'

root = Tk()
root.resizable(0,0)


    
class Application:
      def __init__(self, master=None):
          self.fonte = ("Verdana", "8")
   
          self.container1 = Frame(master)
          self.container1["pady"] = 10
          self.container1.pack()
          self.container2 = Frame(master)
          self.container2["padx"] = 20
          self.container2["pady"] = 5
          self.container2.pack()
          self.container3 = Frame(master)
          self.container3["padx"] = 20
          self.container3["pady"] = 5
          self.container3.pack()
          self.container4 = Frame(master)
          self.container4["padx"] = 20
          self.container4["pady"] = 5
          self.container4.pack()
          self.container5 = Frame(master)
          self.container5["padx"] = 20
          self.container5["pady"] = 5
          self.container5.pack()
          self.container6 = Frame(master)
          self.container6["padx"] = 20
          self.container6["pady"] = 5
          self.container6.pack()
          self.container7 = Frame(master)
          self.container7["padx"] = 20
          self.container7["pady"] = 5
          self.container7.pack()
          self.container8 = Frame(master)
          self.container8["padx"] = 20
          self.container8["pady"] = 10
          self.container8.pack()
          self.container9 = Frame(master)
          self.container9["pady"] = 15
          self.container9.pack()
   
          self.titulo = Label(self.container1, text="Algoritmos de escalonamento de braço do disco:")
          self.titulo["font"] = ("Calibri", "9", "bold")
          self.titulo.pack ()
   
             
            
          self.lblCilindro = Label(self.container3, text="Qtd.Cilindros:", font=self.fonte, width=10)
          self.lblCilindro.pack(side=LEFT)
   
          self.txtCilindros = Entry(self.container3)
          self.txtCilindros["width"] = 25
          self.txtCilindros["font"] = self.fonte
          self.txtCilindros.pack(side=LEFT)
   
          self.lblPosicao = Label(self.container4, text="P. inicial:", font=self.fonte, width=10)
          self.lblPosicao.pack(side=LEFT)
   
          self.txtPosicao = Entry(self.container4)
          self.txtPosicao["width"] = 25
          self.txtPosicao["font"] = self.fonte
          self.txtPosicao.pack(side=LEFT)
   
          self.lblSeek= Label(self.container5, text="Seek:", font=self.fonte, width=10)
          self.lblSeek.pack(side=LEFT)
   
          self.txtSeek = Entry(self.container5)
          self.txtSeek["width"] = 25
          self.txtSeek["font"] = self.fonte
          self.txtSeek.pack(side=LEFT)
   
          self.lblArquivo= Label(self.container6, text="Arquivo:", font=self.fonte, width=10)
          self.lblArquivo.pack(side=LEFT)
   
          self.txtArquivo = Entry(self.container6)
          self.txtArquivo["width"] = 25
          self.txtArquivo["font"] = self.fonte
          self.txtArquivo.pack(side=LEFT)                  
             
          self.btnFIFO = Button(self.container8, text="FIFO", font=self.fonte, width=12)
          self.btnFIFO["command"] = self.simularFifo
          self.btnFIFO.pack (side=LEFT)
   
          self.btnSSF = Button(self.container8, text="SSF", font=self.fonte, width=12)
          self.btnSSF["command"] = self.simularSSF
          self.btnSSF.pack (side=LEFT)
   
          self.bntSCAN = Button(self.container8, text="SCAN", font=self.fonte, width=12)
          self.bntSCAN["command"] = self.simularSCAN
          self.bntSCAN.pack(side=LEFT)
          
          self.btnSCANC = Button(self.container8, text="SCAN C.", font=self.fonte, width=12)
          self.btnSCANC["command"] = self.simularSCANC
          self.btnSCANC.pack(side=LEFT)

          self.btnLoad = Button(self.container8, text="Carregar", font=self.fonte, width=15)
          self.btnLoad["command"] = self.selecionarArquivo
          self.btnLoad.pack(side=LEFT)

          self.btnSave = Button(self.container8, text="Salvar", font=self.fonte, width=12)
          self.btnSave["command"] = self.salvaarquivo
          self.btnSave.pack(side=LEFT)
   
          self.lblmsg = Label(self.container9, text="")
          self.lblmsg["font"] = ("Verdana", "9", "italic")
          self.lblmsg.pack()
   
   
      def simularFifo(self):
          listaNumeros = carregarArquivo(caminhoArquivo)
          #user = Usuarios()
          cilindros = self.txtCilindros.get()
          posicaoInicial = self.txtPosicao.get()
          seek = self.txtSeek.get()
          arquivo = self.txtArquivo.get()
          atual = 0
          #algoritmo
          posIni = posicaoInicial
          for i in range(len(listaNumeros)):
                  if(posIni == listaNumeros[i]):
                      print('')
                  else:
                      atual = (posIni - listaNumeros[i]) 
                  
                  
          
          print(listaNumeros)
          print(cilindros)
          print(posicaoInicial)
          print(seek)
          print(arquivo)

         
   
   
   
      def simularSSF(self):
          #user = Usuarios()
          cilindros = self.txtCilindros.get()
          posicaoInicial = self.txtPosicao.get()
          seek = self.txtSeek.get()
          arquivo = self.txtArquivo.get()
          print(cilindros)
          print(posicaoInicial)
          print(seek)
          print(arquivo)
   
   
   
      def simularSCAN(self):
          #user = Usuarios()
   
          cilindros = self.txtCilindros.get()
          posicaoInicial = self.txtPosicao.get()
          seek = self.txtSeek.get()
          arquivo = self.txtArquivo.get()
          print(cilindros)
          print(posicaoInicial)
          print(seek)
          print(arquivo)
          
      def simularSCANC(self):
          #user = Usuarios()
          cilindros = self.txtCilindros.get()
          posicaoInicial = self.txtPosicao.get()
          seek = self.txtSeek.get()
          arquivo = self.txtArquivo.get()
          print(cilindros)
          print(posicaoInicial)
          print(seek)
          print(arquivo)
   
      def convPositivo(numero):
          if(numero >= 0):
              return numero
          else:
              return numero * -1

      def carregarArquivo(self,caminhoArquivo):
          arq = open(caminhoArquivo,'r')
          vetBruto = arq.read()
          listaNumeros = []
          acm = ""
          for i in range(0,len(vetBruto)):
              if(vetBruto[i] != "-"):
                  acm = acm+vetBruto[i]
              elif(vetBruto[i] == "-"):
                  listaNumeros.append(acm)
                  acm=""
          print(listaNumeros)
          return listaNumeros
          arq.close()

      def selecionarArquivo(self):
          caminhoArquivo = filedialog.askopenfilename()
         # self.txtArquivo.text = caminhoArquivo
          print(" \nArquivo Carregado: "+caminhoArquivo)
          self.carregarArquivo(caminhoArquivo)
          return caminhoArquivo

      def salvaarquivo(self):
          f = filedialog.asksaveasfile(mode="w", )#A foi opcao definida para escrita.
          if f is None:
              return
          f.write("lalalala") #Colocar saidas dentro do arquivo
          f.close()
          
      


#arq.writelines(listaAlunos)   
   
   
#root = Tk()
#root.mainloop()
Application(root)



#f = open(caminhoArquivo,'r')
#novaLista = f.read()
#print("NovaLista\n"+ novaLista)
