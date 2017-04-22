class JsonLoader(object):
    def load(self, path):
        with open(path, 'r', encoding='utf-8') as jsonfile:
            return json.loads(jsonfile.read())


import uuid


class I:
    integer = -1


def guid():
    return str(uuid.uuid4())
    #I.integer += 1
    #return I.integer
