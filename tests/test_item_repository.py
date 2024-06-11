from lib.item_repository import ItemRepository
from lib.Item import Item

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ArtistRepository

    item_catalogue = repository.all() 

    # Assert on the results
    assert item_catalogue == [
        Item("Football",        8.99,   101     ,1),
        Item("Swimming cap",    2.99,   400     ,2),
        Item("Baseball bat",    19.99,  10      ,3),
        Item("Gloves",          10.99,  350,    4)
    ]

"""

Create a new record in the database.
# """
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    newItem = Item("Shinpads", 14.99, 75)

    repository.create(newItem)

    item_respository = repository.all()
    
    assert item_respository == [
        Item("Football",        8.99,   101     ,1),
        Item("Swimming cap",    2.99,   400     ,2),
        Item("Baseball bat",    19.99,  10      ,3),
        Item("Gloves",          10.99,  350,    4),
        Item("Shinpads",        14.99,  75,    5)
    ]



