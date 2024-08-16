from tkinter.ttk import * # Importa todos os elementos do módulo ttk do pacote tkinter
from tkinter import * # Importa todos os elementos do módulo base do tkinter
from tkinter import Tk, ttk # Importa especificamente as classes tk e ttk do módulo tkinter
from PIL import Image, ImageTk # Importa as classes Image e ImageTk do módulo PIL
from tkinter import messagebox # Importa o módulo messagebox do tkinter
from datetime import date # Importa a classe date do módulo datetime
from datetime import datetime # Importa a classe datetime do módulo datetime

# Importando funções do arquivo funcoes_bd
from funcoes_bd import *

# Variável global para armazenar o botão ativo
botao_ativo = None


# Cores --------------

co0 = '#2e2d2b' # preto
co1 = '#feffff' # branco
co2 = '#4fa882' # verde
co3 = '#38576b' # azul
co4 = '#403d3d' # letra
co5 = '#e06636' # profit
co6 = '#E9A178'
co7 = '#3fbfb9' # verde
co8 = '#263238' # +verde
co9 = '#e9edf5' # +verde
co10 = '#6e8faf'
co11 = '#f2f4f2'

# Configurações dos botões com destaque
estilo_botao = {
    'bg': co2,  # Cor de fundo destacada (verde)
    'fg': co1,  # Cor da fonte (branco)
    'font': ('Ivy 11 bold'),  # Fonte em negrito
    'overrelief': RIDGE,  # Efeito ao passar o mouse
    'relief': SOLID,  # Borda sólida
    'bd': 2  # Espessura da borda
}

# Criando a função de data atual
hoje = datetime.today()

# Criando a janela

janela = Tk()
janela.title('Sistema de Biblioteca')
janela.geometry('1365x700')
janela.minsize(1365, 700)  # Define o tamanho mínimo da janela
janela.configure(background=co1)
#janela.resizable(width=FALSE, height=FALSE)
janela.resizable(width=TRUE, height=TRUE) #janela maximilizada


style = Style(janela)
style.theme_use('clam')

# Divisão da janela -------------
parte_superior = Frame(janela, height=70, bg=co3, relief='flat')
parte_superior.grid(row=0, column=0, columnspan=7, sticky=EW)
janela.grid_columnconfigure(0, weight=1)  # Permite que a parte superior se expanda horizontalmente

parte_do_meio = Frame(janela, height=40, bg=co4, relief='solid')
parte_do_meio.grid(row=1, column=0, sticky=EW)
janela.grid_columnconfigure(0, weight=1)  # Permite que a lateral esquerda se expanda horizontalmente

parte_inferior = Frame(janela, height=570, bg=co1, relief='raised')
parte_inferior.grid(row=2, column=0, sticky=EW)
janela.grid_columnconfigure(0, weight=1)  # Permite que a lateral direita se expanda horizontalmente
parte_inferior.grid_columnconfigure(0, weight=1)  # Configura a expansão horizontal dos widgets dentro de parte inferior


# Colocando o logo ------------
logo = Image.open('logo.png')
logo= logo.resize((45,45))
logo = ImageTk.PhotoImage(logo)

img_logo = Label(parte_superior, image=logo, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co3, fg=co3)
img_logo.place(x=5, y=10)

texto_logo = Label(parte_superior, text='Software Para Gestão De Bibliotecas', compound=LEFT, padx=5, anchor=CENTER, font=('Verdana 25 bold'),  bg=co3, fg=co1)
texto_logo.place(x=420, y=10)

# Criando a função que cria o menu para adicionar os dados de um novo usuário

def adicionar_usuario():
    def adicionar():  # Função para adicionar os dados preenchidos no formulário no banco de dados
        pri_nome = entrada_p_nome.get()
        ultimo_nome = entrada_sobrenome.get()
        logradouro = entrada_endereco.get()
        e_mail = entrada_email.get()
        contato = entrada_telefone.get()

        lista = [pri_nome, ultimo_nome, logradouro, e_mail, contato]

        # Verificando se os campos do formulário foram preenchidos ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos.')
                return

        # Função que insere os dados no banco de dados
        inserir_usuario(pri_nome, ultimo_nome, logradouro, e_mail, contato)
        messagebox.showinfo('Sucesso', 'Usuário adicionado com sucesso.')

        # Limpando os campos do formulário
        entrada_p_nome.delete(0, END)
        entrada_sobrenome.delete(0, END)
        entrada_endereco.delete(0, END)
        entrada_email.delete(0, END)
        entrada_telefone.delete(0, END)

    ad_usuario = Label(parte_inferior, text='**ADICIONAR UM NOVO LEITOR**', width=50, compound=LEFT, padx=5, pady=10,
                       font=('Verdana 12 bold'), bg=co7, fg=co4)
    ad_usuario.grid(row=0, column=0, columnspan=4, sticky='nsew')

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, height=1, anchor='nw', font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky='nsew')
    parte_inferior.grid_columnconfigure(0, weight=1)

    # Configuração das colunas para centralizar o conteúdo
    parte_inferior.grid_columnconfigure(0, weight=1)
    parte_inferior.grid_columnconfigure(1, weight=1)
    parte_inferior.grid_columnconfigure(2, weight=1)
    parte_inferior.grid_columnconfigure(3, weight=1)

    primeiro_nome = Label(parte_inferior, text='PRIMEIRO NOME', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    primeiro_nome.grid(row=2, column=1, padx=5, pady=5, sticky='e')

    entrada_p_nome = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_p_nome.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    sobrenome = Label(parte_inferior, text='SOBRENOME', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky='e')

    entrada_sobrenome = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_sobrenome.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    endereco = Label(parte_inferior, text='ENDEREÇO DO USUÁRIO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    endereco.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    entrada_endereco = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_endereco.grid(row=4, column=2, padx=5, pady=5, sticky='w')

    email = Label(parte_inferior, text='EMAIL DO USUÁRIO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    email.grid(row=5, column=1, padx=5, pady=5, sticky='e')

    entrada_email = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_email.grid(row=5, column=2, padx=5, pady=5, sticky='w')

    telefone = Label(parte_inferior, text='TELEFONE PARA CONTATO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    telefone.grid(row=6, column=1, padx=5, pady=5, sticky='e')

    entrada_telefone = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_telefone.grid(row=6, column=2, padx=5, pady=5, sticky='w')

    # Criando o botão salvar
    botao_salvar = Button(parte_inferior, command=adicionar, text='SALVAR', **estilo_botao, width=10)
    botao_salvar.grid(row=7, column=1, columnspan=2, pady=5, sticky='')

# Criando função para excluir usuários

def excluir_user():
    def buscar_leitor():
        termo_busca = entrada_excluir_leitor.get()
        tipo_busca = opcao_tipo_busca.get()

        if termo_busca == '':
            messagebox.showerror('Erro', 'Digite o termo de busca.')
            return

        if tipo_busca == "ID":
            leitor = buscar_usuario_por_id(termo_busca)
            resultados = [leitor] if leitor else []
        elif tipo_busca == "Nome":
            resultados = buscar_usuario_por_nome(termo_busca)
        else:
            resultados = []

        if resultados:
            for item in tree.get_children():
                tree.delete(item)
            for resultado in resultados:
                tree.insert('', 'end', values=resultado)
            botao_confirmar_exclusao.config(state=NORMAL)
        else:
            messagebox.showinfo('Informação', 'Nenhum leitor encontrado.')
            botao_confirmar_exclusao.config(state=DISABLED)

    def realizar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um leitor para excluir.')
            return
        id_leitor = tree.item(selected_item)['values'][0]

        # Verificar se o usuário possui livros emprestados
        livros_emprestados = verificar_livros_emprestados_por_usuario(id_leitor)

        if livros_emprestados:
            messagebox.showerror('Erro',
                                 f'O usuário não pode ser excluído, pois possui o livro "{livros_emprestados[0]}" emprestado.')
        else:
            excluir_usuario(id_leitor)
            messagebox.showinfo('Sucesso', 'Leitor excluído com sucesso.')
            entrada_excluir_leitor.delete(0, END)
            for item in tree.get_children():
                tree.delete(item)
            botao_confirmar_exclusao.config(state=DISABLED)

    lab_excluir = Label(parte_inferior, text='**EXCLUIR LEITORES DO SISTEMA**', width=50, compound=LEFT, padx=5,
                        pady=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co4)
    lab_excluir.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    linha = Label(parte_inferior, width=1000, height=1, anchor=CENTER, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    # Configuração das colunas para centralizar o conteúdo
    parte_inferior.grid_columnconfigure(0, weight=1)
    parte_inferior.grid_columnconfigure(1, weight=1)
    parte_inferior.grid_columnconfigure(2, weight=1)
    parte_inferior.grid_columnconfigure(3, weight=1)

    opcao_tipo_busca = StringVar(value="ID")
    tipo_label = Label(parte_inferior, text='BUSCAR POR', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    tipo_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    tipo_menu = OptionMenu(parte_inferior, opcao_tipo_busca, "ID", "Nome")
    tipo_menu.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    excluir_leitor_label = Label(parte_inferior, text='DIGITE O TERMO DE BUSCA', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    excluir_leitor_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
    entrada_excluir_leitor = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_excluir_leitor.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    botao_buscar_leitor = Button(parte_inferior, command=buscar_leitor, text='Buscar Leitor', **estilo_botao, width=10)
    botao_buscar_leitor.grid(row=4, column=1, columnspan=2, pady=5, sticky='')

    resultado_label = Label(parte_inferior, text='', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    resultado_label.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky=NSEW)

    cabecalho_lista = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']
    global tree
    tree = ttk.Treeview(parte_inferior, selectmode='browse', columns=cabecalho_lista, show='headings')

    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=6, sticky='nsew', columnspan=3)
    vsb.grid(column=3, row=6, sticky='ns')
    hsb.grid(column=0, row=7, sticky='ew', columnspan=3)
    parte_inferior.grid_rowconfigure(0, weight=12)

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=120, anchor='nw')

    botao_confirmar_exclusao = Button(parte_inferior, command=realizar_exclusao, text='Excluir Leitor', **estilo_botao,
                                      state=DISABLED, width=10)
    botao_confirmar_exclusao.grid(row=8, column=1, columnspan=2, pady=5, sticky='')


# Criando a função para ver usuários cadastrados no sistema

def ver_usuarios():
    visu_usuario = Label(parte_inferior, text='**VISUALIZAR USUÁRIOS CADASTRADOS NO SISTEMA**', width=50,
                         compound=LEFT,
                         padx=5, pady=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co4)
    visu_usuario.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, width=1000, height=1, anchor=CENTER, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibir_usuarios()

    # Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho_lista = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']

    global tree

    tree = ttk.Treeview(parte_inferior, selectmode='extended',
                        columns=cabecalho_lista, show='headings')

    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew', columnspan=4)
    vsb.grid(column=4, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew', columnspan=4)

    parte_inferior.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    for item in dados:
        tree.insert('', 'end', values=item)

# Criando função que permite excluir livros
def excluir_exemplar():
    def buscar_livro():
        termo_busca = entrada_deletar_livro.get()
        tipo_busca = opcao_tipo_busca.get()

        if termo_busca == '':
            messagebox.showerror('Erro', 'Digite o termo de busca.')
            return

        if tipo_busca == "ID":
            livro = buscar_livro_por_id(termo_busca)
            resultados = [livro] if livro else []
        elif tipo_busca == "Nome":
            resultados = buscar_livro_por_nome(termo_busca)
        else:
            resultados = []

        if resultados:
            for item in tree.get_children():
                tree.delete(item)
            for resultado in resultados:
                tree.insert('', 'end', values=resultado)
            botao_confirmar_exclusao.config(state=NORMAL)
        else:
            messagebox.showinfo('Informação', 'Nenhum livro encontrado.')
            botao_confirmar_exclusao.config(state=DISABLED)

    def realizar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um livro para excluir.')
            return
        id_livro = tree.item(selected_item)['values'][0]

        # Verificar se o livro está emprestado
        emprestado_para = verificar_usuario_com_livro_emprestado(id_livro)

        if emprestado_para:
            messagebox.showerror('Erro',
                                 f'O livro não pode ser excluído, pois está emprestado para {emprestado_para[0]} {emprestado_para[1]}.')
        else:
            excluir_livro(id_livro)
            messagebox.showinfo('Sucesso', 'Livro excluído com sucesso.')
            entrada_deletar_livro.delete(0, END)
            for item in tree.get_children():
                tree.delete(item)
            botao_confirmar_exclusao.config(state=DISABLED)

    lab_excluir = Label(parte_inferior, text='**EXCLUIR LIVROS DO SISTEMA**', width=50, compound=LEFT, padx=5, pady=10,
                        anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co4)
    lab_excluir.grid(row=0, column=0, columnspan=4, sticky='nsew')

    linha = Label(parte_inferior, height=1, anchor='nw', font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky='nsew')
    parte_inferior.grid_columnconfigure(0, weight=1)

    # Configuração das colunas para centralizar o conteúdo
    parte_inferior.grid_columnconfigure(0, weight=1)
    parte_inferior.grid_columnconfigure(1, weight=1)
    parte_inferior.grid_columnconfigure(2, weight=1)
    parte_inferior.grid_columnconfigure(3, weight=1)

    opcao_tipo_busca = StringVar(value="ID")
    tipo_label = Label(parte_inferior, text='BUSCAR POR', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    tipo_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    tipo_menu = OptionMenu(parte_inferior, opcao_tipo_busca, "ID", "Nome")
    tipo_menu.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    deletar_livro_label = Label(parte_inferior, text='DIGITE O TERMO DE BUSCA', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    deletar_livro_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
    entrada_deletar_livro = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_deletar_livro.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    botao_buscar_livro = Button(parte_inferior, command=buscar_livro, text='BUSCAR LIVRO', **estilo_botao, width=15)
    botao_buscar_livro.grid(row=4, column=1, columnspan=2, pady=5, sticky='')

    resultado_label = Label(parte_inferior, text='', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    resultado_label.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

    cabecalho_lista = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISBN']
    global tree
    tree = ttk.Treeview(parte_inferior, selectmode='browse', columns=cabecalho_lista, show='headings')

    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=6, sticky='nsew', columnspan=3)
    vsb.grid(column=3, row=6, sticky='ns')
    hsb.grid(column=0, row=7, sticky='ew', columnspan=3)
    parte_inferior.grid_rowconfigure(0, weight=12)

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=120, anchor='nw')

    botao_confirmar_exclusao = Button(parte_inferior, command=realizar_exclusao, text='EXCLUIR LIVRO', **estilo_botao,
                                      state=DISABLED, width=15)
    botao_confirmar_exclusao.grid(row=8, column=1, columnspan=2, pady=5, sticky='')

def verificar_livros_emprestados_por_usuario(id_usuario):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT livros.titulo 
        FROM livros 
        JOIN emprestimos ON livros.id = emprestimos.id_livro 
        WHERE emprestimos.id_usuario = ? AND emprestimos.data_devolucao IS NULL
    ''', (id_usuario,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado

def verificar_usuario_com_livro_emprestado(id_livro):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT usuarios.nome, usuarios.sobrenome 
        FROM usuarios 
        JOIN emprestimos ON usuarios.id = emprestimos.id_usuario 
        WHERE emprestimos.id_livro = ? AND emprestimos.data_devolucao IS NULL
    ''', (id_livro,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado


# Função para adicionar um novo livro

def novo_livro():
    def add_livro():
        title = entrada_titulo.get()
        author = entrada_autor.get()
        publisher = entrada_editora.get()
        year = entrada_ano_public.get()
        n_isbn = entrada_isbn.get()

        lista = [title, author, publisher, year, n_isbn]

        # Verificando se os campos do formulário foram preenchidos ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos.')
                return

        # Função que insere os dados no banco de dados
        inserir_livro(title, author, publisher, year, n_isbn)
        messagebox.showinfo('Sucesso', 'Livro adicionado com sucesso.')

        # Limpando os campos do formulário
        entrada_titulo.delete(0, END)
        entrada_autor.delete(0, END)
        entrada_editora.delete(0, END)
        entrada_ano_public.delete(0, END)
        entrada_isbn.delete(0, END)

    ad_livro = Label(parte_inferior, text='**ADICIONAR UM NOVO LIVRO**', width=50, compound=LEFT, padx=5, pady=10,
                     font=('Verdana 12 bold'), bg=co7, fg=co4)
    ad_livro.grid(row=0, column=0, columnspan=4, sticky='nsew')

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, height=1, anchor='nw', font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky='nsew')
    parte_inferior.grid_columnconfigure(0, weight=1)

    # Configuração das colunas para centralizar o conteúdo
    parte_inferior.grid_columnconfigure(0, weight=1)
    parte_inferior.grid_columnconfigure(1, weight=1)
    parte_inferior.grid_columnconfigure(2, weight=1)
    parte_inferior.grid_columnconfigure(3, weight=1)

    titulo = Label(parte_inferior, text='TÍTULO DO LIVRO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    titulo.grid(row=2, column=1, padx=5, pady=5, sticky='e')

    entrada_titulo = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_titulo.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    autor = Label(parte_inferior, text='AUTOR DO LIVRO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    autor.grid(row=3, column=1, padx=5, pady=5, sticky='e')

    entrada_autor = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_autor.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    editora = Label(parte_inferior, text='EDITORA', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    editora.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    entrada_editora = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_editora.grid(row=4, column=2, padx=5, pady=5, sticky='w')

    ano_public = Label(parte_inferior, text='ANO DE PUBLICAÇÃO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    ano_public.grid(row=5, column=1, padx=5, pady=5, sticky='e')

    entrada_ano_public = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_ano_public.grid(row=5, column=2, padx=5, pady=5, sticky='w')

    isbn = Label(parte_inferior, text='ISBN DO LIVRO', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    isbn.grid(row=6, column=1, padx=5, pady=5, sticky='e')

    entrada_isbn = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_isbn.grid(row=6, column=2, padx=5, pady=5, sticky='w')

    # Criando o botão salvar
    botao_salvar = Button(parte_inferior, command=add_livro, text='SALVAR', **estilo_botao, width=10)
    botao_salvar.grid(row=7, column=1, columnspan=2, pady=5, sticky='')




# Função que permitie visualizar os livros cadastrados no sistema
def visualizar_livros():
    visu_usuario = Label(parte_inferior, text='**VISUALIZAR LIVROS CADASTRADOS NO SISTEMA**', width=50, compound=LEFT,
                         padx=5, pady=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co4)
    visu_usuario.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, height=1, anchor=CENTER, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibir_livros()

    #Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho_lista = ['ID','Título','Autor','Editora','Ano de publicação','ISBN']

    global tree

    tree = ttk.Treeview(parte_inferior, selectmode='extended',
                        columns=cabecalho_lista, show='headings')

    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew', columnspan=4)
    vsb.grid(column=4, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew', columnspan=4)

    parte_inferior.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,160,110,100,50,50,100]
    n=0

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    for item in dados:
        tree.insert('', 'end', values=item)

# Função para realizar empréstimos

def fazer_emprestimo():
    global usuarios
    global livros
    usuarios = []
    livros = []

    def buscar_usuario():
        global usuarios
        termo_busca = entrada_usuario.get()
        tipo_busca = tipo_busca_usuario.get()

        if tipo_busca == "ID":
            usuario = buscar_usuario_por_id(termo_busca)
            usuarios = [usuario] if usuario else []
        else:
            usuarios = buscar_usuario_por_nome(termo_busca)

        if usuarios:
            resultado = usuarios[0]
            nome_usuario.set(f"NOME: {resultado[1]} {resultado[2]}")
            endereco_usuario.set(f"ENDEREÇO: {resultado[3]}")
            email_usuario.set(f"EMAIL: {resultado[4]}")
        else:
            messagebox.showerror('Erro', 'Usuário não encontrado.')

    def buscar_livro():
        global livros
        termo_busca = entrada_livro.get()
        tipo_busca = tipo_busca_livro.get()

        if tipo_busca == "ID":
            livro = buscar_livro_por_id(termo_busca)
            livros = [livro] if livro else []
        else:
            livros = buscar_livro_por_nome(termo_busca)

        if livros:
            resultado = livros[0]
            titulo_livro.set(f"TÍTULO: {resultado[1]}")
            autor_livro.set(f"AUTOR: {resultado[2]}")
            editora_livro.set(f"EDITORA: {resultado[3]}")
        else:
            messagebox.showerror('Erro', 'Livro não encontrado.')

    def confirmar_emprestimo():
        if tipo_busca_usuario.get() == "ID":
            user_id = entrada_usuario.get()
        else:
            user_id = usuarios[0][0] if usuarios else None

        if tipo_busca_livro.get() == "ID":
            book_id = entrada_livro.get()
        else:
            book_id = livros[0][0] if livros else None

        if not user_id or not book_id:
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return
        if not verificar_disponibilidade_livro(book_id):
            messagebox.showerror('Erro', 'O livro já está emprestado')
            return

        # Função que insere os dados no banco de dados
        realizar_emprestimos(user_id, book_id, hoje, None)
        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso.')

        # Limpar os campos do formulário
        entrada_usuario.delete(0, END)
        entrada_livro.delete(0, END)
        nome_usuario.set("")
        endereco_usuario.set("")
        email_usuario.set("")
        titulo_livro.set("")
        autor_livro.set("")
        editora_livro.set("")

    ad_emprestimo = Label(parte_inferior, text='**REALIZAR UM EMPRÉSTIMO**', width=50, compound=LEFT, padx=5, pady=10,
                          font=('Verdana 12 bold'), bg=co7, fg=co4)
    ad_emprestimo.grid(row=0, column=0, columnspan=4, sticky='nsew')

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, height=1, anchor='nw', font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky='nsew')
    parte_inferior.grid_columnconfigure(0, weight=1)

    # Configuração das colunas para centralizar o conteúdo
    parte_inferior.grid_columnconfigure(0, weight=1)
    parte_inferior.grid_columnconfigure(1, weight=1)
    parte_inferior.grid_columnconfigure(2, weight=1)
    parte_inferior.grid_columnconfigure(3, weight=1)

    # Entradas e Botões de busca para Usuário
    tipo_busca_usuario = StringVar(value="ID")
    tipo_usuario_label = Label(parte_inferior, text='BUSCAR USUÁRIO POR', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    tipo_usuario_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    tipo_usuario_menu = OptionMenu(parte_inferior, tipo_busca_usuario, "ID", "Nome")
    tipo_usuario_menu.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    entrada_usuario = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_usuario.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    buscar_usuario_button = Button(parte_inferior, command=buscar_usuario, text='BUSCAR USUÁRIO', **estilo_botao, width=15)
    buscar_usuario_button.grid(row=3, column=2, padx=5, pady=5, sticky='e')

    # Exibir informações do usuário
    nome_usuario = StringVar()
    endereco_usuario = StringVar()
    email_usuario = StringVar()

    usuario_info_label = Label(parte_inferior, textvariable=nome_usuario, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    usuario_info_label.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')
    usuario_endereco_label = Label(parte_inferior, textvariable=endereco_usuario, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    usuario_endereco_label.grid(row=5, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')
    usuario_email_label = Label(parte_inferior, textvariable=email_usuario, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    usuario_email_label.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')

    # Entradas e Botões de busca para Livro
    tipo_busca_livro = StringVar(value="ID")
    tipo_livro_label = Label(parte_inferior, text='BUSCAR LIVRO POR', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    tipo_livro_label.grid(row=7, column=1, padx=5, pady=5, sticky='e')
    tipo_livro_menu = OptionMenu(parte_inferior, tipo_busca_livro, "ID", "Nome")
    tipo_livro_menu.grid(row=7, column=2, padx=5, pady=5, sticky='w')

    entrada_livro = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_livro.grid(row=8, column=2, padx=5, pady=5, sticky='w')

    buscar_livro_button = Button(parte_inferior, command=buscar_livro, text='BUSCAR LIVRO', **estilo_botao, width=15)
    buscar_livro_button.grid(row=8, column=2, padx=5, pady=5, sticky='e')

    # Exibir informações do livro
    titulo_livro = StringVar()
    autor_livro = StringVar()
    editora_livro = StringVar()

    livro_info_label = Label(parte_inferior, textvariable=titulo_livro, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    livro_info_label.grid(row=9, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')
    livro_autor_label = Label(parte_inferior, textvariable=autor_livro, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    livro_autor_label.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')
    livro_editora_label = Label(parte_inferior, textvariable=editora_livro, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    livro_editora_label.grid(row=11, column=1, columnspan=3, padx=5, pady=5, sticky='nsew')

    # Botão para confirmar empréstimo
    botao_salvar = Button(parte_inferior, command=confirmar_emprestimo, text='SALVAR', **estilo_botao, width=10)
    botao_salvar.grid(row=12, column=1, columnspan=2, pady=5, sticky='')




# Função para ver livros emprestados
def ver_livros_emprestados():
    visu_livro_emprestado = Label(parte_inferior, text='**VISUALIZAR LIVROS EMPRESTADOS ATUALMENTE**', width=50,
                                  compound=LEFT, padx=5, pady=10, anchor=CENTER, font=('Verdana 12 bold'), bg=co7,
                                  fg=co4)
    visu_livro_emprestado.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, width=1000, height=1, anchor=CENTER, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = []
    livros_emprestados_ = exibir_livros_emprestados()

    for livro in livros_emprestados_:
        data_devolucao = livro[4]
        if data_devolucao:
            data_formatada = datetime.strptime(data_devolucao, '%Y-%m-%d %H:%M:%S.%f').strftime('%d-%m-%Y %H:%M:%S')
        else:
            data_formatada = "Ainda não devolvido"

        dado = [f'{livro[0]}', f'{livro[1]}', f'{livro[2]} {livro[3]}', data_formatada, f'{livro[5]}']
        dados.append(dado)

    # Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho_lista = ['ID','Título','Nome do usuário','Data empréstimo','Data devolução']

    global tree

    tree = ttk.Treeview(parte_inferior, selectmode='extended',
                        columns=cabecalho_lista, show='headings')

    #vertical scrollbar
    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew', columnspan=4)
    vsb.grid(column=4, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew', columnspan=4)

    parte_inferior.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","ne","ne"]
    h=[1,175,120,100,90,100,100]
    n=0

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


# Função para fazer a devolução dos livros
def devolucao_emprestimo():
    def devolver():
        emprestimo_id = entrada_id_emprestimo.get()
        data_retorno = entrada_data_devolucao.get()

        # Verificando se os campos do formulário foram preenchidos
        if not emprestimo_id or not data_retorno:
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return

        # Verificar se o empréstimo existe e se já foi devolvido
        conexao = connect()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM emprestimos WHERE id = ? AND data_devolucao IS NULL', (emprestimo_id,))
        emprestimo = cursor.fetchone()
        conexao.close()

        if not emprestimo:
            messagebox.showerror('Erro', 'Este ID de empréstimo não existe ou já foi devolvido.')
            return

        # Se o empréstimo for válido, proceder com a devolução
        devolucao_livro(emprestimo_id, data_retorno)
        messagebox.showinfo('Sucesso', 'Livro devolvido com sucesso.')

        # Limpando os campos do formulário
        entrada_id_emprestimo.delete(0, END)
        entrada_data_devolucao.delete(0, END)

    def preencher_data_hoje():
        entrada_data_devolucao.delete(0, END)
        entrada_data_devolucao.insert(0, date.today().strftime('%d-%m-%Y'))

    ad_emprestimo = Label(parte_inferior, text='**REALIZAR A DEVOLUÇÃO DE UM EMPRÉSTIMO**', width=50,
                          compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=co7, fg=co4)
    ad_emprestimo.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    # Linha que separa o texto informativo com o formulário
    linha = Label(parte_inferior, width=1000, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    id_emprestimo = Label(parte_inferior, text='DIGITE O ID DO EMPRÉSTIMO', anchor=CENTER, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
    id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky='e')

    entrada_id_emprestimo = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_id_emprestimo.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    data_devolucao = Label(parte_inferior, text='DIGITE A DATA DE DEVOLUÇÃO (FORMATO: DD-MM-AAAA)', anchor=CENTER,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
    data_devolucao.grid(row=3, column=1, padx=5, pady=5, sticky='e')

    botao_hoje = Button(parte_inferior, command=preencher_data_hoje, text='Hoje', **estilo_botao, width=10)
    botao_hoje.grid(row=3, column=3, padx=5, pady=5, sticky='w')

    entrada_data_devolucao = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=50)
    entrada_data_devolucao.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    # Criando o botão salvar
    botao_salvar = Button(parte_inferior, command=devolver, text='SALVAR', **estilo_botao, width=10)
    botao_salvar.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky='n')

# Função para controlar o menu
def controle(u):
    global botao_ativo

    # Redefinir o estilo de todos os botões do menu
    botoes_menu = [botao_usuario, botao_excluir_usuario, adicionar_livro, botao_excluir_livro, consulta_livro,
                   visualizar_usuarios, inserir_emprestimo, devolucao_livros, livro_emprestado, botao_buscar]

    for botao in botoes_menu:
        botao.config(bg=co4, fg=co1, font=('Ivy 11'))

    # Destacar o botão selecionado
    if u == 'ver_usuarios':
        botao_ativo = visualizar_usuarios
    elif u == 'adicionar_usuario':
        botao_ativo = botao_usuario
    elif u == 'delete_leitor':
        botao_ativo = botao_excluir_usuario
    elif u == 'novo_livro':
        botao_ativo = adicionar_livro
    elif u == 'delete_livro':
        botao_ativo = botao_excluir_livro
    elif u == 'visualizar_livros':
        botao_ativo = consulta_livro
    elif u == 'emprestimo':
        botao_ativo = inserir_emprestimo
    elif u == 'devolucao':
        botao_ativo = devolucao_livros
    elif u == 'ver_livros_emprestados':
        botao_ativo = livro_emprestado
    elif u == 'buscar':
        botao_ativo = botao_buscar

    botao_ativo.config(bg=co1, fg=co4, font=('Ivy 11 bold'))

    # Chamar a função correspondente
    if u == 'buscar':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        buscar()
    elif u == 'adicionar_usuario':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        adicionar_usuario()
    elif u == 'ver_usuarios':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        ver_usuarios()
    elif u == 'novo_livro':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        novo_livro()
    elif u == 'visualizar_livros':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        visualizar_livros()
    elif u == 'emprestimo':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        fazer_emprestimo()
    elif u == 'ver_livros_emprestados':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        ver_livros_emprestados()
    elif u == 'devolucao':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        devolucao_emprestimo()
    elif u == 'delete_leitor':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        excluir_user()
    elif u == 'delete_livro':
        for widget in parte_inferior.winfo_children():
            widget.destroy()
        excluir_exemplar()



# Função para buscar leitores ou livros
def buscar():
    def realizar_busca():
        termo_busca = entrada_busca.get()
        tipo_busca = opcao_tipo_busca.get()

        if tipo_busca == "Leitor":
            resultados = buscar_usuario_por_nome(termo_busca)
        elif tipo_busca == "Livro":
            resultados = buscar_livro_por_nome(termo_busca)
        else:
            messagebox.showerror('Erro', 'Selecione um tipo de busca.')
            return

        if resultados:
            for item in tree.get_children():
                tree.delete(item)
            for resultado in resultados:
                tree.insert('', 'end', values=resultado)
        else:
            messagebox.showinfo('Informação', 'Nenhum resultado encontrado.')

    busca_label = Label(parte_inferior, text='**BUSCAR LEITOR OU LIVRO**', width=50, compound=LEFT, padx=5, pady=10,
                        anchor=CENTER, font=('Verdana 12 bold'), bg=co7, fg=co4)
    busca_label.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    linha = Label(parte_inferior, width=1000, height=1, anchor=CENTER, font=('Verdana 1'), bg=co3, fg=co1)
    linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    opcao_tipo_busca = StringVar(value="Leitor")
    tipo_label = Label(parte_inferior, text='TIPO DE BUSCA', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    tipo_label.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    tipo_menu = OptionMenu(parte_inferior, opcao_tipo_busca, "Leitor", "Livro")
    tipo_menu.grid(row=2, column=2, padx=5, pady=5, sticky='w')

    busca_label = Label(parte_inferior, text='TERMO DE BUSCA', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    busca_label.grid(row=3, column=1, padx=5, pady=5, sticky='e')
    entrada_busca = Entry(parte_inferior, justify='center', relief='solid', font=('Ivy 10'), width=75)
    entrada_busca.grid(row=3, column=2, padx=5, pady=5, sticky='w')

    botao_buscar = Button(parte_inferior, command=realizar_busca, text='BUSCAR', **estilo_botao, width=10)
    botao_buscar.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky='n')

    cabecalho_lista = ['ID', 'Nome/Título', 'Sobrenome/Autor', 'Endereço/Editora', 'Email/Ano', 'Telefone/ISBN']

    global tree

    tree = ttk.Treeview(parte_inferior, selectmode='extended', columns=cabecalho_lista, show='headings')

    vsb = ttk.Scrollbar(parte_inferior, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(parte_inferior, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=7, sticky='nsew', columnspan=4)
    vsb.grid(column=4, row=7, sticky='ns')
    hsb.grid(column=0, row=8, sticky='ew', columnspan=4)

    parte_inferior.grid_rowconfigure(0, weight=12)

    for col in cabecalho_lista:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=120, anchor='nw')



parte_do_meio.grid_columnconfigure(0, weight=1)
parte_do_meio.grid_columnconfigure(1, weight=1)
parte_do_meio.grid_columnconfigure(2, weight=1)
parte_do_meio.grid_columnconfigure(3, weight=1)
parte_do_meio.grid_columnconfigure(4, weight=1)
parte_do_meio.grid_columnconfigure(5, weight=1)
parte_do_meio.grid_columnconfigure(6, weight=1)
parte_do_meio.grid_columnconfigure(7, weight=1)
parte_do_meio.grid_columnconfigure(8, weight=1)
parte_do_meio.grid_columnconfigure(9, weight=1)

# Adicione um botão no menu lateral para realizar a busca de leitor ou livro especifico
botao_buscar = Button(parte_do_meio, command=lambda:controle('buscar'), compound=LEFT, anchor=NW, text='Buscar leitor ou livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_buscar.grid(row=0, column=9, sticky=NSEW, padx=5, pady=6)

# Criando o menu interativo 
# Colocando botão para adicionar usuário

botao_usuario = Button(parte_do_meio, command=lambda:controle('adicionar_usuario'), compound=LEFT, anchor=NW, text='Cadastrar leitor', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Colocando botão para excluir usuário

botao_excluir_usuario = Button(parte_do_meio, command=lambda:controle('delete_leitor'), compound=LEFT, anchor=NW, text='Excluir leitor', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_excluir_usuario.grid(row=0, column=1, sticky=NSEW, padx=5, pady=6)


# Colocando botão para adicionar novo livro

adicionar_livro = Button(parte_do_meio, command=lambda:controle('novo_livro'), compound=LEFT, anchor=NW, text='Cadastrar livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
adicionar_livro.grid(row=0, column=2, sticky=NSEW, padx=5, pady=6)

# Colocando botão para excluir livros

botao_excluir_livro = Button(parte_do_meio, command=lambda:controle('delete_livro'), compound=LEFT, anchor=NW, text='Excluir livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_excluir_livro.grid(row=0, column=3, sticky=NSEW, padx=5, pady=6)

# Colocando botão para ver livros cadastrados na biblioteca

consulta_livro = Button(parte_do_meio,command=lambda:controle('visualizar_livros'), compound=LEFT, anchor=NW, text='Exibir livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
consulta_livro.grid(row=0, column=4, sticky=NSEW, padx=5, pady=6)

# Colocando botão para exibir usuários

visualizar_usuarios = Button(parte_do_meio, command=lambda:controle('ver_usuarios'), compound=LEFT, anchor=NW, text='Exibir usuários', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
visualizar_usuarios.grid(row=0, column=5, sticky=NSEW, padx=5, pady=6)

# Colocando botão para realizar empréstimos 

inserir_emprestimo = Button(parte_do_meio, command=lambda:controle('emprestimo'), compound=LEFT, anchor=NW, text='Realizar empréstimos', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
inserir_emprestimo.grid(row=0, column=6, sticky=NSEW, padx=5, pady=6)

# Colocando botão para realizar a devolução de livros 

devolucao_livros = Button(parte_do_meio, command=lambda:controle('devolucao'), compound=LEFT, anchor=NW, text='Devolução de livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
devolucao_livros.grid(row=0, column=7, sticky=NSEW, padx=5, pady=6)

# Colocando botão para exibir livros que estão emprestados no momento

livro_emprestado = Button(parte_do_meio, command=lambda:controle('ver_livros_emprestados'), compound=LEFT, anchor=NW, text='Livros emprestados atualmente', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
livro_emprestado.grid(row=0, column=8, sticky=NSEW, padx=5, pady=6)









janela.mainloop()
