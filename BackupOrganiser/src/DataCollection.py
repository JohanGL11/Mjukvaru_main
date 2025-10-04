class DataCollection:  
    def __init__(self, name, description, creation_date, last_modified_date, still_updated):
        """ __init__ så vet python att den skall köra direkt.
        sickar data till backup för hantering """
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
        self.still_updated = still_updated
        self.backup_entries = []

    """ brief_str och full_str funkar på samma sätt men proceserar olika mängd data """
    def brief_str(self):
        """ returnerar en lista med strängar för kort översikt
        kollar om still_updated är True eller False """
        if self.still_updated:
            status = "True"
        else:
            status = "False"
        return[f"{self.name} _ {status}"]

    def full_str(self):
        """ returnerar en lista med strängar för detaljerad info """
        if self.still_updated:
            status = "True"
        else:
            status = "False"
        num_backups = len(self.backup_entries)

        """ Lista som returneras med information """ 
        info_list = [
            f"Name: {self.name}",
            f"Description: {self.description}",
            f"Created: {self.creation_date}",
            f"Last Modified: {self.last_modified_date}",
            f"Status: {status}",
            f"Number of backup: {num_backups}"
        ]
        
        """ Lägger till (backups) i info:list om det finns saker i backup_entries """
        if self.backup_entries: # körs inte om listan är tom
            info_list.append("backups")
            for backup in self.backup_entries:
                info_list.append(f"  - {backup}")
        return info_list
