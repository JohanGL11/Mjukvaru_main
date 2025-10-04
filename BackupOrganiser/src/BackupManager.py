class backup_manager:
    def __init__(self):
        pass

    def add_backup(self, collection_object, backup_name, backup_date, backup_location):
        self.collection_object = collection_object
        self.backup_name = backup_name
        self.backup_date = backup_date
        self.backup_location = backup_location

        if collection_object is None:
            print("Error: collection object is None")
            return

        backup_entry = f"{backup_name} (date: {backup_date}, Location: {backup_location})"
        collection_object.backup_entries.append(backup_entry)
