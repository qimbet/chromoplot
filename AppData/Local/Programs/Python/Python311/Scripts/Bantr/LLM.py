#LLM for Bantr
#A positional encoder maps an integer to a normalized value, through use of sin/cosine functions.
#These ensure word order is preserved, and behave identically (for equal hyperparameters) over phrases of different length. 

print("Begin LLM.py... ")
import PseudoPost
import spacy
from spacy import displacy

spacy.cli.download("en_core_web_sm")
NER = spacy.load("en_core_web_sm")

def spacy_small_ner(body):
    return{(ent.text.strip(), ent.label_) for ent in NER(body).ents}

textToParse = ""
while textToParse.lower() != "exit":
    tempPost = PseudoPost.generatePost()
    textToParse = input(f"Enter 'exit' to close, or press enter to use the string: \"{tempPost}\"\nYou can also write your own string for analysis.\n")
    if textToParse == "":
        textToParse = tempPost
    
    output = spacy_small_ner(textToParse)
    print(f"Text generated! We have an original string: {textToParse} \nAnd a tokenized(?) array: {output}")