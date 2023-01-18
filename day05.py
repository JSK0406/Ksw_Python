# set

set_ = {1, 3, 5}  # :없이 ,으로 구분(or set())
print(type(set_))
print(set_)

# 교집합: & 또는 a.intersection()
# 합집합: | 또는 a.union()
# 차집합: - 또는 a.difference()
# 대칭 차집합(A + B - (A & B)): ^ 또는 a.symmetric_difference()
# 부분 집합: <= 또는 a.issubset()
# 진 부분 집합: <
# 상위 집합: >= 또는 a.issuperset()

# frozenset
frozen_ = frozenset([3, 2, 1])
print(frozen_)