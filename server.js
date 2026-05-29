const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

app.use(express.static(__dirname));

// Route /admin to admin.html
app.get('/admin', (req, res) => {
    try {
        const content = fs.readFileSync(path.join(__dirname, 'admin.html'), 'utf-8');
        res.setHeader('Content-Type', 'text/html');
        res.send(content);
    } catch (err) {
        res.status(500).send("Error reading admin.html: " + err.message);
    }
});

// Route /login to login.html
app.get('/login', (req, res) => {
    try {
        const content = fs.readFileSync(path.join(__dirname, 'login.html'), 'utf-8');
        res.setHeader('Content-Type', 'text/html');
        res.send(content);
    } catch (err) {
        res.status(500).send("Error reading login.html: " + err.message);
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Pranav Enterprises Server running at http://localhost:${PORT}`);
});
