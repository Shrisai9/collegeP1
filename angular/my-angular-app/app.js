const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();

// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/personDB', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.log('Database connection error: ', err));

// Define Mongoose Schema for Person
const personSchema = new mongoose.Schema({
  name: String,
  age: Number,
  gender: String,
  mobile: String
});

// Create Person Model
const Person = mongoose.model('Person', personSchema);

// ROUTES

// GET /person: Display a list of people
app.get('/person', async (req, res) => {
  try {
    const people = await Person.find();
    res.status(200).json(people); // Return data in JSON format
  } catch (err) {
    res.status(500).json({ message: 'Error fetching people', error: err });
  }
});

// POST /person: Create a new person
app.post('/person', async (req, res) => {
  try {
    const { name, age, gender, mobile } = req.body;
    const newPerson = new Person({ name, age, gender, mobile });
    await newPerson.save();
    res.status(201).json({ message: 'Person created', person: newPerson });
  } catch (err) {
    res.status(500).json({ message: 'Error creating person', error: err });
  }
});

// PUT /person/:id: Update a specific person
app.put('/person/:id', async (req, res) => {
  try {
    const { name, age, gender, mobile } = req.body;
    const updatedPerson = await Person.findByIdAndUpdate(
      req.params.id,
      { name, age, gender, mobile },
      { new: true }
    );
    if (!updatedPerson) {
      return res.status(404).json({ message: 'Person not found' });
    }
    res.status(200).json({ message: 'Person updated', person: updatedPerson });
  } catch (err) {
    res.status(500).json({ message: 'Error updating person', error: err });
  }
});

// DELETE /person/:id: Delete a specific person
app.delete('/person/:id', async (req, res) => {
  try {
    const deletedPerson = await Person.findByIdAndDelete(req.params.id);
    if (!deletedPerson) {
      return res.status(404).json({ message: 'Person not found' });
    }
    res.status(200).json({ message: 'Person deleted', person: deletedPerson });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting person', error: err });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
