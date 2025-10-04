from CollectionManager import CollectionManager 
from BackupManager import backup_manager

def main():
    
    collection_mgr = CollectionManager
    backup_mgr = backup_manager

    print("=" * 50)
    print("TESTING BACKUPORGANISER")
    print("=" * 50)

    print("\n- TEST 1: -adding collections -")
    collection_mgr.add_collection("Customer Data", "All customer information", "2024-01-15", "2024-12-20", True)
    collection_mgr.add_collection("Old Surveys", "Survey results from 2020", "2020-03-10", "2020-06-15", False)
    collection_mgr.add_collection("Project Files", "Development project files", "2023-05-01", "2024-10-01", True)
    print("Added 3 collections")

    print ("TEST 2: -Overview-")
    for info_list in collection_mgr.detailed_overview():
        print(info_list)

if __name__ == "__name__":
    main()
