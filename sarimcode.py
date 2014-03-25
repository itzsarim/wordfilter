WORDLIST = [
    "maverick",
    "ranger",
    "rocket",
    "chicago",
    "bear",
    "wizard",
    "seattle",
    "atlanta",
    "miami",
    "austin",
    "boston",
    "pittsburgh",
    "heat",
    "saint",
    "hawk",
    "king"
]

storefile = []
outfile=[]

#user input

x=raw_input('enter number or text')
z=x
y=x.split()

storefile=y

temp = storefile

replacements = {'maverick':'********', 'ranger':'******', 'rocket':'******', 'king':'****', 'heat':'****'}


for src, target in replacements.iteritems():
    z=z.replace(src,target)



z=z.split()
result=[]
i=0

for line in y:
    if( line in replacements):
    
        temp=replacements[line]
	result.append(temp)
	"""        
	if(temp==z[i]):
            result.append(temp)
        else :
            result.append(line)
	"""
    else :
        
        if (z[i].count('*')==len(z[i])):
            result.append(z[i])
        else :
            result.append(line)
    i = i+1

print result
"""
for line in storefile:
    for src, target in replacements.iteritems():
        print line
    	if len(line)==len(src):
    
        	line = line.replace(src, target)
    outfile.append(line)


print outfile
"""
