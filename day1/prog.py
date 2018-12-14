x = 0
saved = [0]
dupeFound = False

while not dupeFound:
	for s in open("input.txt", "r"):
		x = x + int(s)
		if x in saved:
			print(x)
			print("dupe!")
			dupeFound = True
			break
		saved.append(x)
		#print("saved: " + str(x))
	print("not found yet")

	
	