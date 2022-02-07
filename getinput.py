def GetInput():
	with open('in') as f:
		data = f.readlines()

		for each in data:
			yield each.strip()