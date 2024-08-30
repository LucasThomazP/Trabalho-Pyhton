from tkinter import *  
from tkinter import font 
from tkinter import ttk
from tkinter import messagebox

#comando 


#Importandoi Views 
from view import * 


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x450')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)



################# divisão da tabela ###############

frame_titulo = Frame(janela, width=310, height=50, bg=co6, relief='flat')
frame_titulo.grid(row=0, column=0)

frame_esquerda = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_esquerda.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=700, height=400, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=5, padx=2, pady=2, sticky=NSEW)

################# Configuração Titulo ###############

app_nome = Label(frame_titulo, text='Cadastro Alunos', font=('Ivy 13 bold'), bg=co6, fg=co4, relief='flat')
app_nome.place(x=70, y=10)

#variavel global
global tree

#Função inserir
def inserir():
  nome = e_nome.get()
  email = e_email.get()
  telefone = e_telefone.get()
  data = e_date.get()

  lista = [nome, email, telefone, data]

  if nome=='':
    messagebox.showerror('Erro', 'Preencha o nome')
  else:
    inserir_info(lista)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')  

    e_nome.delete(0,'end')        
    e_email.delete(0,'end')
    e_telefone.delete(0,'end')
    e_date.delete(0,'end')

  for widget in frame_direita.winfo_children():
    widget.destroy()  

  mostrar()
  
# Função atualizar
def atualizar():
  try:
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    tree_lista = treev_dicionario['values']

    valor_id = tree_lista[0]


    e_nome.delete(0,'end')        
    e_email.delete(0,'end')
    e_telefone.delete(0,'end')
    e_date.delete(0,'end')



    e_nome.insert(0,tree_lista[1])        
    e_email.insert(0,tree_lista[2])
    e_telefone.insert(0,tree_lista[3])
    e_date.insert(0,tree_lista[4])

    def update():
      nome = e_nome.get()
      email = e_email.get()
      telefone = e_telefone.get()
      data = e_date.get()

      lista = [nome, email, telefone, data, valor_id]

      if nome=='':
        messagebox.showerror('Erro', 'Preencha o nome')
      else:
        atualizar_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')  

        e_nome.delete(0,'end')        
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_date.delete(0,'end')

      for widget in frame_direita.winfo_children():
        widget.destroy()  

      mostrar()

      #Botão Atualizar
    b_confirmar = Button(frame_esquerda, command=update, text='Confirmar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co4, relief='raised', overrelief='ridge')
    b_confirmar.place(x=110, y=380)


    
  except IndexError:
    messagebox.showerror('Erro', 'Selecione o dado a ser atualizado')

#Função Deletar

def deletar():
    try:
      treev_dados = tree.focus()
      treev_dicionario = tree.item(treev_dados)
      tree_lista = treev_dicionario['values']

      valor_id = [tree_lista[0]]

      deletar_info(valor_id)
      messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso') 

      for widget in frame_direita.winfo_children():
        widget.destroy()   

      mostrar()  

    except IndexError:
      messagebox.showerror('Erro', 'Selecione o dado a ser atualizado')


                                     




################# Configuração Esquerda ###############

#Nome
l_nome = Label(frame_esquerda, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_esquerda, width=35, justify='left', relief='solid')
e_nome.place(x=10, y=40)

#E-mail
l_email = Label(frame_esquerda, text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_esquerda, width=35, justify='left', relief='solid')
e_email.place(x=10, y=100)

#Telefone
l_telefone = Label(frame_esquerda, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_esquerda, width=35, justify='left', relief='solid')
e_telefone.place(x=10, y=160)

#Data inicio 
l_date = Label(frame_esquerda, text='Data de Inicio', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_date.place(x=10, y=190)
e_date = Entry(frame_esquerda, width=35, justify='left', relief='solid')
e_date.place(x=10, y=220)


#Botão inserir
b_inserir = Button(frame_esquerda, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co4, relief='raised', overrelief='ridge')
b_inserir.place(x=10, y=340)

#Botão Atualizar
b_atualizar = Button(frame_esquerda, command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co4, relief='raised')
b_atualizar.place(x=110, y=340)

#Botão Deletar
b_deletar = Button(frame_esquerda, command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co4, relief='raised')
b_deletar.place(x=210, y=340)

#Frame Direita

def mostrar():
    
    global tree

    lista = mostrar_info()

    #criando cabeçalho direita

    tabela_head = ['ID', 'NOME', 'EMAIL', 'TELEFONE', 'DATA']


    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    #vertical scroolbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    #horizontal Scroolbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, stick='nsew')
    vsb.grid(column=1, row=0, stick='ns')
    hsb.grid(column=0, row=1, stick='ew')
    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw", "center", "center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
     tree.heading(col, text=col.title(), anchor=(CENTER))

    #adjust th column's width to the header string

     tree.column(col, width=h[n])

     n+=1

    for item in lista:
     tree.insert('', 'end', values=item)


#chamando a função mostar 
mostrar()




janela.mainloop()