from core.database import obter_conexao

def cadastrar_livro(titulo, autor, isbn, quantidade):
    """Insere um novo livro no banco de dados."""
    conexao = obter_conexao()
    if not conexao:
        return False
    
    try:
        # O cursor é quem executa os comandos SQL dentro da conexão
        with conexao.cursor() as cursor:
            sql = """
                INSERT INTO livros (titulo, autor, isbn, quantidade_disponivel)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(sql, (titulo, autor, isbn, quantidade))
            conexao.commit() # Salva as alterações no banco de dados
            print(f"📖 Livro '{titulo}' cadastrado com sucesso!")
            return True
    except Exception as e:
        print(f"❌ Erro ao cadastrar livro: {e}")
        conexao.rollback() # Cancela a operação se der erro
        return False
    finally:
        conexao.close()

def listar_livros():
    """Busca e retorna todos os livros cadastrados."""
    conexao = obter_conexao()
    if not conexao:
        return []
    
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, titulo, autor, isbn, quantidade_disponivel FROM livros;")
            livros = cursor.fetchall() # Pega todos os resultados da consulta
            return livros
    except Exception as e:
        print(f"❌ Erro ao listar livros: {e}")
        return []
    finally:
        conexao.close()

def cadastrar_usuario(nome, email):
    """Insere um novo usuário/leitor no banco."""
    conexao = obter_conexao()
    if not conexao:
        return False
    
    try:
        with conexao.cursor() as cursor:
            sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s);"
            cursor.execute(sql, (nome, email))
            conexao.commit()
            print(f"👤 Usuário '{nome}' cadastrado com sucesso!")
            return True
    except Exception as e:
        print(f"❌ Erro ao cadastrar usuário: {e}")
        conexao.rollback()
        return False
    finally:
        conexao.close()
        
from datetime import datetime, timedelta

def listar_usuarios():
    """Busca e retorna todos os usuários cadastrados no banco."""
    conexao = obter_conexao()
    if not conexao:
        return []
    
    try:
        with conexao.cursor() as cursor:
            # Seleciona as colunas id, nome e email da tabela usuarios
            cursor.execute("SELECT id, nome, email FROM usuarios;")
            usuarios = cursor.fetchall()
            return usuarios
    except Exception as e:
        print(f"❌ Erro ao listar usuários: {e}")
        return []
    finally:
        conexao.close()

def realizar_emprestimo(id_usuario, id_livro):
    """Registra o empréstimo de um livro e reduz seu estoque."""
    conexao = obter_conexao()
    if not conexao:
        return False
    
    try:
        with conexao.cursor() as cursor:
            # 1. Verifica se o livro tem estoque disponível
            cursor.execute("SELECT quantidade_disponivel FROM livros WHERE id = %s;", (id_livro,))
            resultado = cursor.fetchone()
            
            if not resultado:
                print("❌ Livro não encontrado!")
                return False
            
            if resultado['quantidade_disponivel'] <= 0:
                print("❌ Livro esgotado no momento!")
                return False
            
            # 2. Calcula a data de devolução prevista (daqui a 14 dias)
            data_prevista = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            
            # 3. Insere o registro de empréstimo
            sql_emprestimo = """
                INSERT INTO emprestimos (id_usuario, id_livro, data_devolucao_prevista, status)
                VALUES (%s, %s, %s, 'Ativo');
            """
            cursor.execute(sql_emprestimo, (id_usuario, id_livro, data_prevista))
            
            # 4. Atualiza o estoque do livro (Subtrai 1)
            cursor.execute("""
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel - 1 
                WHERE id = %s;
            """, (id_livro,))
            
            conexao.commit()
            print(f"✅ Empréstimo registrado! Devolução prevista para: {data_prevista}")
            return True
            
    except Exception as e:
        print(f"❌ Erro ao realizar empréstimo: {e}")
        conexao.rollback()
        return False
    finally:
        conexao.close()

def registrar_devolucao(id_usuario, id_livro):
    """Finaliza um empréstimo ativo com base no Usuário e no Livro, atualizando o estoque."""
    conexao = obter_conexao()
    if not conexao:
        return False
    
    try:
        with conexao.cursor() as cursor:
            # 1. Busca um empréstimo que esteja 'Ativo' para ESSE usuário e ESSE livro
            sql_busca = """
                SELECT id FROM emprestimos 
                WHERE id_usuario = %s AND id_livro = %s AND status = 'Ativo'
                LIMIT 1;
            """
            cursor.execute(sql_busca, (id_usuario, id_livro))
            emprestimo = cursor.fetchone()
            
            if not emprestimo:
                print("❌ Nenhum empréstimo ATIVO encontrado para este Usuário e Livro!")
                return False
            
            id_emprestimo = emprestimo['id']
            
            # 2. Atualiza o status desse empréstimo específico para 'Devolvido'
            cursor.execute("UPDATE emprestimos SET status = 'Devolvido' WHERE id = %s;", (id_emprestimo,))
            
            # 3. Devolve 1 unidade ao estoque do livro
            cursor.execute("""
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel + 1 
                WHERE id = %s;
            """, (id_livro,))
            
            conexao.commit()
            print("✅ Devolução registrada e estoque atualizado com sucesso!")
            return True
            
    except Exception as e:
        print(f"❌ Erro ao registrar devolução: {e}")
        conexao.rollback()
        return False
    finally:
        conexao.close()   