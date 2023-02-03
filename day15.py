def print_poly(px):
    """
    다항식을 출력하는 함수
    :param px:
    :return:
    """
    term = len(px) - 1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if coef == 0:
            term -= 1
            continue
        if coef > 0 and not i == 0:
            poly_str += "+"
        poly_str += f'{coef}x^{term} '
        term -= 1

    return poly_str


def calc_poly(xVal, px):
    """
    계산하는 함수
    :param xVal:
    :param px:
    :return:
    """
    retValue = 0
    term = len(px) - 1

    for i in range(len(px)):
        coef = px[i]  # 계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue

px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

if __name__ == "__main__":
    p_str = print_poly(px)
    print(p_str)

    xValue = int(input("X 값 : "))

    pxValue = calc_poly(xValue, px)
    print(pxValue)


