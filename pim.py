import os

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
                sistemas_operacionais()
            elif direcionamento == "P":
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
                sistemas_operacionais()
            elif direcionamento == "P":
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
                sistemas_operacionais()
            elif direcionamento == "P":
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
                sistemas_operacionais()
            elif direcionamento == "P":
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
                sistemas_operacionais()
            elif direcionamento == "P":
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
                sistemas_operacionais()
            elif direcionamento == "P":
                exibir_menu()

        elif opcao == "0":
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
            break
        else:
            protecao_dados()

def comunicacao_ong():
    print("")

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
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-7 ou 0 para sair): ")

        if escolha == '1':
            sistemas_operacionais()
        elif escolha == '2':
            aplicacoes_computadores()
        elif escolha == '3':
            grafico_mmm()
        elif escolha == '4':
            consumo_descarte()
        elif escolha == '5':
            seguranca_digital()
        elif escolha == '6':
            protecao_dados()
        elif escolha == '7':
            comunicacao_ong()
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7 ou 0 para sair.")

if __name__ == "__main__":
    main()