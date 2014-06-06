




def bitSwapRequired( a, b) :
	
    count = 0
	
    c = a ^ b
    while c> 0:
        count+c&1
        c=c>> 1
		

    return count;
