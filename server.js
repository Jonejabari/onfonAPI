const express = require('express');
const app = express();
const port = 5001;

// sample data (name, contact number) with current date
const contacts = [
    {name: "Jone Jabari", contactNumber: "26653536457", date: new Date().toString() },
    {name: "Jane Jone", contactNumber: "2666323676", date: new Date().toString()},
    {name: "Tsephe Lethata", contactNumber: "266784748", date: new Date().toString()}
];

// middlware to parse JSON bodies/format
app.use(express.json());

// GET route to fetch all contacts
app.get('/contacts', (req, res) => {
    res.json(contacts);
});

// GET route to fetch a specif contact by name
app.get('/contacts/:name', (req, res) => {
    const contact = contacts.find(c => c.name.toLowerCase() === req.params.name.toLowerCase());
    if(contact){
        res.json(contact);
    }else{
        res.status(404).json({ message: "contact not fount" });
    }
});

// POST route to add a new contact
app.post('/contacts', (req, res) => {
    const { name, contactNumber } = req.body;
    if (!name || !contactNumber){
        return res.status(400).json({ message: "Name and Contact number are required"});
    }
    return newContact = {
        name,
        contactNumber,
        date: new Date().toISOString()
    };
    contacts.push(newContact);
    res.status(201).json(newContact);
});

// PUT route to update a contact
app.put('/contacts/:name', (req, res) => {
    const { contactNumber } = req.body;
    const contactIndex = contacts.findIndex(c => c.name.toLowerCase() === req.params.name.toLowerCase());
    if (contactIndex > -1){
        contacts[contactIndex] = {
            ...contacts[contactIndex],
            contactNumber,
            date: new Date().toISOString()
        };
        res.json(contacts[contactIndex]);
    }else{
        res.status(404).json({ message: "Contact not found" });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`API running at http:localhost:${port}`);
});