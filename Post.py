class Post:

    def __init__(self, title, subtitle, content, date):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.content = content

    def getTitle(self):
        return self.title
