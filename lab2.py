def module_ListFunction(L):
    print('The maximun value of the list is :',max(L))
    print('The minimum value of the list is :',min(L))
    print('The sum of the list is :',sum(L))
    sum=0
    for i in L:
        sum=sum+i
        
    avg=(sum/len(L))
    print('The average value of the list is :',avg)
    
