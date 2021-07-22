


-------------------------------------------------
For mathplotlib demo:

1) Make a matpyplot of some sort:
callpy('apps/mpl',make_pyplot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                            [4948,1045,1010,364,321,195,139,97,89,59,56,59,26,25,22],
			    'number_of_components','component_size'),X).

2) Now show the pyplot:
callpy('apps/mpl',show_pyplot(),F).

3) Alternately make a pyplot in PDF form in File
callpy('apps/mpl',pdf_save_pyplot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
				   [4948,1045,1010,364,321,195,139,97,89,59,56,59,26,25,22],
			    	   'number_of_components','component_size',File),Ret).

-------------------------------------------------
For spacy_demo:

1) Make a spacy document for a given piece of text:

callpy(spacy_demo,make_doc('As the Royal Navy takes part in the wars against Napoleonic France, young Jack Aubrey receives his first command, the small, old, and slow HMS Sophie. Accompanied by his eccentric new friend, the physician and naturalist Stephen Maturin, Aubrey does battle with the naval hierarchy, with his own tendency to make social blunders, and with the challenges of forging an effective crew -- before ultimately taking on enemy ships in a vivid, intricately detailed series of sea battles.'),F).

2) Return some token info to Prolog
callpy(spacy_demo,get_token_info(),Toks).

3) Find what tokens in the document are textually different from their lemma form
callpy(spacy_demo,get_token_info(),Toks),member(''(Text,Lemma,POS,Tag,Dep),Toks),Text \= Lemma.

4) Check out the noun phrases

5) Check out the noun phrases
callpy(spacy_demo,get_chunks(),F).

-------------------------------------------------

For callback example, consult ping.P and type the goal ping(N), which
will create callbacks of level N (more or less)  between XSB and Python