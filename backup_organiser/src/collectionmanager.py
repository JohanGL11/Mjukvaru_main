from datacollection import DataCollection

""" Manager är inte en lista, den har collections(i en lista) """
class CollectionManager: #Hanterar alla DataCollection-objekt
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """ skapar en DataCollection object och lägger till det i listan """
        print("data", name, description, creation_date, last_modified_date, still_updated)
        new_collection = DataCollection(
            name,
            description,
            creation_date,
            last_modified_date,
            still_updated
        )
        self.collections.append(new_collection)
        print(new_collection)
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
            out.append(collection.full_str()) #fel för adam
        print(out)
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
    # def edit(self, collection_name, modification_date=None, updated=None):
    #     """ Modify the first data collection that maches collection_name.

    #     Return the modified data collection.

    #     """
    #     dc = self.get(collection_name)
    #     if dc and None != modification_date: dc.modification_date = modification_date
    #     if dc and None != updated: dc.still_updated = updated
    #     return dc

    # def delete(self, collection_name):
    #     """ Delete the first data collection that matches collection_name.

    #     Return True if a collection was found and deleted, otherwise False. """

    #     old_len = len(self.collections)
    #     self.collections = [x for x in self.collections if x.name != collection_name]
    #     new_len = len(self.collections)

    #     return new_len == old_len-1
