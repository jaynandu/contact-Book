// Fetch contacts from the backend
async function loadContacts() {
    const response = await fetch('/contacts', {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
    });

    if (!response.ok) {
        alert('Failed to load contacts. Please check your token or server.');
        return;
    }

    const contacts = await response.json();
    const contactList = document.getElementById('contact-list');
    contactList.innerHTML = ''; // Clear previous entries

    contacts.forEach(contact => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>Name:</span> ${contact.name} <br>
            <span>Email:</span> ${contact.email} <br>
            <span>Phone:</span> ${contact.phone}
        `;
        contactList.appendChild(li);
    });
}

// Add a new contact
async function addContact(event) {
    event.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();

    if (!name || !email || !phone) {
        alert('All fields are required.');
        return;
    }

    const response = await fetch('/contacts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify({ name, email, phone }),
    });

    if (response.ok) {
        alert('Contact added successfully!');
        document.getElementById('contact-form').reset();
        loadContacts();
    } else {
        const error = await response.json();
        alert(`Error: ${error.message || 'Failed to add contact.'}`);
    }
}

// Attach event listeners
document.getElementById('contact-form').addEventListener('submit', addContact);

// Load contacts on page load
loadContacts();
