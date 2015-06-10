import re
def convert(s):
	words = re.split('\ *', s.replace('\t', ' ').replace('\n', ' ') )
	words2 = []
	for w in words:
		if w==':': words2 += ['::=']
		elif w.upper() == w and w != '|': words2 += ['\'' + w + '\'']
		else: words2 += [w]
	return ' '.join(words2)

g2 = [convert(r) for r in g]
res = '\n\n'.join(g2)
print res
