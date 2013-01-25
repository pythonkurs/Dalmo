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

    for f in range(len(outages)):
        if outages[f].reason.cdata==REP:
            r+=1
        else:
            n+=1

    print r,"of",r+n,"outages has the reason",REP

    return


