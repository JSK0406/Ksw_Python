# ch 7

# 7.1 to 7.3
years_list = [1980, 1981, 1982, 1983, 1984, 1985]
print(years_list[3])
print(years_list[-1])

# 7.8 to 7.9
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise[-1].lower()[::-1].capitalize())

# 7.10
even_lst = [i for i in range(10) if i % 2 == 0]
print(even_lst)

# 7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done")
    ]
start2 = 'Someone better'

for tmp in rhymes:
    (first, second) = tmp
    print(*(i.capitalize() + '! ' for i in start1), first.capitalize() + '!', sep='')
    print(start2, second + '.')