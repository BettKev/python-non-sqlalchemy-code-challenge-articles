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
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")


    def articles(self):
        pass

    def magazines(self):
        pass

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
