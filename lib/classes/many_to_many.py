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
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
