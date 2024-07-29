from loader.data_loader import DataLoader
from database.setup import setup_database

def main():
    setup_database()
    data_loader = DataLoader()
    data_loader.load_data()

if __name__ == "__main__":
    main()
