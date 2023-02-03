def insert_pokemon(name, hp):
    tmp = [name, hp]
    i = 0
    for i in range(len(pokemon_lst)):
        if pokemon_lst[i][1] < hp:
            break
        else:
            continue
    else:
        i += 1
    pokemon_lst.insert(i, tmp)

if __name__ == "__main__":
    check = 'A'
    pokemon_lst = [["파이리", 1000], ["꼬부기", 500], ["이상해씨", 400], ["치코리타", 300], ["이브이", 100]]
    while check != 'q':
        name = input("포켓몬 이름 : ")
        hp = int(input("포켓몬 체력 : "))
        insert_pokemon(name, hp)
        print(pokemon_lst)
        check = input("종료하려면 q / 계속하려면 q 제외 아무키나 : ")
    print("최종 결과 :", *pokemon_lst)