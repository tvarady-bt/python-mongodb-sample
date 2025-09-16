import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client["test_db"]
    
    collection = db["test_collection"]

    data = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        },
        {
            "name": "Bob Johnson",
            "email": "bob.johnson@example.co"
        },
        {
            "name": "Alice Williams",
            "email": "alice.williams@example.com"
        }
    ]

    x = collection.insert_many(data)
    print(f"Inserted {len(x.inserted_ids)} results into database")

    query = {"name": "Bob Johnson"}

    results = collection.find(query)
    if len(results) != 1:
        print(f"Incorrect number of results from query: {len(results)}")
    else:
        print(f"Name: {results[0].name}, Email: {results[0].email}")

if __name__ == "__main__":
    main()