import nltk
from nltk import CFG, PCFG


cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
    V -> 'saw' | 'ate' | 'walked'
    P -> 'in' | 'on' | 'by' | 'with'
""")


cfg_parser = nltk.ChartParser(cfg_grammar)


pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'man' [0.2] | 'dog' [0.4] | 'cat' [0.2] | 'telescope' [0.1] | 'park' [0.1]
    V -> 'saw' [0.3] | 'ate' [0.4] | 'walked' [0.3]
    P -> 'in' [0.4] | 'on' [0.3] | 'by' [0.2] | 'with' [0.1]
""")


pcfg_parser = nltk.ViterbiParser(pcfg_grammar)


sentence = "the dog saw a man in the park".split()


print("Constituency Parsing:")
for tree in cfg_parser.parse(sentence):
    print(tree)
    tree.pretty_print()


print("\nProbabilistic Parsing:")
for tree in pcfg_parser.parse(sentence):
    print(tree)
    tree.pretty_print()