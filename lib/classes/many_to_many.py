class Article:
    #Class level list to store all Article instances
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title  # Use a private variable
        Article.all.append(self)
    
    #getter
    @property
    def title(self):
        return self._title  # Provide read-only access to the title

class Author:
    def __init__(self, name):
        self._name = name

    #getter
    @property
    def name(self):
        return self._name # Provide read-only access to the name

    def articles(self):
        # Return a list of articles where the author matches self
        return [article for article in Article.all if article.author == self]

    def magazines(self):
         # Collect unique magazines where the author has written articles
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, magazine, title):
        # Create a new article and return it
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
    # Use the magazines method to get all magazines and extract their categories
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        # Return a list of articles where the magazine matches self
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return a list of unique authors who have written articles for this magazine
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        # Return a list of titles of articles published in this magazine
        return [article.title for article in Article.all if article.magazine == self]

    def contributing_authors(self):
        # Return a list of authors who have written more than one article for this magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 1]