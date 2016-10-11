Temp = [('barium',56),('beryllium',4),('calcium',20),('magnesium',12),('radium',88),('strintium',38)]

sort = sorted(Temp, key=lambda x : x[1], reverse = True)
print(sort[0][1])

print(sorted(Temp, key=lambda x : x[1]))

temp_dict = {x:y for (x,y) in Temp}
print (temp_dict)

noble_gases = {'helium':2,'neon':10,'argon':18,'krypton':36,'xenon':54,'radon':86}

tmp = dict()
tmp.update(temp_dict)
tmp.update(noble_gases)
print(sorted(tmp.items()))

