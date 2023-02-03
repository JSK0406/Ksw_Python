pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]

def insert_data(idx, pokemon):
    """
    선형 리스트 특정 위치에 삽입
    :param idx:
    :param pokemon:
    :return:
    """
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    """
    선형 리스트 원소 삭제
    :param idx:
    :return:
    """
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i] = None
    while not pokemons[-1]:
        pokemons.pop()

def add_data(pokemon):
    """
    선형 리스트 맨 뒤에 원소 삽입
    :param pokemon:
    :return:
    """
    pokemons.append(None)
    pokemons[-1] = pokemon

if __name__ == "__main__":
    # insert_data(3, '거북왕')
    # print(pokemons)
    # insert_data(6, '어니부기')
    # print(pokemons)
    #
    # delete_data(3)
    # print(pokemons)
    #
    # add_data("터검니")
    # print(pokemons)

    select = -1
    pokemons = []

    while select != 4:

        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (select == 1):
            poke = input("추가할 데이터--> ")
            add_data(poke)
            print(pokemons)
        elif (select == 2):
            pos = int(input("삽입할 위치--> "))
            poke = input("추가할 데이터--> ")
            insert_data(pos, poke)
            print(pokemons)
        elif (select == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif (select == 4):
            print(pokemons)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue