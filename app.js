// app.js

document.addEventListener("DOMContentLoaded", function() {
    // This script will handle client-side interactions if needed
    console.log("To-Do App Loaded");

    // Example: Add task dynamically to the list (can be extended as per your logic)
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const title = document.querySelector('#title').value;
        const newTask = document.createElement('li');
        newTask.textContent = title;
        document.querySelector('#todo-list ul').appendChild(newTask);
        form.reset();
    });
});
