def reverse_hash(h, s):
	remainder = h % 37
	print s[remainder]
	h = (h - remainder)/37
	if (h == 7):
		return ""
	return reverse_hash(h, s)

def forward_hash(s):
# should print out 680131659347 using leepadg
    h = 7
    s_letters = 'acdegilmnoprstuw'
    for i in s:
        h = (h * 37 + s_letters.index(i))
        print h
    return h

forward_hash('leepadg')
reverse_hash( 945924806726376, 'acdegilmnoprstuw' )
