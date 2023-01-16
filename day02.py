limit = 200
tweet = 'blah'*80

if diff := limit-len(tweet) >= 0:
    print("yes")
else:
    print("over", abs(diff))