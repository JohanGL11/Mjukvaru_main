class DataCollection:
    def __init__(self, name, description, creation_date, last_modified_date, still_updated):
        """__init__ vet python att den ska köra automatiskt"""
        """Skickar vidare data till backup hantering"""
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
        self.still_updated = still_updated
        self.backup_entries = []

    def brief_str(self):
        """Returnerar en lista med strängar för kort översikt"""
        """Kollar om still.updated är True eller False"""
        if self.still_updated:
            status = True
        else:
            status = False
        return [f"{self.name} - {status}"]

    def full_str(self):
        if self.still_updated:
            status = True
        else:
            status = False
        number_of_backups = len(self.backup_entries)
        """Listan som returneras med information"""
        info_list = [
            f"Name: {self.name}"
            f" Description: {self.description}"
            f" Created: {self.creation_date}"
            f" Last Modified: {self.last_modified_date}"
            f" Status: {status}"
            f" Number of backups {number_of_backups}"
        ]
        if self.backup_entries:
            info_list.append("Backups: ")
            for backup in self.backup_entries:
                info_list.append(
                    f"  - {backup['name']} ({backup['date']}) at {backup['location']}"
                )
        return info_list

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "last_modified_date": self.last_modified_date,
            "still_updated": self.still_updated,
            "backups": self.backup_entries  # Already a list of dicts
        }
