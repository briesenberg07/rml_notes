# 4rdardf - test mappings and test data
| description/comments | test map | test output |
|---|---|---|
| Triple with prop X, IRI value | [rda2bf_rml_001.ttl](rda2bf_rml_001.ttl) | [bf_data_002.ttl](bf_data_002.ttl) |
| Triple with prop X, literal value | [rda2bf_rml_002.ttl](rda2bf_rml_002.ttl) | [bf_data_002.ttl](bf_data_002.ttl) |
| Triple with prop X, IRI value *and* prop X, literal value | [rda_data_003.ttl](rda_data_003.ttl)| [bf_data_003.ttl](bf_data_003.ttl) |
| Doing things with a full rdac:Manifestation record; did a bit more with [the `rml:iterator` value](https://github.com/briesenberg07/libraryNotes/blob/977fa33d379eebf7f316c348f6a6640c4e6ec573/rml/rda2bf_rml_004.ttl#L23) to avoid specifying only one resource to convert | [rda2bf_rml_004.ttl](rda2bf_rml_004.ttl) | [bf_data_004.ttl](bf_data_004.ttl) |
| One (1) TriplesMap with two (2) predicateObjectMap statements; `ex:PublicationMap` has [two `rr:predicateObjectMap` statements](https://github.com/briesenberg07/libraryNotes/blob/977fa33d379eebf7f316c348f6a6640c4e6ec573/rml/rda2bf_rml_005.ttl#L56-L70) | [rda2bf_rml_005.ttl](rda2bf_rml_005.ttl) | [bf_data_005.ttl](bf_data_005.ttl) |
| How much can I do with *just one* logical source? [see [1](#notes)]  | [rda2bf_rml_006.ttl](rda2bf_rml_006.ttl) | [bf_data_006.ttl](bf_data_006.ttl) |
| [LEVEL 5 [!!]](https://github.com/uwlib-cams/rml/tree/master/getting_started/practice_data) practice data from MCM | [rda2bf_rml_007.ttl](rda2bf_rml_007.ttl) | 😠 see [#2](https://github.com/briesenberg07/rml_notes/issues/2) |
| try another LEVEL 5er | [rda2bf_rml_008.ttl](rda2bf_rml_008.ttl) | 😠 see [#2](https://github.com/briesenberg07/rml_notes/issues/2) |

## notes
[1] It's kind of a trick question. What I think of as the "main" map (the map for an RDA Manifestation, which in a full mapping would--I think--have many many predicateObjectMap statements) has, of course, only one logical source. But every new, distinct TriplesMap--that is, every distinct TriplesMap which will be referenced in a predicateObjectMap in the "main" map and defined outside of that "main" map, must of course also have a logical source.
## tangential thoughts about mapping `rdaa:`, `rdap:`, other RDA/RDF properties to BF
For RDA Agent, Place props, and other RDA-entity props, I had assumed that I'd be finding equivalent properties in the BF ontology. But I really hadn't thought this through.   
There *are* no BF props with domain `bf:Agent`, or with domain `bf:Place`...
