from flask import url_for
import re
import json
import pdb
class Project:
    def __init__(self, title, subtitle, content, path):
        self.title = title
        self.subtitle = subtitle
        self.content = content
        r = re.compile(r'^http*')
        # IF local path
        if (r.match(path)):
            self.path = path
        else:
            self.path = url_for('static', filename=path)

    def json(self):
        return json.dumps(self.__dict__)


