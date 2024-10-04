import json

# Sample JSON data
data = '''
{
  "store": {
    "book": [
      { "category": "fiction", "title": "The Great Gatsby", "price": 10.99 },
      { "category": "fiction", "title": "To Kill a Mockingbird", "price": 7.99 },
      { "category": "non-fiction", "title": "Sapiens", "price": 20.99 },
      { "category": "fiction", "title": "1984", "price": 8.99 }
    ],
    "bicycle": { "color": "red", "price": 19.95 }
  }
}
'''

# Load JSON into Python dictionary
parsed_data = json.loads(data)

# Complex Parsing: Extract specific information
def parse_store_data(parsed_data):
    books = parsed_data['store']['book']
    bicycle_info = parsed_data['store']['bicycle']
    
    # Extracting fiction books
    fiction_books = [book['title'] for book in books if book['category'] == 'fiction']
    
    # Extracting all book titles with price > 10
    expensive_books = [book['title'] for book in books if book['price'] > 10]
    
    # Extracting bicycle details
    bicycle_price = bicycle_info['price']
    bicycle_color = bicycle_info['color']
    
    return {
        "fiction_books": fiction_books,
        "expensive_books": expensive_books,
        "bicycle_details": {
            "price": bicycle_price,
            "color": bicycle_color
        }
    }

# Call the function to parse and extract data
extracted_info = parse_store_data(parsed_data)

# Display the extracted information
print(json.dumps(extracted_info, indent=2))
