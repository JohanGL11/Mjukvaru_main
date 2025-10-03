import DataCollection

class CollectionManager:
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, modification_date, updated):
        new_collection=DataCollection()
        new_collection.name = name
        new_collection.description = description
        new_collection.creation_date = creation_date
        new_collection.modification_date = modification_date
        new_collection.updated = updated
        self.collections.append(new_collection)

    def overview(self): # tar ut en i taget. lägger till i slutet av listan.
        out = []
        for i in self.collections:
            out.append(i.brief_str())
        return out

    def detailed_overview(self):
        out = []
        for i in self.collections:
            out.append(i.full_str())
        return out

    def info(collection_name):
        DataCollection.full_str()
        pass

    def get(collection_name):
        pass
