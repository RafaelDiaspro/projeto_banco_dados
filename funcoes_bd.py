import sqlite3

# Função que permite conectar ao banco de dados
def connect():
    conexao = sqlite3.connect('dados.db')
    
    # Criar a tabela de livros se não existir
    conexao.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT,
                        autor TEXT,
                        editora TEXT,
                        ano_publicacao INTEGER,
                        isbn TEXT NULL)''')

    # Criar a tabela de usuarios se não existir
    conexao.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        sobrenome TEXT,
                        endereco TEXT,
                        email TEXT,
                        telefone TEXT)''')

    # Criar a tabela de empréstimos se não existir
    conexao.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                        id INTEGER PRIMARY KEY,
                        id_livro INTEGER,
                        id_usuario INTEGER,
                        data_emprestimo TEXT,
                        data_devolucao TEXT,
                        FOREIGN KEY(id_livro) REFERENCES livros(id),
                        FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')

    return conexao

# Função que permite inserir livros na tabela no banco de dados

def inserir_livro(titulo, autor, editora, ano_publicacao, isbn):
    conexao = connect()
    conexao.execute('INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES(?, ?, ?, ?, ?)', (titulo, autor, editora, ano_publicacao, isbn))
    conexao.commit() # Permite que a operação, no caso a inserção dos livros se tornem permanentes
    conexao.close() # Para fechar o banco de dados


# Função que permite inserir usuários na tabela no banco de dados

def inserir_usuario(nome, sobrenome, endereco, email, telefone):
    conexao = connect()
    conexao.execute('INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES(?, ?, ?, ?, ?)',(nome, sobrenome, endereco, email, telefone))
    conexao.commit() # Permite que a operação, no caso a inserção dos usuarios se tornem permanentes
    conexao.close()

# Função que permite visualizar livros registrados na tabela no banco de dados 

def exibir_usuarios():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios 


# Função que permite exibir os livros registrados no banco de dados

def exibir_livros():
    conexao = connect()
    livros = conexao.execute('SELECT * FROM livros').fetchall()
    conexao.close()
    
    return livros

# Função que permite realizar empréstimos

def realizar_emprestimos(id_usuario, id_livro, data_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute('INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(?, ?, ?, ?)',(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conexao.commit()
    conexao.close()

# Função que permite exibir os livros emprestados 

def exibir_livros_emprestados():
    conexao = connect()
    resutado = conexao.execute('SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao FROM livros\
                                INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                               INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                               WHERE emprestimos.data_devolucao IS NULL').fetchall()
    conexao.close()
    return resutado


# Função para realizar de devolução dos livros

def devolucao_livro(id_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute('UPDATE emprestimos SET data_devolucao = ? WHERE id = ?', (data_devolucao,id_emprestimo))
    conexao.commit()
    conexao.close()


# Função que permite excluir usuários da tabela 

def excluir_usuario(id_usuario):
    conexao = connect()
    conexao.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
    conexao.commit()
    conexao.close()



# Função que permite excluir livros da tabela

def excluir_livro(id_livro):
    conexao = connect()
    conexao.execute('DELETE FROM livros WHERE id = ?', (id_livro,))
    conexao.commit()
    conexao.close()

# Função para buscar um usuário por ID
def buscar_usuario_por_id(id_usuario):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id_usuario,))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

# Função para buscar um livro por ID
def buscar_livro_por_id(id_livro):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros WHERE id = ?', (id_livro,))
    livro = cursor.fetchone()
    conexao.close()
    return livro

# Função para buscar usuários por nome
def buscar_usuario_por_nome(nome_usuario):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome LIKE ?', ('%' + nome_usuario + '%',))
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

# Função para buscar livros por nome
def buscar_livro_por_nome(nome_livro):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros WHERE titulo LIKE ?', ('%' + nome_livro + '%',))
    livros = cursor.fetchall()
    conexao.close()
    return livros

# Função para verificar se o livro está disponível para empréstimo
def verificar_disponibilidade_livro(book_id):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM emprestimos WHERE id_livro = ? AND data_devolucao IS NULL", (book_id,))
    resultado = cursor.fetchone()
    conexao.close()

    return not resultado  # Retorna True se não houver empréstimos ativos para o livro


# Testando as funções
#inserir_livro('Shingeki no Kyojin', 'Hajime Isayama', 'Panini', '2013', '1557896546')
#inserir_usuario('Rafael', 'Dias', 'Rua Capitão Gomes, Cipotânea', 'rafaeldepaulo2011@hotmail.com', '985741256')
#realizar_emprestimos(5,6, '2024-08-10', None)
#print(exibir_livros_emprestados())
#exibir_livros()



