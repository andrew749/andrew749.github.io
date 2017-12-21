from flask import url_for
class Post:

    def __init__(self, title, subtitle, content, date):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.content = content

    def getTitle(self):
        return self.title

    def __json__(self):
        return dict(
            title=self.title,
            subtitle=self.subtitle,
            date=self.date,
            content=self.content,
            url=url_for('blog_post', blog_slug=self.title)
        )

    def serialize(self):
        return self.__json__()

    def to_json(self):
        return self.__json__()

