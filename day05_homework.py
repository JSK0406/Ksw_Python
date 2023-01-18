# ch 9

# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())
# 9.2
def get_odds():
    return [i for i in range(10) if i % 2 ==1]
print(get_odds()[2])