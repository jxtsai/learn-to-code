def byreverse(data):
    data_list = []
    for i in range(len(data)//4):
        data_list.append(data[i*4:(i+1)*4])

    return data_list


test = byreverse([1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0])


print(test)
