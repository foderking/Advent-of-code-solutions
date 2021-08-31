import functools, re
pos=[]

fil = open('/home/fenix/advent/in').readlines()
n = functools.reduce(lambda x, y: x + y, fil)
vals = n.split('\n\n')

def validchecker(ar):

	if not re.search( r'byr:(\d{4})', ar):
		return 'Invalid'
	else:
		if not (1920 <= int(re.search( r'byr:(\d{4})', ar).group(1)) <= 2002):
			return 'Invalid'

	if not re.search( r'iyr:(\d{4})', ar):
		return 'Invalid'
	else:
		if not (2010 <= int(re.search( r'iyr:(\d{4})', ar).group(1)) <= 2020):
			return 'Invalid'

	if not re.search( r'eyr:(\d{4})', ar):
		return 'Invalid'
	else:
		if not (2020 <= int(re.search( r'eyr:(\d{4})', ar).group(1)) <= 2030):
			return 'Invalid'

	if not re.search( r'hcl:#[a-f0-9]{6}', ar):
		return 'Invalid'

	if not re.search( r'ecl:(?:amb|blu|brn|gry|grn|hzl|oth)', ar):
		return 'Invalid'

	if not re.search( r'pid:\d{9}', ar):
		return 'Invalid'


	if not re.search( r'hgt:\d+(?:cm|in)', ar):
		return 'Invalid'
	else:
		if re.search( r'hgt:\d+(cm|in)', ar).group(1) == 'cm':
			if not (150 <= int(re.search( r'hgt:(\d+)(?:cm|in)', ar).group(1) ) <= 193):
				return 'Invalid'
		else:
			if not (59 <= int(re.search( r'hgt:(\d+)(?:cm|in)', ar).group(1) ) <= 76):
				return 'Invalid'

	return 'Valid'






for i in vals:
	pos.append(validchecker(i))

print(pos.count('Valid'))