from GestoreCalcoli import *
if __name__ == '__main__':
	c=GestoreCalcoli()
	x=int(input('Inserire il primo numero: '))
	y=int(input('Inserire il secondo numero: '))
	print(f'La somma vale:{c.add(x,y)}')
	print(f'La sottrazione vale: {c.sub(x,y)}')
	print(f'La moltiplicazione vale: {c.mul(x,y)}')
	print(f'La divisione vale: {c.div(x,y)}')
