strNormal=input("Digite uma string: ")
strSeparada=[i for i in strNormal]
j=len(strSeparada)-1
strInversa=[]
for i in range (len(strSeparada)):
    strInversa.append(strSeparada[j])
    j-=1
strInversa = (','.join(str(x) for x in strInversa)).replace(',','')
print(strInversa)