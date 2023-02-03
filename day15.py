def insert(name, times):
    tmp = (name, times)
    for i in data[::-1]:
        if times >= i[1]:
            continue
        else:
            idx = data.index(i) + 1
            break
    else:
        idx = 0
    data.insert(res, tmp)


if __name__ == "__main__":
    data = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
    insert('미나', 40)
    print(data)
    insert('A', 250)
    print(data)

