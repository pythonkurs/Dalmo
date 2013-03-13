
import urllib2
import untangle

#The definition uses untangle to parse the xml-file
#It goes thorugh all the outages in NYC and counts the
#ones due to a certain reson.

def CountRepair(xml,REP):

    EscStat =  urllib2.urlopen(xml)
    html = EscStat.read()
    doc = untangle.parse(html)
    outages = doc.NYCOutages.outage

    r=0
    n=0
    OTHER=''

    for f in range(len(outages)):
        if outages[f].reason.cdata==REP:
            r+=1
        else:
            n+=1
            if outages[f].reason.cdata in OTHER:
                OTHER+=''
            else:
                OTHER+=str(outages[f].reason.cdata)+"\n"

    ANS=str(r)+" of "+str(r+n)+" outages has the reason "+str(REP) 
         
    return ANS+"\n\n"+"The other outages are:\n"+OTHER

