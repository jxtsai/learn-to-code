def doing(*nums):
    '''
      aster * 表示不確定此 function 所要求的 參數有多少個 
    '''

    return sum(filter(lambda x: x > 3, nums))

test = doing(4, 2, 5, 1)
print(test)