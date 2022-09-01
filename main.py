def request_input():
    dia = int(input('insira o dia\n'))
    if dia > 31 or dia <= 0:
        print("Dia inválido!")
        request_input()
        return
    
    mes = int(input('insira o mes\n'))
    if mes <= 0 or mes > 12:
        print("Mês inválido!")
        request_input()
        return
        
    ano = int(input('insira o ano\n'))
    print(f"Dia {dia} de " + pegar_nome_do_mes(mes) + f" de {ano}")

def pegar_nome_do_mes(mes):
    return {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
}[mes]

request_input()