from collections import Counter


def show_statistics(results):
    '''
    ### Saída
    Uma execução do programa proposto deve rodar 300 simulações, imprimindo no
    console os dados referentes às execuções. Esperamos encontrar nos dados as
    seguintes informações:
    * Quantas partidas terminam portime out (1000 rodadas);
    * Quantos turnos em média demora uma partida;
    * Qual a porcentagem de vitórias por comportamento dos jogadores;
    * Qual o comportamento que mais vence.
    '''
    total_FIM_DO_TEMPO = sum([1 for result in results if result["time_out"]])
    # total_time = sum([result["time_it"] for result in results])
    total_played = sum([result["played"] for result in results])
    count_vencedor = Counter()
    for result in results:
        estrategia = str(result['estrategia'])
        count_vencedor[estrategia] += 1
    # quantos turnos em media demora uma partida
    print(
        f'''Quantas partidas terminam por tempo esgotado(FIM_DO_TEMPO): '''
        f'''{total_FIM_DO_TEMPO}'''
    )
    print(
        f'''Quantos turnos em média demora uma partida: '''
        f'''{total_played / len(results):.1f}'''
    )
    print(
        f'''Qual o comportamento que mais venceu:
        {count_vencedor.most_common(1)[0][0]}
        venceu: {count_vencedor.most_common(1)[0][1]}'''
    )
    print("Qual a porcentagem de vitórias por comportamento dos jogadores")
    for estrategia, vencedor in count_vencedor.most_common():
        print("  *  ", f"{estrategia}: {(vencedor * 100)// len(results)}%")
