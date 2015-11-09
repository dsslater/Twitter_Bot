import nltk

def get_pns(text):
    pronouns = list()    
    tok_text = nltk.word_tokenize(text)
    pos_text = nltk.pos_tag(tok_text)
    last_was_pn = False
    size = 1
    for word_tup in pos_text:
        if word_tup[1] == 'NNP' or word_tup[1] == 'NNPS':
            if last_was_pn and size < 2:
                last_index = len(pronouns) - 1
                root = pronouns[last_index]
                new_pn = root + ' ' + word_tup[0]
                pronouns[last_index] = new_pn
                size += 1
            else:
                if size >= 2:
                    size = 1                
                pronouns.append(word_tup[0])
                last_was_pn = True
        else:
            last_was_pn = False
    return pronouns

def substitute(head1, replacements):
    headline = head1    
    for sub in replacements:
        found = headline.find(sub[0])
        while(found != -1):
            headline = headline[:found] + sub[1] + headline[found + len(sub[0]):]
            found = headline.find(sub[0])
            return headline
    return headline

def new_headline(head1, head2):
    pn1 = get_pns(head1)
    pn2 = get_pns(head2)
    replacements = zip(pn1, pn2)

    return substitute(head1, replacements)
