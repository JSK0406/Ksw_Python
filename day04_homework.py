# ch8

# 8.1 to 8.5
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f['walrus'])  # 8.2
f2e = {b: a for (a, b) in e2f.items()}
print(f2e)  # 8.3
print(f2e['chien'])  # 8.4
print(e2f.keys())  # 8.5

# 8.6 to 8.9
another = {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}
life = {'animals': another, 'plants': {}, 'other': {}}
print(life)  # 8.6
print(life.keys())  # 8.7
print(life['animals'].keys())  # 8.8
print(life['animals']['cats'])  # 8.9

# 8.10
squares = {i: i*i for i in range(10)}
print(squares)
