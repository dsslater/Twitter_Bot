import feedparser

USED_STORIES_FILE = ''

def googlink_to_link(googlink):
    return(googlink[googlink.find('url=http') + 4:])

def googtitle_to_title(googtitle):
    title = googtitle[:(-1 * (''.join(reversed(googtitle)).find(' - ') + 3))]
    return title

def add_to_used(title):
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
    with open(USED_STORIES_FILE, 'r') as f:
    	used = [line[:-1] for line in f.readlines()]
    for story in stories:
        if story[0] not in used:
            add_to_used(story[0])
            return story
    return None

def get_story(query):
    return select_story(get_top_stories(query))
