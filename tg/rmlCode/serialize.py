import rdflib
import os

g = rdflib.Graph()

turtle1 = g.parse("../data/level3/combo.ttl", format="turtle")

json = turtle1.serialize(format='json-ld')
nt = turtle1.serialize(format='nt')
turtle2 = turtle1.serialize(format='turtle')

#if os.path.exists('../uwlswd_vocabs/newspaperGenreList.json'):
#    os.remove('../uwlswd_vocabs/newspaperGenreList.json')

#if os.path.exists('../uwlswd_vocabs/newspaperGenreList.nt'):
#    os.remove('../uwlswd_vocabs/newspaperGenreList.nt')

file = open('../data/level3/combo2.json', 'wb')
file.write(json)
file.close()

file = open('../data/level3/combo2.nt', 'wb')
file.write(nt)
file.close()

file = open('../data/level3/combo2.ttl', 'wb')
file.write(turtle2)
file.close()