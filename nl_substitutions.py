import nltk
import random


def get_ps(text, types):
    """
    Takes in a string and an array of the parts of 
    speech that need to be identified. This method 
    uses NLTK to tokenize and then analyze every 
    word in the string. If a word is of a part of 
    speech thatis in the list of types then it is 
    added to a list of matches that is returned. 
    One special case is when there a mulptiple 
    consecutive matches. This tends to suggest 
    that the words should be kept together 
    (Ex. 'Donald' and 'Trump' should probably be 
    kept together as 'Donald Trump'). To do this we 
    keep a flag updated on whether or no the last word 
    was a match so that if the next word is also a match 
    it can just be appended to the last entry.
    """
    pronouns = list()    
    tok_text = nltk.word_tokenize(text)
    pos_text = nltk.pos_tag(tok_text)
    last_was_ps = False
    size = 1
    for word_tup in pos_text:
        if word_tup[1] in types:
            if last_was_ps and size < 2:
                last_index = len(pronouns) - 1
                root = pronouns[last_index]
                new_pn = root + ' ' + word_tup[0]
                pronouns[last_index] = new_pn
                size += 1
            else:
                if size >= 2:
                    size = 1                
                pronouns.append(word_tup[0])
                last_was_ps = True
        else:
            last_was_ps = False
    return pronouns

def substitute(head1, replacements):
    """
    randomly selects one of the mapped word tuples 
    and replaces all instances of the 0th word with 
    the 1st word in headline and then returns the 
    new string
    """
    headline = str(head1)  
    index = random.randint(0, len(replacements)-1)
    sub = replacements[index]
    found = headline.find(sub[0])
    while(found != -1):
        headline = headline[:found] + sub[1] + headline[found + len(sub[0]):]
        found = headline.find(sub[0])
        return headline
    return headline

def new_headline(head1, head2):
    """
    Identifies the Proper Nouns and the Adjectives for 
    both headlines. Then it randomly decided which 
    headeine will get the substitutions. Next an attempt 
    will be made to substitute Proper Nouns and then 
    Adjectives. If neither of these is possible (because 
    both headlines did not have either PNs or JJs) then
    new_headline returns false. Otherwise it returns the 
    new headline
    """
    print(head1, "  |  ", head2)
    pn1 = get_ps(head1, list(['NNP', 'NNPS']))
    pn2 = get_ps(head2, list(['NNP', 'NNPS']))
    adj1 = get_ps(head1, list(['JJ']))
    adj2 = get_ps(head2, list(['JJ']))
    if random.choice([True, False]):
        pn_reps = list(zip(pn1, pn2))
        adj_reps = list(zip(adj1, adj2))
        head = head1
    else:
        pn_reps = list(zip(pn2, pn1))
        adj_reps = list(zip(adj2, adj1))
        head = head2
    success = False
    if len(pn_reps) :
        head = substitute(head, pn_reps)
        success = True
    if len(adj_reps) :
        head = substitute(head, adj_reps)
    if success:
        return head
    return False
