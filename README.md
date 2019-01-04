Testing plural to singular mapping for art thesaurus terms that need OpenRefine reconciliation.

In the GLAM domain, popular art vocabularies typically use plural (and/or capitalized) terms, such as "Mice" vs "mouse" or "Tapestries" vs "tapestry."

When these plurals and capped terms are used in OpenRefine and reconciled against Wikidata, the results are pretty unsatisfactory as they tend to erroneously match proper nouns, such as titles of artworks or geographical locations rather than the general term.

As an experiment, I had a museum keyword set in plural form and ran a Python script using CLIPS pattern Python library (https://www.clips.uantwerpen.be/pattern) to change those plurals to singular and lowercase. The results of reconciliation were much improved. Ideally, there would be a module or setting in OpenRefine to automatically make this adjustment for better matching. 

This might also have some uses for Wikidata Mix'n'match, where we see a similar problem when we import a data set that is plural and capitalized, and get suboptimal recommended matches.
