## Contact API Monorepo ##

A monorepo containing two implementations of a contact API build with Node.js and Python. Both APIs provide endpoints to manage contact information including name, contact number and timestamps

## Project Structure ##

contact-api-monorepo/
|-- node-api/
|     |--- server.js
|     |--- package.js
|--- python-api/
|      |--- server.py
|
|__ README.md

## Fearures ##

Both APIs provide identical functionality:
- Retrieve all contacts
- Get a specific contacts by name
- Add new contacts
- Update existing contacts
- Automatic timestamp tracking for all records

## Installation & Setup

# Node.js API #
Navigate to Node.js project
cd nodeApi
# install dependencies
npm install
# Start the server
npm run dev

# Python API #
Navigate to Python project
cd pythonApi
# install dependencies
pip install 
# Start the server
python server.py

Both servers will run on http://localhost:5001

## API Endpoints ##
