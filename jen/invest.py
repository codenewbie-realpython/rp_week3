# week three assignment 3 - jen b

def invest(amount, rate, time):
    print "principle amount: ${}".format(amount)
    print "annual rate of return:", rate
    for i in range(1, time + 1):
        amount = amount *(1 + rate)
        print "year {}:${}".format(i, amount)
    print

invest(100, .05, 8)
invest(2000, .025, 5)



