# Sistema de cadastro de turmas
VALID_AREAS = ["Matemática", "História", "Inglês"]
VALID_DAYS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
VALID_SCHEDULES = ["M", "N", "T"]
DATA_FILE_PATH = "classes_data.csv"
registered_classes = []


def update_database():
    with open(file=DATA_FILE_PATH, mode="w", encoding="utf-8") as classes_data_file:
        lines_to_add = []
        for registered_class in registered_classes:
            current_class = registered_class['class_subject']
            current_class_data = registered_class['class_data']
            formatted_data_to_csv = f"{current_class},{current_class_data['area']},{current_class_data['day']},{current_class_data['class_schedules']}\n"
            lines_to_add.append(formatted_data_to_csv)
        classes_data_file.writelines(lines_to_add)


def check_data(valid_entries: list, user_entry: str) -> bool:
    # Verificar se os dados inseridos pelo usuário realmente estão dentro do escopo do programa.
    if user_entry not in valid_entries:
        # print("Insira somente uma das opções apresentadas.")
        return False
    else:
        return True


def validate_data(area: str, day: str, class_time: str) -> list:
    # Esta função trata os dados organizando-os em forma de dicionários para que
    dict_area = {'user_entry': area, 'valid_areas': VALID_AREAS}
    dict_day = {'user_entry': day, 'valid_areas': VALID_DAYS}
    dict_schedules = {'user_entry': class_time, 'valid_areas': VALID_SCHEDULES}
    data_compare = [dict_area, dict_day, dict_schedules]
    # Esta lista é composta pelo resultado do retorno de cada valor da lista a cima
    result_list = [check_data(valid_entries=item['valid_areas'], user_entry=item['user_entry']) for item in
                   data_compare]
    return result_list  # Lista com os valores True ou False


def remove_class():
    # Verificar se há turmas cadastradas
    if len(registered_classes) > 0:
        list_registered_classes()
        resposta = int(input("\n❓QUAL O NÚMERO DA TURMA QUE DESEJA EXCLUIR: ")) - 1
        if resposta < 0 or resposta > len(registered_classes):
            # Verifica se o número da turma inserido corresponde ao número de turmas cadastradas
            print("⚠️OPÇÃO INVÁLIDA⚠️")
            remove_class()
        else:
            registered_classes.pop(resposta)  # Remove a turma através do índice
            update_database()
            print("✅TURMA EXCLUÍDA COM SUCESSO!✅")
    else:
        print("\n⚠️NÃO HÁ TURMAS CADASTRADAS⚠️")


# Listagem dos dados da turma
def list_registered_classes():
    if len(registered_classes) == 0:
        print("\n⚠️NÃO HÁ TURMAS CADASTRADAS⚠️")
    else:
        print(f"\n{'TURMAS CADASTRADAS' if len(registered_classes) > 1 else 'TURMA CADASTRADA:'}")
        for class_index in range(len(registered_classes)):
            # Estas variáveis são responsáveis apenas para facilitar a compreensão do código
            current_class = registered_classes[class_index]
            sub_data = current_class['class_data']
            ##########################################
            texto_formatado = f"-->📖TURMA {class_index + 1}:\nASSUNTO: {current_class['class_subject']}" \
                              f"\nÁREA: {sub_data['area']} | " \
                              f"DIA: {sub_data['day']} | " \
                              f"TURNO: {sub_data['class_schedules']}"
            print(texto_formatado)


def check_if_class_already_exists(class_to_check: dict) -> bool:
    for registered_class in registered_classes:
        if class_to_check['class_data'] == registered_class['class_data']:
            return True
        else:
            return False


def format_class_data(theme: str, area: str, day: str, class_time: str) -> dict:
    # Esta função formata os dados inseridos pelo usuário e retorna um dicionário
    formatted_class_data = {"class_subject": theme,
                            "class_data": {"area": area, "day": day, "class_schedules": class_time}}
    return formatted_class_data


def register_new_class():
    print("⬇️ INSIRA A BAIXO OS DADOS DA TURMA QUE DESEJA CADASTRAR ⬇️")
    # Recebe os dados do usuário
    class_theme = input("ASSUNTO: ").capitalize().strip()
    area = input("ÁREA: matemática | história | inglês: ").capitalize().strip()
    day = input("DIA: segunda | terça | quarta | quinta | sexta: ").capitalize().strip()
    class_time = input("TURNO: [M] manhã | [T] tarde | [N] noite: ").upper().strip()

    # Verifica se os dados inseridos estão de acordo com os dados apresentados (Tratamento).
    data_verification = validate_data(area=area, day=day, class_time=class_time)

    if False in data_verification:
        print("⛔ VOCÊ INSERIU ALGUM DADO INVÁLIDO! POR FAVOR TENTE CADASTRAR NOVAMENTE.⛔")
        register_new_class()
    else:
        # Formatação dos dados em dicionário
        formatted_class_data = format_class_data(theme=class_theme, area=area, day=day, class_time=class_time)
        # Verifica se já existe uma turma da mesma área cadastrada no mesmo horário.
        already_exists = check_if_class_already_exists(formatted_class_data)
        if already_exists:
            print(f"\n⚠️TURMA DE {area.upper()} JÁ CADASTRADA NESTE TURNO⚠️")
            register_new_class()
        else:
            registered_classes.append(formatted_class_data)
            update_database()
            print("\n✅TURMA CADASTRADA COM SUCESSO!✅")


with open(file=DATA_FILE_PATH, mode="r", encoding="utf-8") as classes_data:
    for line in classes_data.readlines():
        data_as_list = line.strip().split(",")
        data_as_list_formatted = format_class_data(theme=data_as_list[0], area=data_as_list[1], day=data_as_list[2],
                                                   class_time=data_as_list[3])

        registered_classes.append(data_as_list_formatted)

# MENU INICIAR - Controla o funcionamento do programa
is_on = True
while is_on:
    # Breve explicação a respeito do funcionamento do programa
    option = input(
        "\n\033[1mMenu\033[1m\n[1] - Cadastrar Nova Turma\n[2] - Remover Turma\n[3] - Listar turmas\n[0] - "
        "Sair\nEscolha uma opção: ").strip()

    # Funções a serem executadas dependendo da escolha do usuário.
    if option == "1":
        register_new_class()
    elif option == "2":
        remove_class()
    elif option == "3":
        list_registered_classes()
    elif option == "0":
        is_on = False
    else:
        print("Opção inválida")
