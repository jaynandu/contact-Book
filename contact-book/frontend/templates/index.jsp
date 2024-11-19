<%@ include file="../secure_headers.jsp" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Book</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <div id="app">
        <header>
            <h1>Contact Book</h1>
        </header>

        <main>
            <form id="contact-form">
                <input type="text" id="name" placeholder="Name" required>
                <input type="email" id="email" placeholder="Email" required>
                <input type="text" id="phone" placeholder="Phone" required>
                <button type="submit">Add Contact</button>
            </form>

            <ul id="contact-list">
                <!-- Contacts will be rendered here dynamically -->
            </ul>
        </main>
    </div>

    <script src="/static/app.js"></script>
</body>
</html>
