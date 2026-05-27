# Rohit Enterprises - Professional Solutions

Welcome to the **Rohit Enterprises** web application repository. This is a modern, responsive, and beautifully designed web application built to serve as a digital storefront and administrative panel for a trusted local enterprise in Sawantwadi, Sindhudurg. 

## 🌟 Key Features

- **Dynamic Homepage**: Fast and visually appealing landing page that showcases the core values and identity of the business.
- **Product Gallery**: Elegant grid display for the finest selections and collections, dynamically populated from the database.
- **Project Portfolio (Our Work)**: A dedicated space to display successful projects and services rendered to clients.
- **Bilingual Support**: Instant toggle between English and Marathi (मराठी) across the entire application for local and wider audiences.
- **Admin Dashboard**: A secure back-end panel for the owner to add, edit, or delete products and works, mark items as "Sold Out," and "Pin" items to the top of the gallery.
- **Fully Responsive**: Carefully optimized layout and mobile navigation for perfect usability across desktop, tablet, and mobile devices.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)
- **Design System**: Material Design Icons, Google Fonts (Playfair Display, Inter, etc.)
- **Backend/Database**: Firebase Firestore (for storing and managing products & works)
- **Deployment**: Vercel

## 🚀 Getting Started

### Prerequisites

To run this project locally, you will need a simple HTTP server (like `Live Server` in VS Code, or Python's `http.server`) and a Firebase project.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/rohit-enterprises.git
   cd rohit-enterprises
   ```

2. **Set up Firebase:**
   Create a file named `firebase-config.js` in the root directory and add your Firebase configuration:
   ```javascript
   export const firebaseConfig = {
     apiKey: "YOUR_API_KEY",
     authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
     projectId: "YOUR_PROJECT_ID",
     storageBucket: "YOUR_PROJECT_ID.appspot.com",
     messagingSenderId: "YOUR_SENDER_ID",
     appId: "YOUR_APP_ID"
   };
   ```

3. **Run Locally:**
   Serve the directory using any static file server.
   ```bash
   npx serve .
   ```
   Open `http://localhost:3000` in your browser.

## 🔒 Administrative Access

To manage products and portfolio works, navigate to `/admin.html`. The admin panel allows you to seamlessly update the content visible on the homepage using Firebase Firestore. 

*Note: Ensure proper Firestore security rules are configured in your Firebase console to protect administrative operations in a production environment.*

## 📄 License

© 2024 Rohit Enterprises. All rights reserved.
