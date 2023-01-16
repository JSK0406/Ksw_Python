5.4 / 5.5


letter = '''\tDear {salutation} {name},\n\n\tThank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any
{animals}.\n\n\tSend us your receipt and {amount} for shipping and handling. We will send you
another {product} taht, in our tests, is {percent}% less likely to have {verbed}.

\tThank you for your support.
\tSincerly,
\t{spokesman}
\t{job_title}'''

salutation = 'A'
name = 'B'
product = 'C'
verbed = 'D'
room = 'E'
animals = 'F'
amount = 'g'
percent = 'h'
spokesman = 'i'
job_title = 'g'


print(letter.format(salutation = salutation, name = name, \
product = product, verbed = verbed, room=room, animals=animals, amount=amount, percent=percent, spokesman=spokesman, job_title=job_title))

text1 = '%sy Mc%sface\n%sy Mc%sface\n%sy Mc%sface'%('duck', 'duck', 'gourd', 'gourd', 'spitz', 'spitz')
text2 = '{first}y Mc{first}face\n{second}y Mc{second}face\n{third}y Mc{third}face'.format(first ='duck', second ='gourd', third = 'spitz')
first = 'duck'
second = 'gourd'
third = 'spitz'
text3 = f'{first}y Mc{first}face\n{second}y Mc{second}face\n{third}y Mc{third}face'

print(text1)
print(text2)
print(text3)