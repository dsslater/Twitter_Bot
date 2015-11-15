import feedparser

USED_STORIES_FILE = ''

def is_cap_headline(headline):
    """
    Returns True if more than 80 percent of the words in the headline are capitalized.
    NLTK assumes that when things are capitalized that they are proper nouns. This 
    function weeds out headlines that capitalize every word.
    """
    headline = headline.replace("'","")
    headline = headline.replace('"','')
    words = headline.split()
    not_up = 0
    for word in words:
        if word[0] != word.upper()[0]:
            not_up += 1
    if not_up / len(words) < 0.2:
        return True
    return False

def googlink_to_link(googlink):
    """
    Processes google links and returns the actual link
    """
    return(googlink[googlink.find('url=http') + 4:])

def googtitle_to_title(googtitle):
    """
    Processes Google titles and removes the name of the publication
    """
    title = googtitle[:(-1 * (''.join(reversed(googtitle)).find(' - ') + 3))]
    return title

def add_to_used(title):
    """
    adds the name of the headline to the list of used headlines.
    """
    with open(USED_STORIES_FILE, 'a') as f:
        f.write(title + '\n')

def get_top_stories(query):
    """
    Returns a tuple with the title of the top sports story from Google News and the url of the story.
    """
    l = list()
    feed = feedparser.parse('https://news.google.com/news/section?q='+ query + '&output=rss')
    for i in range(len(feed['entries'])):
        title = googtitle_to_title(feed['entries'][i:i+1][0]['title'])
        link = googlink_to_link(feed['entries'][i:i+1][0]['link'])
        tup = (title, link)
        l.append(tup)
    return l

def select_story(stories):
    """
    Gets a list of stories given the query and returns one that has not already been used. 
    It then adds that headline to the file of used headlines.
    """
    with open(USED_STORIES_FILE, 'r') as f:
    	used = [line[:-1] for line in f.readlines()]
    for story in stories:
        if story[0] not in used and not is_cap_headline(story[0]):
            add_to_used(story[0])
            return story
    return None

def get_story(query):
    return select_story(get_top_stories(query))
