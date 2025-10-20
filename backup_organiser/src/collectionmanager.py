from datacollection import DataCollection

""" Manager är inte en lista, den har collections(i en lista) """
class CollectionManager: 
    """ Hanterar alla DataCollection-objekt """
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

    def overview(self):
        """Returnerar översikt som JSON-objekt"""
        out = []
        for collection in self.collections:
            out.append(
                {
                    "name": collection.name,
                    "backups": collection.backup_entries,  # Använd backup_entries
                }
            )
        return out

    def detailed_overview(self):
        """ samma sak som overview fast returnerar en array """
        out = []
        for  collection in self.collections:
            out.append(collection.to_dict())
        print(out)
        return out

    def info(self, collection_name):
        """ Info om EN lista """
        """ Returnerar en Lista med strängar för en specifik DataCollection """
        for  collection in self.collections:
            if collection.name == collection_name:
                """ kollar om namnet på nuvarande collection matchar namnet du söker efter """
                return collection.to_dict() #körs när if är True 
        return [f"collection {collection_name} not found"]

    def get(self, collection_name):
        """ Hämtar EN collection objekt. """
        """ Returnerar ett DataCollection objekt """
        for  collection in self.collections:
            if collection.name == collection_name:
                return collection
        return None

    def delete(self, collection_name):
        """ Delete the first data collection that matches collection_name.

        Return True if a collection was found and deleted, otherwise False. """

        old_len = len(self.collections)
        self.collections = [x for x in self.collections if x.name != collection_name]
        new_len = len(self.collections)

        return new_len == old_len-1

    def edit(self, collection_name, last_modified_date=None, still_updated=None):
        """Redigera en collection"""
        for collection in self.collections:
            if collection.name == collection_name:
                """ Uppdatera last_modified_date om den finns """
                if last_modified_date is not None:
                    collection.last_modified_date = last_modified_date
                """ Uppdatera still_updated om den finns """
                if still_updated is not None:
                    """ Konvertera string "true"/"false" till boolean """
                    if isinstance(still_updated, str):
                        collection.still_updated = still_updated.lower() == "true"
                    else:
                        collection.still_updated = bool(still_updated)
                return True
        return False

    def search(self, search_term):
        """Search collections and return as JSON"""
        result = []
        search_lower = search_term.lower()
        for collection in self.collections:
            if search_lower in collection.name.lower():
                result.append({
                    "name": collection.name, 
                    "backups": collection.backup_entries})
        return result
