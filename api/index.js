const express = require('express');
const mongoose = require('mongoose');


// setup database

const mongoPassword = 'uUVU6zXm8dxpjLRa';

const mongoString = `mongodb+srv://ndiuel:${mongoPassword}@cluster0.nelkdpf.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp`;



mongoose.connect(mongoString);

const database = mongoose.connection;

database.on('error', (error) => {
    console.log(error)
});

database.once('connected', () => {
    console.log('Database Connected');
});

const dataSchema = new mongoose.Schema({
    name: {
        type: String
    },
    email: {
        type: String
    }
});


const Person = mongoose.model('Person', dataSchema);


const transform = data => (
    { name: data.name, email: data.email, id: data._id }
)

const app = express();

app.use(express.json());

app.post('/api', async (req, res) => {
    const person = new Person({
        name: req.body.name,
        email: req.body.email
    });
    try {
        const data = await person.save();
        res.status(200).json(transform(data));
    }
    catch (error) {
        console.log(error.message)
        res.status(400).json({ message: error.message })
    }

})

app.get('/api', async (req, res) => {
    try {
        const data = await Person.find();
        res.json(data.map(transform))
    }
    catch (error) {
        res.status(500).json({ message: error.message })
    }
})


app.get('/api/:id', async (req, res) => {
    try {
        let data = await Person.findById(req.params.id)

        res.json(transform(data))
    }
    catch (error) {
        try {
            data = await Person.findOne({ name: req.params.id })

            res.json(transform(data))
        }
        catch (error) {
            res.status(500).json({ message: error.message })
        }
    }
})


app.patch('/api/:id', async (req, res) => {
    try {
        let data = await Person.findByIdAndUpdate(req.params.id, req.body, {new: true})

        res.json(transform(data))
    }
    catch (error) {
        try {
            data = await Person.findOneAndUpdate({ name: req.params.id }, req.body, {new: true})

            res.json(transform(data))
        }
        catch (error) {
            res.status(500).json({ message: error.message })
        }
    }
})

app.delete('/api/:id', async (req, res) => {
    try {
        let data = await Person.findByIdAndRemove(req.params.id, req.body, {new: true})

        res.json({message: `${data.name} has been deleted`})
    }
    catch (error) {
        try {
            data = await Person.findOneAndRemove({ name: req.params.id }, req.body, {new: true})

            res.json({message: `${data.name} has been deleted`})
        }
        catch (error) {
            res.status(500).json({ message: error.message })
        }
    }
})


app.listen(3000, () => {
    console.log(`Server Started at ${3000}`)
});


