stringsfiles=open("love.txt")
outputfile=("output_love.txt","w")
phrase=""
for line in stringsfiles:
    phrase+=" "+ line
    
print(phrase,file=outputfile)
outputfile.close()