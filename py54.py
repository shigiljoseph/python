inf=False

try:
    inf=open('new.txt','r+')
    line=inf.readlines()
    inf.seek(0,0)
    print(inf.read(),line)
    n=int(input('Enter the line to remove'))
    r=line[n]
    line.remove(r)
    inf.truncate(0)
    inf.seek(0,0)
    inf.writelines(line)
    print(inf.read())
    #print(inf.read())
except Exception as f:
    print(f,"Error occured")
finally:
    if inf:inf.close()
