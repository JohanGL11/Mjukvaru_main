import DataCollection

class CollectionManager:
    def add_collection(self, name, description, creation_date, modification_date, updated):
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.updated = updated
    def overview():
        pass

    def detailed_overview():
        DataCollection.brief_str()
        pass

    def info(collection_name):
        DataCollection.full_str()
        pass

    def get(collection_name):
        pass
