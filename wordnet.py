from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis
from collections import defaultdict
import re

def print_nouns():
    nouns = []
    for synset in list(wn.all_synsets('n')):
        match = re.search(r'\w+.n', synset.name())
        if match:
            nouns.append(match.group())
    nouns = sorted(set(nouns))
    for noun in nouns:
        print(noun[:-2])

def print_sense(word):
    print(wn.synsets(word))

def print_synonyms(word):
    synonyms = [] 
    for syn in wn.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    synonyms = sorted(set(synonyms))
    if synonyms:
        print(synonyms)
        print("len: " + str(len(synonyms)))
    else:
        print("Synonyms are not present")
        print("len: 0")

def print_antonyms(word):
    antonyms = [] 
    for syn in wn.synsets(word): 
        for l in syn.lemmas(): 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
    antonyms = sorted(set(antonyms))
    if antonyms:
        print(antonyms)
        print("len: " + str(len(antonyms)))
    else:
        print("Antonyms are not present")
        print("len: 0")

def print_number_of_senses(word):
    print("number: " + str(len(wn.synsets(word))))

def print_semantic_similarity(word1, word2):
    print('Printing path similarity')
    print(str(wn.synsets(word1)[0].path_similarity(wn.synsets(word2)[0])))
    print('Printing Leacock-Chodorow similarity')
    print(str(wn.synsets(word1)[0].lch_similarity(wn.synsets(word2)[0])))
    print('Printing Wu-Palmer similarity')
    print(str(wn.synsets(word1)[0].wup_similarity(wn.synsets(word2)[0])))
    '''
    Requires information content
    '''
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    semcor_ic = wordnet_ic.ic('ic-semcor.dat')
    genesis_ic = wn.ic(genesis, False, 0.0)
    print('Printing Resnik similarity')
    print('Brown information content: ' + str(wn.synsets(word1)[0].res_similarity(wn.synsets(word2)[0], brown_ic)))
    print('Genesis information content: ' + str(wn.synsets(word1)[0].res_similarity(wn.synsets(word2)[0], genesis_ic)))
    print('Printing Jiang-Conrath similarity')
    print('Brown information content: ' + str(wn.synsets(word1)[0].jcn_similarity(wn.synsets(word2)[0], brown_ic)))
    print('Genesis information content: ' + str(wn.synsets(word1)[0].jcn_similarity(wn.synsets(word2)[0], genesis_ic)))
    print('Printing Lin similarity')
    print('Semcor information content: ' + str(wn.synsets(word1)[0].lin_similarity(wn.synsets(word2)[0], semcor_ic)))

def print_hypernyms(word):
    # hypernyms = [synset.hypernyms() for synset in wn.synsets(word)]
    # hypernyms = [item for sublist in hypernyms for item in sublist]
    # hypernyms = sorted(set(hypernyms))
    '''
    flat_list = [item for sublist in l for item in sublist]
    The above line of code translates to-
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    '''
    hypernyms = sorted(set(wn.synsets(word)[0].hypernyms()))
    if hypernyms:
        for hypernym in hypernyms:
            match = re.search(r'\w+.n', hypernym.name())
            if match:
                print(match.group()[:-2])
    else:
        print('Hypernyms not present')

def print_co_hyponyms(word):
    hypernyms = wn.synsets(word)[0].hypernyms()
    co_hyponyms = []
    for hypernym in hypernyms:
        for ch in hypernym.hyponyms():
            match = re.search(r'\w+.n', ch.name())
            if match:
                co_hyponyms.append(match.group()[:-2])
    co_hyponyms = sorted(set(co_hyponyms))
    co_hyponyms.remove(word)
    if co_hyponyms:
        for ch in co_hyponyms:
            print(ch)
    else:
        print('Co-hyponyms not present')

def print_hyponyms(word):
    # hyponyms = [synset.hyponyms() for synset in wn.synsets(word)]
    # hyponyms = [item for sublist in hyponyms for item in sublist]
    # hyponyms = sorted(set(hyponyms))
    hyponyms = sorted(set(wn.synsets(word)[0].hyponyms()))
    if hyponyms:
        for hyponym in hyponyms:
            match = re.search(r'\w+.n', hyponym.name())
            if match:
                print(match.group()[:-2])
    else:
        print('Hyponyms not present')

def print_words_from_domain(domain):
    domain_to_synsets = defaultdict(list)
    for line in open('wn-domains-3.2-20070223', 'r'):
        ssid, doms = line.strip().split('\t')
        doms = doms.split()
        for d in doms:
            domain_to_synsets[d].append(ssid)
    synsets = wn.all_synsets()
    synset_offsets = {}
    for synset in synsets:
        ss = str(synset.offset())
        length = len(ss)
        if length == 7:
            ss = '0' + ss
        elif length == 6:
            ss = '00' + ss
        elif length == 5:
            ss = '000' + ss
        elif length == 4:
            ss = '0000' + ss
        match = re.search(r'\w+.n', synset.name())
        if match:
            synset_offsets[ss] = match.group()[:-2]
    keys = list(synset_offsets.keys())
    for word in domain_to_synsets[domain]:
        '''
        TODO
        figure out why the offsets extracted from the above opened file do not
        directly correspond to a synset
        '''
        # synset = wn.synset_from_pos_and_offset(word[-1], int(word[:-2]))
        # synset = wn.of2ss(word[:-2] + word[-1])
        # match = re.search(r'\w+.n', synset.name())
        # if match:
            # print(match.group()[:-2])
        '''
        just displaying the synset offset-id of words related to domain for now
        '''
        print(word, end='\t')
        # if word[:-2] in keys:
            # print(synset_offsets[word[:-2]])

def main():
    # print('Printing all nouns...')
    # print_nouns()
    # word = input('Input a word: ')
    # print('Printing all senses...')
    # print_sense(word)
    # word = input('Input a word: ')
    # print('Printing all synonyms...')
    # print_synonyms(word)
    # word = input('Input a word: ')
    # print('Printing all antonyms...')
    # print_antonyms(word)
    # word = input('Input a word: ')
    # print('Printing number of senses...')
    # print_number_of_senses(word)
    # word1 = input('Input first word: ')
    # word2 = input('Input second word: ')
    # print('Printing semantic similarities...')
    # print_semantic_similarity(word1, word2)
    # word = input('Input a word: ')
    # print('Printing hypernyms...')
    # print_hypernyms(word)
    # word = input('Input a word: ')
    # print('Printing co-hyponyms...')
    # print_co_hyponyms(word)
    # word = input('Input a word: ')
    # print('Printing hyponyms...')
    # print_hyponyms(word)
    print('Printing words having sport domain...')
    print_words_from_domain('sport')

if __name__ == '__main__':
    main()
