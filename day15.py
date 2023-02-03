pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]

def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i] = None
    while not pokemons[-1]:
        pokemons.pop()

if __name__ == "__main__":
    insert_data(3, '거북왕')
    print(pokemons)
    insert_data(6, '어니부기')
    print(pokemons)

    delete_data(3)
    print(pokemons)
