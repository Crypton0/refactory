import turtle # karena bukan 'import turtle from *' maka class 'turtle' selalu dipanggil

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'white']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
	t.pencolor(colors[x%6])		# bisa diganti 7, sesuai index array colors
	t.width(x/100 + 1)			# tebal dari pencolor
	t.forward(x)
	t.left(59)

