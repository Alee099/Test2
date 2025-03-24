import math

file ='/home/ghazanfar/Downloads/random6.txt'
handle=open(file,'rb')
data=handle.read().split()

size=len(data)
print('File size in bytes : ',size , ' bytes')
freqlist={}

for byte in data:
    freqlist[byte]= (data.count(byte)/size)

ent=0
for freq in freqlist.values():
    ent =ent + freq * math.log(freq,2)
    
ent=abs(ent)
min_bytes=((size*ent)/8)
print('Shannon entropy (min bits per byte-character) :' ,ent)
print('Minimum possible file size is : ', min_bytes , ' bytes')
print('Efficency  = ', (min_bytes/size)*100 , ' %')