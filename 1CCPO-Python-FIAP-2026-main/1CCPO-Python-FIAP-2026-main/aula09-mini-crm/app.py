from model import model_lead
import control


def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Etapa de vendas: ")

    # verifique e valide os campos
    # depois dos campos validados, preciso modelar os dados
    # os leads serão estruturados como dict
    print(model_lead(name, email, company, stage))

    # com os dados modelados, preciso enviá-los para o DB
    # para isso, vamos usar os métodos criados no control
    control.create_lead(model_lead(name, email, company, stage))

    print("Lead adicionado (func)")


def list_leads():
    leads = control.read_leads()

    print(f"## | {"Nome":<10} | {"E-mail":<10} | Empresa")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")


def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # vou agora enviar a busca do usuário (query) para o control
    # o control vai comparar a busca com a base de dados
    # e vai retornar uma lista com o resultado

    leads_found = control.read_leads_search(query)
    print(f"## | {"Nome":<10} | {"E-mail":<10} | Empresa")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")


def export_lead():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads")
    else:
        print(f"Exportado para {path_csv}")


def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar nome, email, empresa")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_lead()
        elif opt == "0":
            print("Até mais..")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
