from pynput.mouse import listener


def writetofile(x,y):
	print("position of current mouse{0}".format({x,y}))

with listener(on_move=writetofile) as l:
	l.join()