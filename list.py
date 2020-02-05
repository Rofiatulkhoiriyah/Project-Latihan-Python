matriks = {'dict1 ':[1,2,3],
           'dict2 ':[4,5,6],
           'dict3 ':[7,8,9]}
row = {'dict1':[1,2,3],
        'dict2':[4,5,6],
        'dict3':[7,8,9]}
hasil = {
    'dict1' :(matriks['dict1'][0]+row['dict1'][0],matriks['dict2'][0]+row['dict2'][0],matriks['dict3'[0]+row]['dict3'][0]),
    'dict2' :(matriks['dict1'][1]+row['dict1'][1],matriks['dict2'][1]+row['dict2'][1],matriks['dict3'[1]+row]['dict3'][1]),
    'dict3' :(matriks['dict1'][2]+row['dict1'][2],matriks['dict2'][2]+row['dict2'][2],matriks['dict3'[2]+row]['dict3'][2])
}
print(hasil.get('dict1'))
print(hasil.get('dict2'))
#print(hasil.get('dict3'))