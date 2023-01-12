subjects = {'의사소통영어':'A', '오래된 미래':'B+', '양자역학':'A0'}

student = '김도훈'
subject = '오래된 미래'

print('%s학생의 %s과목 성적은 %s입니다.' % (student, subject, subjects[subject]))
print('{}학생의 {}과목 성적은 {}입니다.'.format(student, subject, subjects[subject]))