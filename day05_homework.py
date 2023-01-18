# ch 8

# 8.11
odd_set = {i for i in range(10) if i % 2 == 1}
print(odd_set)
# 8.12
generator_ = (('Got', i) for i in range(10))
for i in generator_:
    print(*i)
# 8.13
key_tuple = ('optimist', 'pessimist', 'troll')
value_tuple = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
new_dict = dict(zip(key_tuple, value_tuple))
print(new_dict)
# 8.14
key_lst = ['Creature of Habit', "crewel Fate"]
value_lst = ['A num turns into a monster', 'A haunted yarn shop']
movies = dict(zip(key_lst, value_lst))
print(movies)