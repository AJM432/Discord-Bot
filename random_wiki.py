import wikipedia as wiki

def random_wiki_topic():
    article_topic = wiki.random(1)
    return article_topic


def get_wiki_image(topic):
    wikipage = wiki.page(topic)
    return wikipage.images[0]


def random_wiki_url(topic):
    return 'https://en.wikipedia.org/wiki/' + '_'.join(topic.split())


if __name__ == "__main__":
    topic = random_wiki_topic()
    print(get_wiki_image(topic))
    print(random_wiki_url(topic))
