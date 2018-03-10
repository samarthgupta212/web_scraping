import urllib
import re

f=open("C:\Users\Comptech\Documents\icc_schedule.txt",'r')

line=f.readline()
j=0

a={}
s=[]
s=line

while line!='':
    while s[j]!="\n":
        j+=1
        l=j
        
    line2=line[:l-2]
    i=line[line.rfind(' '):]
    i=i.rstrip()
    i=i.lstrip()
    if i!= '':
        a.update({line2:int(i)})
        
    line=f.readline()
    s=line
    j=0

f.close()
while True:
    team1=raw_input('team1')
    team2=raw_input('team2')
    team1=team1.title()
    team2=team2.title()
    b=team1+" vs "+team2
    
    try:
        match1=a[b]
    except KeyError:
        print("Enter teams in reverse order")
    else:
        break;

        
match=15769+match1

match=str(match)

match1=str(match1)

name=raw_input("player name")

name=name.title()

name2=name.split()

name2='-'.join(name2)

name2=name2.lower()

group1=["Bangladesh","Ireland","India","Pakistan","Oman","Netherlands","New Zealand","Australia"]
group2=["Hong Kong","Afghanistan","Zimbabwe","West Indies","England","Sri Lanka","South Africa","Scotland"]   

if team1 in group1:
    group="2"
else:
    group="1"


m=0
p=0
for i in team1:
    p+=1
    if ' ' in i:
        q=p
        m+=1

if m==0:
    team1=team1[0:2+1]
else:
    team1=team1[:1]+team1[q:q+1]
    
m=0
p=0
for i in team2:
    p+=1
    if ' ' in i:
        q=p
        m+=1

if m==0:
    team2=team2[0:2+1]
else:
    team2=team2[:1]+team2[q:q+1]

team1=team1.lower()
team2=team2.lower()

s=[team1,"vs",team2]
s='-'.join(s)


url="http://www.cricbuzz.com/live-cricket-scorecard/"+match+"/"+s+"-"+match1+"th-match-super-10-group-"+group+"-icc-world-t20-2016"

htmltext=urllib.urlopen(url).read()

i=0

while i<2:
    regex='<div class="cb-col cb-col-[^.]* "><a href="/profiles/[^.]*/'+name2+'" title="View profile of '+ name + '" class="cb-text-link">'+name+'</a></div><div class="cb-col cb-col-[^.]*"><span class="text-gray">(.+?)</span>[^.]*<label>[^.]*</label>[^.]*</div><div class="cb-col cb-col-[^.]* text-right text-bold">(.+?)</div>'
    i+=1
        
pattern=re.compile(regex)
 
runs=re.findall(pattern,htmltext)

if runs[0][0]=="not out":
    print "the runs scored by {0} is {1} and he was not out".format(name,runs[0][1])
    
else:
        print "the runs scored by {0} is {1} and his wicket was taken by {2}".format(name,runs[0][1],runs[0][0])


   

    
         

