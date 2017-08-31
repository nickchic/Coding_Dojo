list_one_a = [1,2,5,6,2]
list_two_a = [1,2,5,6,2]

list_one_b = [1,2,5,6,5]
list_two_b = [1,2,5,6,5,3]

list_one_c = ['celery','carrots','bread','milk']
list_two_c = ['celery','carrots','bread','cream']

def compareLists(x,y):
    if not len(x) == len(y):
        print "The lists are different"
    else:
        for idx in range(0,len(x)):
            if not x[idx] == y[idx]:
                print "The lists are different"
                return
        print "The lists are the same"


compareLists(list_one_a, list_two_a)
compareLists(list_one_b, list_two_b)
compareLists(list_one_c, list_two_c)
