from flask import url_for
import re
import json
import pdb
class Project:
    def __init__(self, title, subtitle, content, thumbnailPath, projectSlug):
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.projectSlug = projectSlug
        r = re.compile(r'^http*')
        # IF local path
        if (r.match(thumbnailPath)):
            self.thumbnailPath = thumbnailPath
        else:
            self.thumbnailPath = url_for('static', filename=thumbnailPath)
        self.url = "project/{}".format(projectSlug)

    def dict(self):
        return self.__dict__

    def json(self):
        return json.dumps(self.__dict__)


