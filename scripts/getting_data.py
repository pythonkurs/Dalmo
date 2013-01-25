import urllib2
import untangle

EscStat =  urllib2.urlopen('http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml')
html = EscStat.read()

def CountRepair(xml):
    doc = untangle.parse(xml)
    outages = doc.NYCOutages.outage

    r=0
    n=0

    for f in range(len(outages)):
        if outages[f].reason.cdata=='REPAIR':
            r+=1
        else:
            n+=1

    print r,"of",r+n,"outages has the reason repair"

    return

CountRepair(html)
