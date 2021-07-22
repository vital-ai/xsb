import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp('')

def make_doc(text):
    global doc
    doc = nlp(text)
    return(doc)

def get_nps():
    global doc
    return([chunk.text for chunk in doc.noun_chunks])

def get_token_info():
    global doc
    return([(token.text,token.lemma_,token.pos_,token.tag_,token.dep_) for token in doc])
           
def get_chunks():
    global doc
    return([chunk.text for chunk in doc.noun_chunks])
