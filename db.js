const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.resolve(__dirname, 'database.sqlite');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error opening database', err.message);
    } else {
        console.log('Connected to the SQLite database.');
        
        // Create Users table
        db.run(`CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )`, (err) => {
            if (!err) {
                // Insert default admin user if not exists
                db.get(`SELECT * FROM users WHERE username = ?`, ['admin'], (err, row) => {
                    if (!row) {
                        db.run(`INSERT INTO users (username, password) VALUES (?, ?)`, ['admin', 'password']);
                        console.log('Created default admin user (admin / password)');
                    }
                });
            }
        });

        // Create Products table
        db.run(`CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            sku TEXT,
            status TEXT,
            date_added TEXT,
            inventory INTEGER,
            image_url TEXT
        )`, (err) => {
            if (!err) {
                // Insert some initial data if the table is empty
                db.get(`SELECT COUNT(*) as count FROM products`, (err, row) => {
                    if (row && row.count === 0) {
                        const defaultProducts = [
                            ['Precision One Smartwatch', 'PROD-772-B', 'Published', 'Oct 24, 2023', 428, 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&q=80&w=200&h=200'],
                            ['Acoustic Pro Headphones', 'AUD-991-A', 'Draft', 'Nov 02, 2023', 1200, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&q=80&w=200&h=200'],
                            ['Executive Chrono V2', 'WAT-112-X', 'Published', 'Oct 15, 2023', 84, 'https://images.unsplash.com/photo-1524592094714-0f0654ece975?auto=format&fit=crop&q=80&w=200&h=200']
                        ];
                        
                        const stmt = db.prepare(`INSERT INTO products (name, sku, status, date_added, inventory, image_url) VALUES (?, ?, ?, ?, ?, ?)`);
                        defaultProducts.forEach(product => {
                            stmt.run(product);
                        });
                        stmt.finalize();
                        console.log('Inserted default products');
                    }
                });
            }
        });
    }
});

module.exports = db;
