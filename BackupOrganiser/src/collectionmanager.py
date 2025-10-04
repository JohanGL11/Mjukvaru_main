from datacollection import DataCollection

""" Manager är inte en lista, den har collections(i en lista) """
class CollectionManager: #Hanterar alla DataCollection-objekt
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """ skapar en DataCollection object och lägger till det i listan """
        new_collection = DataCollection(
            name,
            description,
            creation_date,
            last_modified_date,
            still_updated
        )
        self.collections.append(new_collection)
        """ new_collection=DataCollection()
        new_collection.name = name
        new_collection.description = description
        new_collection.creation_date = creation_date
        new_collection.last_modified_date = last_modified_date
        new_collection.still_updated = still_updated
        self.collections.append(new_collection) """

    def overview(self): #Tar ut en i taget. lägger till i slutet av listan.
        """ Returnerar en lista med strängar, varje DataCollection för en sträng """
        out = []
        for collection in self.collections:
            out.append(collection.brief_str()[0])
        return out

    def detailed_overview(self):
        """ samma sak som overview fast returnerar en array """
        out = []
        for  collection in self.collections:
            out.append(collection.brief_str())
        return out

    def info(self, collection_name): #info om EN lista
        """ Returnerar en Lista med strängar för en specifik DataCollection """
        for  collection in self.collections:
            if collection.name == collection_name:
                """ kollar om namnet på nuvarande collection matchar namnet du söker efter """
                return collection.full_str() #körs när if är True 
        return [f"collection {collection_name} not found"]

    def get(self, collection_name): # hämtar EN collection objekt.
        """ Returnerar ett DataCollection objekt """
        for  collection in self.collections:
            if collection.name == collection_name:
                return collection
        return None
