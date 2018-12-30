medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida,cm,mm))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida * 1
dm = medida * 10
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}m'.format(m))
print('{}dm'.format(dm))

