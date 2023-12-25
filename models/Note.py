class Note:
    def __init__(self, title, text, tags=[]):
        self.__title = None
        self.__tags = None

        self.title = title
        self.text = text
        self.tags = tags
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = str(title).capitalize()
    
    @property
    def tags(self):
        return self.__tags
    
    @tags.setter
    def title(self, tags):
        self.__tags = [tag.lower() for tag in tags]
    
    
    def add_tag(self, tag):
        self.tags.append(tag.lower())
    
    def edit_title(self, title):
        self.title = title
    
    def edit_text(self, text):
        self.text = text

    def __str__(self):
        return f"{self.title}\n{self.text}\n{" #".join(self.tags)}\n"
