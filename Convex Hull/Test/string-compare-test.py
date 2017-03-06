def one():
    return "blah"


if (one() == 'blahh'):
    print "Stuff is broken"
elif(one() == 'blah'):
    print "Normal comparison works"
else:
    print "Nope, find a new way"
