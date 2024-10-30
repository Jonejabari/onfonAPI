from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Sample data with current date
contacts = [
    {
        "name": "Jone Jabari",
        "contact_number": "266 5353 6457",
        "date": datetime.now(pytz.UTC).isoformat()
    },
    {
        "name": "Jabari Jabari",
        "contact_number": "266 5353 0099",
        "date": datetime.now(pytz.UTC).isoformat()
    },
    {
        "name": "Tsephe Lethata",
        "contact_number": "266784748",
        "date": datetime.now(pytz.UTC).isoformat()
    }
     
]

def get_cuurent_time():
    """Helper function to get current UTC time in ISO format"""
    return datetime.now(pytz.UTC).isoformat()


# GET all contacts endpoint
@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Get all contacts"""
    return jsonify(contacts)


# GET contact by name endpoint
@app.route('/contacts/<name>', methods=['GET'])
def get_contact(name):
    """Get a specif contact by name"""
    contact = next(
        (contact for contact in contacts if contact ["name"].lower() == name.lower()),
        None
    )
    if contact:
        return jsonify(contact)
    return jsonify({"message": "contact not found"}), 404

# Add new user
@app.route('/contacts', methods=['POST'])
def add_contact():
    """Add new contact"""
    data = request.get_json()

    if not data or 'name' not in data or 'contact_number' not in data:
        return jsonify({"message": "Name and contact number are required"}), 400
    
    new_contact = {
        "name": data["name"],
        "contact_number": data["contact_number"],
        "date": get_cuurent_time()
    }

    contacts.append(new_contact)
    return jsonify(new_contact), 201

# Update existing contact
@app.route('/contacts/<name>', methods=['PUT'])
def update_contact(name):
    """Update an existing contact"""
    data = request.get_json()

    if not data or 'contact_number' not in data:
        return jsonify({"message": "Contact number is required"}), 400
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["contact_number"] = data["contact_number"]
            contact["date"] = get_cuurent_time()
            return jsonify(contact)
        
    return jsonify({"message": "contact not found"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

