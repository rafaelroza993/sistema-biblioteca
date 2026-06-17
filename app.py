from core.queries import (
    cadastrar_livro, listar_livros, cadastrar_usuario, 
    realizar_emprestimo, registrar_devolucao, listar_usuarios  # ⬅️ Adicionamos o import aqui
)

def exibir_menu():
    print("\n" + "="*30)
    print("      SISTEMA BIBLIOTECA      ")
    print("="*30)
    print("[1] Cadastrar Novo Livro")
    print("[2] Listar Todos os Livros")
    print("[3] Cadastrar Novo Usuário")
    print("[4] Pegar Livro Emprestado")
    print("[5] Devolver Livro")
    print("[6] Listar Todos os Usuários")  # ⬅️ Nova opção visualizada no menu
    print("[0] Sair do Sistema")
    print("="*30)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRO DE LIVRO ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN (Único): ")
            qtd = int(input("Quantidade: "))
            cadastrar_livro(titulo, autor, isbn, qtd)

        elif opcao == "2":
            print("\n--- LIVROS CADASTRADOS ---")
            livros = listar_livros()
            if not livros:
                print("Nenhum livro encontrado.")
            for livro in livros:
                print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Estoque: {livro['quantidade_disponivel']}")

        elif opcao == "3":
            print("\n--- CADASTRO DE USUÁRIO ---")
            nome = input("Nome do Leitor: ")
            email = input("E-mail (Único): ")
            cadastrar_usuario(nome, email)

        elif opcao == "4":
            print("\n--- NOVO EMPRÉSTIMO ---")
            id_usuario = int(input("ID do Usuário: "))
            id_livro = int(input("ID do Livro: "))
            realizar_emprestimo(id_usuario, id_livro)

        elif opcao == "5":
            print("\n--- DEVOLUÇÃO DE LIVRO ---")
            id_usuario = int(input("ID do Usuário: "))
            id_livro = int(input("ID do Livro: "))
            registrar_devolucao(id_usuario, id_livro)  # ⬅️ Agora passamos os dois IDs

        # ⬇️ NOVA LÓGICA DA OPÇÃO 6 ADICIONADA AQUI
        elif opcao == "6":
            print("\n--- USUÁRIOS CADASTRADOS ---")
            usuarios = listar_usuarios()
            if not usuarios:
                print("Nenhum usuário encontrado.")
            for usuario in usuarios:
                print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | E-mail: {usuario['email']}")

        elif opcao == "0":
            print("\nFechando o sistema... Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()