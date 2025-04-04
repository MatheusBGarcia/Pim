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
    print("\nOlá, bem vindo a plataforma de cursos da OEIT (Organização de Estudos Independentes Tecnológicos): ")
    print("\n1. Vantagens e Desvantagens Entre os Sistemas Operacionais.")
    print("2. Como Lidar com os Aparelhos Eletrônicos.")
    print("3. Segurança Digital.")
    print("4. Proteção de Dados Pessoais")
    print("5. Pensamento Lógico Computacional.")
    print("6. Questionário sobre os cursos.")
    print("0. Sair do Programa")
    
def sistemas_operacionais():
    while True:    
        print("\nVantagens e Desvantagens Entre os Sistemas Operacionais:")
        print("\n1 = Windows")
        print("2 = macOS")
        print("3 = Linux (Ubuntu, Debian, Fedora, etc.)")
        print("4 = Android (móvel)")
        print("5 = iOS (móvel)")
        print("6 = Conclusão/Resumo")
        print("0 = Voltar para página inicial")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_console()
            print("\nWindows:")
            print("\n✅ Vantagens:")
            print("Grande compatibilidade com softwares e jogos.")
            print("Interface amigável e fácil de usar.")
            print("Suporte para uma grande variedade de hardware.")
            print("Maior suporte técnico e documentação.")
            print("\n❌ Desvantagens:")
            print("Pode ser vulnerável a vírus e ataques cibernéticos.")
            print("Algumas versões são pesadas e exigem mais hardware.")
            print("Licenciamento pago, aumentando o custo.")
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()

            
        elif opcao == "2":
            limpar_console()
            print("\nmacOs:")
            print("\n✅ Vantagens:")
            print("  Design otimizado e interface intuitiva.")
            print("  Maior estabilidade e desempenho consistente.")
            print("  Excelente integração com dispositivos Apple (iPhone, iPad, etc.).")
            print("  Segurança elevada com menos riscos de vírus.")
            print("\n❌ Desvantagens:")
            print("  Preço elevado dos dispositivos Apple.")
            print("  Pouca compatibilidade com jogos e softwares exclusivos de Windows.")
            print("  Menos opções de personalização.")
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()
        
        elif opcao == "3":
            limpar_console()
            print("\nLinux:")
            print("\n✅ Vantagens:")
            print("  Gratuito e open-source, sem custos de licença.")
            print("  Muito seguro e estável, com menos vírus.")
            print("  Alto nível de personalização e controle.")
            print("  Ideal para servidores e programação.")
            print("\n❌ Desvantagens:")
            print("  Curva de aprendizado maior para iniciantes.")
            print("  Alguns programas populares não têm versão para Linux.")
            print("  Pode ter dificuldades com drivers de hardware menos comuns.")
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()

        elif opcao == "4":
            limpar_console()
            print("\nAndroid(móvel):")
            print("\n✅ Vantagens:")
            print("  Grande variedade de dispositivos e preços.")
            print("  Personalizável, com suporte a ROMs customizadas.")
            print("  Maior compatibilidade com aplicativos e serviços do Google.")
            print("\n❌ Desvantagens:")
            print("  Atualizações fragmentadas e dependentes do fabricante.")
            print("  Pode ter vulnerabilidades de segurança se não for atualizado.")
            print("  Alguns modelos vêm com bloatware (apps desnecessários).")
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()

        elif opcao == "5":
            limpar_console()
            print("\niOS(móvel):")
            print("\n✅ Vantagens:")
            print("  Excelente otimização e desempenho.")
            print("  Atualizações frequentes e suporte a longo prazo.")
            print("  Maior segurança e privacidade.")
            print("\n❌ Desvantagens:")
            print("  Sistema fechado, pouca personalização.")
            print("  Alto custo dos dispositivos Apple.")
            print("  Depende do ecossistema da Apple para muitos serviços.")
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()

        elif opcao == "6":
            limpar_console()
            print("\nConclusão:")
            print("\nPara jogos e trabalho corporativo, Windows é a melhor opção.")
            print("Para design, criatividade e integração Apple, macOS se destaca.")
            print("Para segurança, servidores e programadores, Linux é excelente.")
            print("Para mobilidade e personalização, Android é ideal.")
            print("Para desempenho otimizado e segurança, iOS se sobressai.")
            
            direcionamento = input("\nDigite S para ver mais sistemas operacionais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                sistemas_operacionais()
            elif direcionamento == "P":
                limpar_console()
                main()

        elif opcao == "0":
            limpar_console()
            main()
        
        else:
            print("⚠ Opção inválida ⚠")
            break
        
def consumo_descarte():
    while True:
        print("\nComo lidar com os Aparelhos Eletrônicos.")
        print("1. Redução do consumo de energia")
        print("2. Descarte de equipamentos eletrônicos")
        print("0. Voltar a página inicial")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            limpar_console()
            print("\nRedução do consumo de energia:")
            print("\nEscolher equipamentos eficientes (certificação Energy Star ou Procel).")
            print("Configurar modos de economia de energia, como suspensão ou hibernação.")
            print("Usar fontes de alimentação eficientes (certificação 80 Plus).")
            print("Trocar HDDs por SSDs e usar componentes de baixo consumo.")
            print("Desligar equipamentos inativos ou usar tomadas inteligentes.")
            print("Migrar para computação em nuvem e usar virtualização para otimizar recursos.")
            direcionamento = input("\nDigite C para ver sobre o Descarte de Equipamentos Eletrônicos ou digite P para ir a página inicial: ")
            if direcionamento == "C":
                limpar_console()
                consumo_descarte()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "2":
            limpar_console()
            print("\nDescarte de equipamentos eletrônicos:")
            print("\nDoar ou recondicionar equipamentos ainda funcionais.")
            print("Vender ou revender equipamentos usados.")
            print("Reciclar equipamentos de forma responsável, com centros especializados.")
            print("Retirar componentes reutilizáveis de equipamentos defeituosos.")
            print("Participar de programas de retorno de fabricantes para descarte adequado.")
            print("Considerar reparos em vez de descarte quando possível.")
            direcionamento = input("\nDigite D para ver sobre a Redução do Consumo de Energia ou digite P para ir a página inicial: ")
            if direcionamento == "D":
                limpar_console()
                consumo_descarte()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "0":
            limpar_console()
            main()
        else:
            print("Opção invãlida")
            limpar_console()
            consumo_descarte()
            

def seguranca_digital():
    limpar_console()
    print("\nSegurança Digital")
    print("\n1.O que é Segurança Digital?")
    print("2. Senhas Fortes e Autenticação")
    print("3. Ataques Cibernéticos e Como se Proteger")
    print("4. Protegendo Dispositivos e Redes")
    print("5. Conclusão")
    print("0. Voltar para a página inicial")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        limpar_console()
        print("\n1. O que é Segurança Digital?")
        print("\n🔹 Segurança digital é o conjunto de práticas para proteger dispositivos, redes e informações contra ameaças cibernéticas, como hackers, vírus e golpes online.")
        print("🔹 Envolve o uso de senhas seguras, autenticação de dois fatores, antivírus, criptografia e boas práticas de navegação.")
        print("\n📌 Exemplo de ameaça:")
        print("• Um site falso (phishing) imita um banco e tenta roubar suas credenciais.")
        print("• Um e-mail suspeito contém um anexo malicioso que pode instalar um vírus.")
        print("\n💡 Dica: Nunca clique em links suspeitos e sempre verifique a autenticidade dos sites antes de inserir dados pessoais.")
        direcionamento = input("\nDigite S para ver mais sobre segurança digital ou digite P para ir a página inicial: ")
        if direcionamento == "S":
            limpar_console()
            seguranca_digital()
        elif direcionamento == "P":
            limpar_console()
            main()
    elif opcao == "2":
        limpar_console
        print("\n2. Senhas Fortes e Autenticação")
        print("\n🔑 Por que senhas fortes são importantes?")
        print("Senhas fracas são facilmente descobertas por hackers usando ataques de força bruta (testando várias combinações) ou engenharia social.")
        print("\n✅ Regras para uma senha forte:")
        print("✔️ Pelo menos 12 caracteres")
        print("✔️ Letras maiúsculas e minúsculas")
        print("✔️ Números e símbolos (!, @, #, etc.)")
        print("✔️ Nada óbvio (ex: '123456', 'senha', 'meunome2024')")
        print("\n📌 Exemplo de senha fraca vs. forte:")
        print("❌ Fraca: senha123")
        print("✅ Forte: G!zD9r@M5xT2")
        print("\n🔹 Autenticação de dois fatores (2FA):")
        print("Além da senha, exige um segundo fator de autenticação (ex: SMS, app autenticador, biometria). Isso dificulta acessos não autorizados.")
        print("\n💡 Dica: Use um gerenciador de senhas para armazenar e gerar senhas seguras automaticamente.")
        direcionamento = input("\nDigite S para ver mais sobre segurança digital ou digite P para ir a página inicial: ")
        if direcionamento == "S":
            limpar_console()
            seguranca_digital()
        elif direcionamento == "P":
            limpar_console()
            main()
    elif opcao == "3":
        limpar_console()
        print("\n3. Ataques Cibernéticos e Como se Proteger")
        print("\n👾 Principais tipos de ataques:")
        print("\n1️⃣ Phishing – Golpe que engana usuários para fornecerem dados pessoais.")
        print("📌 Exemplo: Um e-mail falso dizendo que seu banco bloqueou sua conta e pedindo login.")
        print("💡 Proteção: Verifique remetentes, URLs e nunca clique em links suspeitos.")
        print("\n2️⃣ Malware (Vírus, Ransomware, Trojans, Spyware) – Softwares maliciosos que roubam ou bloqueiam seus dados.")
        print("📌 Exemplo: Um arquivo baixado infecta seu computador e rouba senhas salvas.")
        print("💡 Proteção: Use antivírus atualizado e evite baixar arquivos de fontes desconhecidas.")
        print("\n3️⃣ Ataques de Engenharia Social – Quando um hacker engana a vítima para obter informações sigilosas.")
        print("📌 Exemplo: Alguém finge ser um suporte técnico e pede sua senha.")
        print("💡 Proteção: Nunca compartilhe dados pessoais por telefone ou e-mail.")
        direcionamento = input("\nDigite S para ver mais sobre segurança digital ou digite P para ir a página inicial: ")
        if direcionamento == "S":
            limpar_console()
            seguranca_digital()
        elif direcionamento == "P":
            limpar_console()
            main()
    elif opcao == "4":
        limpar_console()
        print("\n4. Protegendo Dispositivos e Redes")
        print("\n💻 Dicas para manter seu computador e celular seguros:")
        print("\n✔️ Mantenha o sistema operacional e aplicativos atualizados")
        print("✔️ Ative um firewall para bloquear acessos não autorizados")
        print("✔️ Instale um antivírus confiável e faça varreduras periódicas")
        print("✔️ Evite redes Wi-Fi públicas para acessar dados sensíveis")
        print("\n🔒 Privacidade na Internet:")
        print("• Use um navegador seguro e configure a privacidade")
        print("• Cuidado ao compartilhar informações pessoais em redes sociais")
        print("• Utilize VPN para proteger sua conexão em redes abertas")
        print("\n💡 Dica Extra: Desative o Bluetooth e Wi-Fi quando não estiverem em uso para evitar conexões indesejadas.")
        direcionamento = input("\nDigite S para ver mais sobre segurança digital ou digite P para ir a página inicial: ")
        if direcionamento == "S":
            limpar_console()
            seguranca_digital()
        elif direcionamento == "P":
            limpar_console()
            main()
    elif opcao == "5":
        limpar_console()
        print("\nConclusão")
        print("\n🎯 A segurança digital é essencial para proteger sua privacidade e evitar prejuízos financeiros e pessoais. Aplicando essas boas práticas, você reduz os riscos de ataques e navega com mais tranquilidade.")
        print("\n🛡️ Resumo das principais dicas:")
        print("✅ Use senhas fortes e 2FA")
        print("✅ Desconfie de e-mails e links suspeitos")
        print("✅ Mantenha seus dispositivos atualizados")
        print("✅ Evite redes Wi-Fi públicas sem proteção")
        direcionamento = input("\nDigite S para ver mais sobre segurança digital ou digite P para ir a página inicial: ")
        if direcionamento == "S":
            limpar_console()
            seguranca_digital()
        elif direcionamento == "P":
            limpar_console()
            main()
    elif opcao == "0":
        limpar_console()
        main()
    else:
        limpar_console()
        print("Opção inválida! Tente novamente.")
        seguranca_digital()

def protecao_dados():
    while True:
        limpar_console()
        print("\nProteção de Dados Pessoais")
        print("\n1. 💡 O que são Dados Pessoais?")
        print("2. 💡 Por que a Proteção de Dados é Importante?")
        print("3. 💡 Como Proteger Seus Dados Pessoais?")
        print("4. 💡 A LGPD e Seus Direitos")
        print("5. 💡 Conclusão")
        print("0. Voltar a Página Inicial")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_console()
            print("\nO que são Dados Pessoais?")
            print("\n🆔 Dados pessoais são informações que identificam ou podem identificar um indivíduo.")
            print("\nTipos de Dados Pessoais:")
            print("🔹 Dados comuns: Nome, CPF, RG, endereço, telefone, e-mail.")
            print("🔹 Dados sensíveis: Origem racial ou étnica, religião, opinião política, saúde, biometria, vida sexual.")
            print("🔹 Dados anonimizados: Foram tratados de forma que não possam identificar uma pessoa diretamente.")
            print("\n📌 Exemplo:")
            print("• Seu CPF é um dado pessoal porque identifica você.")
            print("• Seu histórico médico é um dado sensível porque revela informações sobre sua saúde.")
            print("\n💡 Dica: Sempre pense antes de compartilhar seus dados, especialmente em sites e redes sociais.")
            direcionamento = input("\nDigite S para ver mais sobre Dados Pessoais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                protecao_dados()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "2":
            limpar_console()
            print("\nPor que a Proteção de Dados é Importante?")
            print("\n🔐 Proteger seus dados evita:")
            print("✔️ Golpes e fraudes (roubo de identidade, clonagem de cartão)")
            print("✔️ Vazamento de informações pessoais")
            print("✔️ Uso indevido dos seus dados por empresas sem consentimento")
            print("\n📌 Exemplo de golpe:")
            print("• Um hacker usa seus dados vazados para abrir uma conta bancária em seu nome.")
            print("• Seu número de telefone é vendido para empresas que te enviam spam sem permissão.")
            print("\n💡 Dica: Sempre leia as políticas de privacidade antes de fornecer seus dados em sites ou aplicativos.")
            direcionamento = input("\nDigite S para ver mais sobre Dados Pessoais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                protecao_dados()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "3":
            limpar_console()
            print("\nComo Proteger Seus Dados Pessoais?")
            print("\n🔑 Boas práticas de segurança:")
            print("\n✅ Senhas seguras e autenticação de dois fatores (2FA)")
            print("✔️ Use senhas longas e complexas")
            print("✔️ Não reutilize senhas em vários sites")
            print("✔️ Ative a autenticação de dois fatores sempre que possível")
            print("\n✅ Cuidado com golpes (phishing)")
            print("✔️ Desconfie de e-mails ou mensagens pedindo seus dados")
            print("✔️ Nunca clique em links suspeitos")
            print("✔️ Verifique a URL de sites antes de inserir informações")
            print("\n✅ Configurações de privacidade")
            print("✔️ Ajuste as permissões de aplicativos para não coletarem dados desnecessários")
            print("✔️ Use navegadores com proteção contra rastreamento")
            print("✔️ Não compartilhe informações pessoais em redes sociais")
            print("\n💡 Dica: Se uma empresa pedir seus dados, pergunte por que eles são necessários e como serão usados.")
            direcionamento = input("\nDigite S para ver mais sobre Dados Pessoais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                protecao_dados()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "4":
            limpar_console()
            print("\nA LGPD e Seus Direitos")
            print("\n⚖️ O que é a LGPD (Lei Geral de Proteção de Dados)?")
            print("A LGPD (Lei nº 13.709/2018) regula o uso de dados pessoais no Brasil e garante direitos aos cidadãos.")
            print("\n📌 Seus direitos como titular de dados:")
            print("✔️ Saber quais dados uma empresa tem sobre você")
            print("✔️ Solicitar a correção ou exclusão de seus dados")
            print("✔️ Revogar consentimento para uso de dados a qualquer momento")
            print("✔️ Ser informado caso seus dados sejam vazados")
            print("\n🔎 Exemplo prático:")
            print("Se uma loja online pede seu CPF para fazer uma compra, você pode perguntar se é obrigatório e para qual finalidade será usado.")
            print("\n💡 Dica: Se seus dados forem usados sem permissão, você pode registrar uma reclamação na Autoridade Nacional de Proteção de Dados (ANPD).")
            direcionamento = input("\nDigite S para ver mais sobre Dados Pessoais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                protecao_dados()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "5":
            limpar_console()
            print("\nConclusão")
            print("\n🎯 Proteger seus dados pessoais é essencial para evitar golpes, garantir privacidade e ter mais controle sobre suas informações.")
            print("\n✅ Resumo das principais dicas:")
            print("🔹 Use senhas fortes e ative autenticação de dois fatores")
            print("🔹 Evite fornecer dados sem necessidade")
            print("🔹 Desconfie de e-mails, links e mensagens suspeitas")
            print("🔹 Ajuste suas configurações de privacidade em redes sociais e aplicativos")
            print("🔹 Conheça seus direitos na LGPD e exija transparência no uso dos seus dados")
            direcionamento = input("\nDigite S para ver mais sobre Dados Pessoais ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                protecao_dados()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "0":
            limpar_console()
            main()
        else:
            limpar_console()
            print("Opção inválida! Tente novamente.")
            protecao_dados()

        

def mini_curso_pensamento_logico():
    while True:
        limpar_console()
        print("\nPensamento Lógico Computacional")
        print("1. 💡 O que é pensamento computacional?")
        print("2. 💡 Como um programa 'toma decisões' e repete ações?")
        print("3. 💡 Como transformar lógica em instruções claras?")
        print("4. 💡 Como resolver problemas de forma eficiente?")
        print("0. Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            limpar_console()
            print("\nO pensamento computacional é uma abordagem para resolver problemas de maneira estruturada e lógica, semelhante ao que ocorre em um programa de computador. Ele se baseia em quatro pilares fundamentais:")
            print("\n🔹 Decomposição: Dividir um problema complexo em partes menores e mais gerenciáveis.")
            print("🔹 Reconhecimento de padrões: Identificar semelhanças ou padrões em problemas para encontrar soluções mais eficientes.")
            print("🔹 Abstração: Focar apenas nos aspectos essenciais do problema, ignorando detalhes irrelevantes.")
            print("🔹 Algoritmos: Criar uma sequência de passos lógicos para resolver o problema.")
            print("\n📌 Exemplo:")
            print("Imagine que você quer ensinar um robô a fazer um sanduíche. Você precisa dividir essa tarefa em etapas (decomposição), identificar padrões como 'sempre colocar pão primeiro' (reconhecimento de padrões), ignorar detalhes desnecessários como 'marca do pão' (abstração) e criar uma lista de instruções precisas (algoritmos).")
            direcionamento = input("\nDigite S para ver mais sobre Pensamento Lógico ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                mini_curso_pensamento_logico()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "2":
            limpar_console()
            print("\nOs programas de computador precisam decidir qual ação tomar com base em certas condições. Isso é feito por estruturas de decisão, como o IF-ELSE:")
            print("\n📌 Exemplo (IF-ELSE em Python):")
            print(" idade = int(input('Digite sua idade: '))")
            print(" if idade >= 18:")
            print("     print('Você é maior de idade.')")
            print(" else:")
            print("     print('Você é menor de idade.')")
            print("\nAlém disso, os programas frequentemente precisam repetir ações. Isso é feito com estruturas de repetição, como os laços WHILE e FOR:")
            print("📌 Exemplo (FOR loop em Python):")
            print(" for i in range(5):")
            print("     print(f'Este é o passo {i + 1}')")
            print("\n📌 Exemplo (WHILE loop em Python):")
            print(" contador = 0")
            print(" while contador < 3:")
            print("     print(f'Contagem: {contador}')")
            print("     contador += 1")
            print("\nEssas estruturas ajudam os programas a serem dinâmicos e adaptáveis a diferentes situações.")
            direcionamento = input("\nDigite S para ver mais sobre Pensamento Lógico ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                mini_curso_pensamento_logico()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "3":
            print("\nUm algoritmo é uma sequência de passos bem definidos para resolver um problema. Ele pode ser escrito em texto (como pseudocódigo) ou representado visualmente como um fluxograma.")
            print("\n📌 Exemplo de algoritmo (pseudocódigo para fazer um café):")
            print("1. Pegar um filtro de café")
            print("2. Colocar o pó de café no filtro")
            print("3. Esquentar a água")
            print("4. Derramar a água quente sobre o pó de café")
            print("5. Esperar a filtragem")
            print("6. Servir o café na xícara")
            print("\n📌 Exemplo de fluxograma:")
            print("➡ Início → 🏺 Pegar filtro → ☕ Adicionar pó de café → 🔥 Esquentar água → 💧 Derramar água → 🕒 Esperar → 🍵 Servir café → ⏹ Fim")
            print("\nOs fluxogramas usam símbolos para representar diferentes tipos de ações:")
            print("🔹 Óvalo: Início/Fim")
            print("🔹 Retângulo: Processo (ex: calcular, preparar, misturar)")
            print("🔹 Losango: Decisão (ex: 'Se a água estiver quente, derramar no filtro')")
            print("\nEles ajudam a visualizar e planejar um algoritmo antes da implementação em código.")
            direcionamento = input("\nDigite S para ver mais sobre Pensamento Lógico ou digite P para ir a página inicial: ")
            if direcionamento == "S":
                limpar_console()
                mini_curso_pensamento_logico()
            elif direcionamento == "P":
                limpar_console()
                main()
        elif opcao == "4":
            print("\nResolver problemas computacionais envolve três etapas principais:")
            print("1️⃣ Identificar as entradas (dados de entrada do problema)")
            print("2️⃣ Definir os processos (o que deve ser feito com esses dados)")
            print("3️⃣ Determinar as saídas (o que o programa precisa exibir no final)")
            print("\n📌 Exemplo de problema:")
            print("'Queremos criar um programa que calcule a média de três notas de um aluno e diga se ele foi aprovado ou reprovado (média ≥ 7).'")
            print("🔷 Entradas: Notas do aluno")
            print("🔷 Processamento: Somar as notas, dividir por 3 e comparar com 7")
            print("🔷 Saída: Mostrar se o aluno foi aprovado ou reprovado")
            print("\n📌 Código em Python:")
            print("nota1 = float(input('Digite a primeira nota: '))")
            print("nota2 = float(input('Digite a segunda nota: '))")
            print("nota3 = float(input('Digite a terceira nota: '))")
            print("\nmedia = (nota1 + nota2 + nota3) / 3")
            print("\nif media >= 7:")
            print("     print(f'Aprovado! Média: {media:.2f}')")
            print("else:")
            print("     print(f'Reprovado. Média: {media:.2f}')")
            print("\n🔎 Boas práticas na criação de algoritmos:")
            print("✅ Clareza e simplicidade na lógica")
            print("✅ Eficiência (evitar cálculos desnecessários)")
            print("✅ Código bem documentado e organizado")
        elif opcao == "0":
            limpar_console()
            main()
        else:
            limpar_console()
            print("Opção inválida! Tente novamente.")
            mini_curso_pensamento_logico()

def questionario():
    print("Bem-vindo ao questionário desse curso!")
    print("Por favor, responda as perguntas a seguir:\n")

    perguntas = [
        "1. Qual é o melhor sistema operacional para a programação?",
        "2. Qual dessas senhas é considerada fraca?",
        "3. Qual desses comandos é uma estrutura de decisão?",
        "4. O que é um Phising",
        "5. Qual é a importância da criptografia na proteção de dados?",
        "6. Como funciona a autenticação de dois fatores (2FA) e por que ela é recomendada?",
        "7. Qual é o melhor sistema operacional para mobilidade e personalização?",
        "8. Quem pintou a Mona Lisa?",
        "9. Qual é a língua mais falada do mundo?",
        "10. Qual é o maior oceano do mundo?"
    ]

    alternativas = [
        ["A) Linux", "B) Windows", "C) macOS", "D) Android (móvel)", "E) iOS (móvel)"],
        ["A) gR.2025", "B) 1290Kain!", "C) 0hAppY0_", "D) senha123", "E) 1001ALKs?"],
        ["A) WHILE", "B) FOR", "C) IF", "D) PRINT", "E) RETURN"],
        ["A) Golpe que engana usuários para fornecerem dados pessoais.", "B) Um vírus que queima o computador", "C) Um anti-vírus", "D) Um roteador Wi-Fi", "E) É uma linguagem de programação"],
        ["A) A criptografia melhora a velocidade da transmissão de dados na internet.", "B) B) A criptografia garante que apenas pessoas autorizadas possam acessar as informações, protegendo contra acessos não autorizados.", "C) A criptografia substitui completamente a necessidade de senhas e autenticação.", "D) D) A criptografia serve apenas para ocultar informações temporariamente, sem garantir segurança real.", "E) A criptografia só é útil para grandes empresas e não tem aplicação para usuários comuns."],
        ["A) A 2FA é um processo onde o usuário precisa fornecer apenas um código enviado por e-mail.", "B) A 2FA exige dois tipos diferentes de informação: algo que o usuário sabe (como uma senha) e algo que ele possui (como um código gerado ou enviado para um dispositivo).", "C) A 2FA requer que o usuário faça login duas vezes com a mesma senha para garantir a segurança.", "D) A 2FA exige apenas uma senha forte para acessar a conta e não envolve verificação adicional.", "E) A 2FA é recomendada apenas para usuários de aplicativos bancários e não para serviços online comuns."],
        ["A) Windows", "B) macOS", "C) iOS(móvel)", "D) Linux", "E) Android(móvel)"],
        ["A) Leonardo da Vinci", "B) Michelangelo", "C) Van Gogh", "D) Picasso", "E) Rembrandt"],
        ["A) Mandarim", "B) Inglês", "C) Espanhol", "D) Hindi", "E) Árabe"],
        ["A) Pacífico", "B) Atlântico", "C) Índico", "D) Ártico", "E) Antártico"]
    ]

    respostas_certas = ['A', 'D', 'C', 'A', 'B', 'B', 'E', 'A', 'A', 'A']
    nota_total = 0

    for i in range(len(perguntas)):
        print(perguntas[i])
        for alternativa in alternativas[i]:
            print(alternativa)
        resposta = input("Escolha uma alternativa (A, B, C, D ou E): ").strip().upper()
        
        while resposta not in ['A', 'B', 'C', 'D', 'E']:
            print("Alternativa inválida. Tente novamente.")
            resposta = input("Escolha uma alternativa (A, B, C, D ou E): ").strip().upper()
        
        # Atribui nota 10 para resposta correta e 0 para resposta errada
        if resposta == respostas_certas[i]:
            nota_total += 10
        else:
            nota_total += 0  # Pode ser ajustado para dar notas parciais se desejado

    print(f"\nObrigado por participar do questionário! Sua nota total é: {nota_total}/100")

def main():
    while True:
        exibir_menu()
        escolha = input("\nEscolha uma opção (1-6 ou 0 para sair): ")

        if escolha == '1':
            limpar_console()
            sistemas_operacionais()
        elif escolha == '2':
            limpar_console()
            consumo_descarte()
        elif escolha == '3':
            limpar_console()
            seguranca_digital()
        elif escolha == '4':
            limpar_console()
            protecao_dados()
        elif escolha == '5':
            limpar_console()
            mini_curso_pensamento_logico()
        elif escolha == "6":
            limpar_console()
            questionario()
        elif escolha == '0':
            cert = input("Tem certeza que quer sair do programa? S/N ")
            if cert == "S":
                print("Saindo do programa...")
                break
            else:
                limpar_console()
                main()
        else:
            limpar_console()
            print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 7 ou 0 para sair.")
            main()

if __name__ == "__main__":
    login()