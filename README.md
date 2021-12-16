# LEARNING RML
- I should really read [the spec](https://rml.io/specs/rml/)
- Reading tutorial maps from Melissa from [09-21](https://github.com/uwlib-cams/rml/tree/master/getting_started/2021-09-21-demo) and [10-12](https://github.com/uwlib-cams/rml/tree/master/getting_started/2021-10-12-demo)

## running mapper
Running from the directory containing *both* the map `rda2bf_rml.ttl` and the logical source `rda_data.rdf`  
```
$ java -jar ~/mappertarget/mapper-all.jar -m rda2bf_rml.ttl
<http://www.example.org/aWork001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://id.loc.gov/ontologies/bibframe/Work>.
<http://www.example.org/aWork001> <http://id.loc.gov/ontologies/bibframe/title> <>.
```
or with an output file (instead of stdout):  
```
$ java -jar ~/mappertarget/mapper-all.jar -m rda2bf_rml.ttl -o bf_data.rdf
```
or, more likely, something like (also see [[1](#notes)]):
```
$ java -jar ~/ries/rmlmapper-java/target/rmlmapper-4.12.0-r358-all.jar -m hasPart.ttl -o bf_data003c0e.ttl -s turtle
```

### notes
[1] *\*Initially, for some reason I couldn't get the `-o` and `-s` options to work...*[1]\*
Error messages when attempting to use `-o` `-s` arguments when running (these went away later...without explanation?)
```
$ java -jar ~/mappertarget/mapper-all.jar -m rda2bf_rml.ttl -o bf_data.ttl -s turtle
17:46:52.238 [main] ERROR be.ugent.rml.cli.Main               .main(367) - Not a valid (absolute) IRI:
$ java -jar ~/mappertarget/mapper-all.jar -m rda2bf_rml.ttl -s turtle -o bf_data.ttl
17:47:48.837 [main] ERROR be.ugent.rml.cli.Main               .main(367) - Not a valid (absolute) IRI:
```
