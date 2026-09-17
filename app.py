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
    print(leads)

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais..")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()