#!/usr/bin/python3
import sys
# Program to assemble reads generated randomly from mitochondrial genome.
# Run like python3 programName readsFileName
readList=[]

with open(sys.argv[1]) as fin:
    for line in fin:
        if not line.startswith('>'):
            readList.append(line.strip('\n'))

scs=readList[0]; del(readList[0])

while len(readList)>0:
    scorDict={}; print(len(readList))
    for read in readList:
        if read in scs:
            readList.remove(read); print('removed')
        else:
            for i in range(1,len(read)+1):
                readStart=read[0:i]; readEnd=read[-i:]
                scsStart=scs[0:i]; scsEnd=scs[-i:]
                if readEnd==scsStart:
                    scorDict[i]=read,read[:-i],'head'
                if readStart==scsEnd:
                    scorDict[i]=read,read[i:],'tail'

    if len(scorDict)!=0:
        if scorDict[max(scorDict)][2]=='head':
            scs=scorDict[max(scorDict)][1]+scs; print('head')
        else:
            scs=scs+scorDict[max(scorDict)][1]; print('tail')
        readList.remove(scorDict[max(scorDict)][0])
    else:
        print('No more alignments possible, breaking out with '+str(len(readList))+ ' reads unaligned..')
        break

with open(sys.argv[1]+'.assemb','w') as fout:
    print('>assemblage',scs,sep="\n",file=fout)
