from nltk.corpus import wordnet as wn
import dbm

def main():
    fh = open('wn-domains-3.2-20070223', 'r')
    dbdomains = dbm.open('dbdomains', 'c')
    for line in fh:
        offset, domain = line.split('\t')
        dbdomains[offset[:-2]] = domain
    fh.close()
    # l = 0
    for synset in wn.all_synsets():
        ss = str(synset.offset())
        length = len(ss)
        if length == 7:
            zeroes = '0'
        elif length == 6:
            zeroes = '00'
        elif length == 5:
            zeroes = '000'
        elif length == 4:
            zeroes = '0000'
        if 'sport' in str(dbdomains.get(zeroes + ss)):
            print(synset.name())
        # l += 1
    # print(len(dbdomains), l)

if __name__ == '__main__':
    main()
