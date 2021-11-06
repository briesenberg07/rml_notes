# LEARNING RML
- I should really read [the spec](https://rml.io/specs/rml/)
- Reading tutorial maps from Melissa from [09-21](https://github.com/uwlib-cams/rml/tree/master/getting_started/2021-09-21-demo) and [10-12](https://github.com/uwlib-cams/rml/tree/master/getting_started/2021-10-12-demo)

## 4rdardf - test mappings and test data
| desc. | test input | test map | test output | comments/notes |
|---|---|---|---|---|
| Triple with prop X, IRI value | [rda_data_001.ttl](4rdardf/rda_data_001.ttl) | [rda2bf_rml_001.ttl](4rdardf/rda2bf_rml_001.ttl) | [bf_data_002.ttl](4rdardf/bf_data_002.ttl) | |
| Triple with prop X, literal value | [rda_data_002.ttl](4rdardf/rda_data_002.ttl) | [rda2bf_rml_002.ttl](4rdardf/rda2bf_rml_002.ttl) | [bf_data_002.ttl](4rdardf/bf_data_002.ttl) | |
| Triple with prop X, IRI value *and* prop X, literal value | [rda_data_003.ttl](4rdardf/rda_data_003.ttl)| [rda2bf_rml_003.ttl](4rdardf/rda2bf_rml_003.ttl) | [bf_data_003.ttl](4rdardf/bf_data_003.ttl) | |
| Doing things with a full rdac:Manifestation record | [lost_airline_colors.ttl](4rdardf/lost_airline_colors.ttl) | [rda2bf_rml_004.ttl](4rdardf/rda2bf_rml_004.ttl) | [bf_data_004.ttl](4rdardf/bf_data_004.ttl) | Did a bit more with [the `rml:iterator` value](https://github.com/briesenberg07/libraryNotes/blob/977fa33d379eebf7f316c348f6a6640c4e6ec573/rml/rda2bf_rml_004.ttl#L23) to avoid specifying only one resource to convert |
| One (1) TriplesMap with two (2) predicateObjectMap statements | [lost_airline_colors.ttl](4rdardf/lost_airline_colors.ttl) | [rda2bf_rml_005.ttl](4rdardf/rda2bf_rml_005.ttl) | [bf_data_005.ttl](4rdardf/bf_data_005.ttl) | `ex:PublicationMap` has [two `rr:predicateObjectMap` statements](https://github.com/briesenberg07/libraryNotes/blob/977fa33d379eebf7f316c348f6a6640c4e6ec573/rml/rda2bf_rml_005.ttl#L56-L70) |
| How much can I do with *just one* logical source?  | [lost_airline_colors.ttl](4rdardf/lost_airline_colors.ttl) | [rda2bf_rml_006.ttl](4rdardf/rda2bf_rml_006.ttl) | [bf_data_006.ttl](4rdardf/bf_data_006.ttl) |  |

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
[2] JPL's map ran after a few [fixes to the Turtle](https://github.com/briesenberg07/libraryNotes/commit/9d6ffae290cc9d40ab521f99e64313c545a33d50#diff-6250cb7da2933ad75bd6a9dd19a493fc4076ac1edaa54354c31585e2308b835a). The output doesn't look quite right so still some looking needed.

### tangential thoughts about mapping `rdaa:`, `rdap:`, other RDA/RDF properties to BF
For RDA Agent, Place props, and other RDA-entity props, I had assumed that I'd be finding equivalent properties in the BF ontology. But I really hadn't thought this through.   
There *are* no BF props with domain `bf:Agent`, or with domain `bf:Place`...
