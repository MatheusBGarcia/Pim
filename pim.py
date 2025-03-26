import os
import json
import bcrypt

USERS_FILE = "usuarios.json"

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

def salvar_usuarios(usuarios):
    with open(USERS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

def cadastrar_usuario(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios:
        print("Usuário já existe!")
        return
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    usuarios[username] = senha_hash
    salvar_usuarios(usuarios)
    print("Usuário cadastrado!")

def autenticar_usuario(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios and bcrypt.checkpw(senha.encode(), usuarios[username].encode()):
        return True
    return False

def login():
    while True:
        opcao = input("\n1. Cadastrar\n2. Entrar\n3. Sair\nEscolha: ")
        if opcao == "1":
            cadastrar_usuario(input("Usuário: "), input("Senha: "))
        elif opcao == "2":
            if autenticar_usuario(input("Usuário: "), input("Senha: ")):
                print("Login bem-sucedido!")
                limpar_console()
                main()
            else:
                print("Usuário ou senha incorretos!")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")


def exibir_menu():
    print("\nPágina inicial:")
    print("Olá, bem vindo a plataforma de cursos da OEIT (Organização de Estudos Independentes Tecnológicos): ")
    print("1. Vantagens e desvantagens entre os sistemas operacionais.")
    print("2. Apresentar as aplicações que serão utilizadas nos computadores da consultoria.")
    print("3. Criar gráficos com informações sobre os usuários usando média, moda e mediana.")
    print("4. Apresentar soluções para menor consumo de energia elétrica dos equipamentos de informática, bem como o descarte de equipamentos obsoletos ou com defeito.")
    print("5. Definir boas práticas de segurança digital como a criação de senhas seguras, proteção contra Phising e Backup de dados.")
    print("6. Definir às políticas de proteção de dados pessoais.")
    print("7. Definir uma estratégia de comunicação para a ONG.")
    print("8. Mini curso sobre Pensamento Lógico Computacional.")
    print("0. Sair")
    
def sistemas_operacionais():
    while True:    
        print("")
        print("Escolha umas das 7 opções a seguir para conhecer as vantagens e desvantagens sobre cada sistema operacional: ")
        print("1 = Windows")
        print("2 = macOS")
        print("3 = Linux (Ubuntu, Debian, Fedora, etc.)")
        print("4 = Android (móvel)")
        print("5 = iOS (móvel)")
        print("6 = Conclusão/Resumo")
        print("0 = Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print("")
            print("                             Windows:")
            print("✅ Vantagens:")
            print("  Grande compatibilidade com softwares e jogos.")
            print("  Interface amigável e fácil de usar.")
            print("  Suporte para uma grande variedade de hardware.")
            print("  Maior suporte técnico e documentação.")
            print("❌ Desvantagens:")
            print("  Pode ser vulnerável a vírus e ataques cibernéticos.")
            print("  Algumas versões são pesadas e exigem mais hardware.")
            print("  Licenciamento pago, aumentando o custo.")
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()

            
        elif opcao == "2":
            print("")
            print("                             macOs:")
            print("✅ Vantagens:")
            print("  Design otimizado e interface intuitiva.")
            print("  Maior estabilidade e desempenho consistente.")
            print("  Excelente integração com dispositivos Apple (iPhone, iPad, etc.).")
            print("  Segurança elevada com menos riscos de vírus.")
            print("❌ Desvantagens:")
            print("  Preço elevado dos dispositivos Apple.")
            print("  Pouca compatibilidade com jogos e softwares exclusivos de Windows.")
            print("  Menos opções de personalização.")
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()
        
        elif opcao == "3":
            print("")
            print("                             Linux:")
            print("✅ Vantagens:")
            print("  Gratuito e open-source, sem custos de licença.")
            print("  Muito seguro e estável, com menos vírus.")
            print("  Alto nível de personalização e controle.")
            print("  Ideal para servidores e programação.")
            print("❌ Desvantagens:")
            print("  Curva de aprendizado maior para iniciantes.")
            print("  Alguns programas populares não têm versão para Linux.")
            print("  Pode ter dificuldades com drivers de hardware menos comuns.")
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()

        elif opcao == "4":
            print("")
            print("                             Android(móvel):")
            print("✅ Vantagens:")
            print("  Grande variedade de dispositivos e preços.")
            print("  Personalizável, com suporte a ROMs customizadas.")
            print("  Maior compatibilidade com aplicativos e serviços do Google.")
            print("❌ Desvantagens:")
            print("  Atualizações fragmentadas e dependentes do fabricante.")
            print("  Pode ter vulnerabilidades de segurança se não for atualizado.")
            print("  Alguns modelos vêm com bloatware (apps desnecessários).")
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()

        elif opcao == "5":
            print("")
            print("                             iOS(móvel):")
            print("✅ Vantagens:")
            print("  Excelente otimização e desempenho.")
            print("  Atualizações frequentes e suporte a longo prazo.")
            print("  Maior segurança e privacidade.")
            print("❌ Desvantagens:")
            print("  Sistema fechado, pouca personalização.")
            print("  Alto custo dos dispositivos Apple.")
            print("  Depende do ecossistema da Apple para muitos serviços.")
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()

        elif opcao == "6":
            print("")
            print("                             Conclusão:")
            print("  Para jogos e trabalho corporativo, Windows é a melhor opção.")
            print("  Para design, criatividade e integração Apple, macOS se destaca.")
            print("  Para segurança, servidores e programadores, Linux é excelente.")
            print("  Para mobilidade e personalização, Android é ideal.")
            print("  Para desempenho otimizado e segurança, iOS se sobressai.")
            
            direcionamento = input("Digite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                exibir_menu()

        elif opcao == "0":
            limpar_console()
            exibir_menu()
        
        else:
            print("⚠ Opção inválida ⚠")
            break
        


def aplicacoes_computadores():
    print("")

def grafico_mmm():
    print("")

def consumo_descarte():
    print("")

def seguranca_digital():
    print("")

def mini_curso_pensamento_logico():
    while True:
        print("\nMini Curso: Pensamento Lógico Computacional")
        print("1. Introdução ao Pensamento Computacional")
        print("2. Estruturas de Decisão e Repetição")
        print("3. Algoritmos e Fluxogramas")
        print("4. Problemas e Soluções com Algoritmos")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nO pensamento computacional é a habilidade de resolver problemas de forma estruturada, dividindo tarefas complexas em partes menores e aplicando lógica para encontrar soluções.")
        elif opcao == "2":
            print("\nEstruturas de decisão (como IF-ELSE) e estruturas de repetição (como WHILE e FOR) são fundamentais na programação para definir fluxos lógicos baseados em condições e repetições de ações.")
        elif opcao == "3":
            print("\nAlgoritmos são sequências de passos para resolver problemas. Fluxogramas são representações gráficas de algoritmos que ajudam a visualizar o fluxo de execução de um programa.")
        elif opcao == "4":
            print("\nResolver problemas computacionais envolve identificar entradas, definir processos e calcular saídas desejadas. Bons algoritmos são eficientes, corretos e bem documentados.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def protecao_dados():
    while True:
        print("")
        print("A política de proteção de dados é um conjunto de diretrizes e práticas adotadas por uma organização para garantir a segurança, privacidade e integridade das informações pessoais e sensíveis que coleta, armazena e processa.")
        print("Seu objetivo é cumprir legislações como a LGPD (Lei Geral de Proteção de Dados) no Brasil e o GDPR (Regulamento Geral de Proteção de Dados) na União Europeia.")
        print("Ela inclui princípios como:")
        print("✅ Transparência – Informar aos titulares sobre o uso de seus dados.")
        print("✅ Finalidade – Coletar apenas os dados necessários para um propósito legítimo.")
        print("✅ Consentimento – Obter autorização do titular quando exigido.")
        print("✅ Segurança – Adotar medidas para proteger os dados contra acessos não autorizados e vazamentos.")
        print("✅ Direitos dos titulares – Garantir acesso, correção e exclusão dos dados quando solicitado.")
        voltar = input("Digite V para voltar a tela inicial:  ")
        if voltar == "V":
            limpar_console()
            main()
        else:
            limpar_console()
            protecao_dados()

def comunicacao_ong():
    print("")
    print("Para ter uma melhor segurança digital")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-7 ou 0 para sair): ")

        if escolha == '1':
            limpar_console()
            sistemas_operacionais()
        elif escolha == '2':
            limpar_console()
            aplicacoes_computadores()
        elif escolha == '3':
            limpar_console()
            grafico_mmm()
        elif escolha == '4':
            limpar_console()
            consumo_descarte()
        elif escolha == '5':
            limpar_console()
            seguranca_digital()
        elif escolha == '6':
            limpar_console()
            protecao_dados()
        elif escolha == '7':
            limpar_console()
            comunicacao_ong()
        elif escolha == '8':
            limpar_console
            mini_curso_pensamento_logico()
        elif escolha == '0':
            cert = input("Tem certeza que quer sair do programa? S/N ")
            if cert == "S":
                print("Saindo do programa.")
                break
            else:
                limpar_console()
                main()
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7 ou 0 para sair.")

if __name__ == "__main__":
    login()