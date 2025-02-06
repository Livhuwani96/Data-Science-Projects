# garden.py

import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boats.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Process each sentence using spaCy
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    
    # Tokenization
    print("Tokens:", [token.text for token in doc])
    
    # Named Entity Recognition
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}, Explanation: {spacy.explain(ent.label_)}")
    print("\n")

# Comment about two entities looked up
# 1. ENTITY: "Band-Aid", LABEL: "PRODUCT"
#    EXPLANATION: Products including manufactured items, technology, etc.
#    This makes sense as "Band-Aid" is a manufactured product.
# 2. ENTITY: "Mississippi", LABEL: "GPE"
#    EXPLANATION: Countries, cities, states.
#    This makes sense as "Mississippi" is a state in the United States.
