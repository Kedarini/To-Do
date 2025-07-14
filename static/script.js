function OpenForm(index = null, name = '', due_date = '') {
    document.getElementById('popup-overlay').style.display = 'block';
    document.getElementById('popup-form').style.display = 'block';

    let taskDisplay = document.getElementById('taskname-display');
    let nameInput = document.getElementById('taskname-input');
    let dueDateInput = document.getElementById('due_date');
    let indexInput = document.getElementById('task-index-hidden');
    let form = document.getElementById('add-task-form');

    if (index !== null && index !== undefined) {
        // Editing
        taskDisplay.textContent = "Edit Task";
        nameInput.value = name;
        dueDateInput.value = due_date;
        indexInput.value = index;
        form.action = `/edit/${index}`;
    } else {
        // Adding
        taskDisplay.textContent = "Add Task";
        nameInput.value = name && name.trim() ? name : "New Task";
        dueDateInput.value = '';
        indexInput.value = '';
        form.action = '/add';
    }
}

function CloseForm() {
    document.getElementById("popup-overlay").style.display = "none";
    document.getElementById("popup-form").style.display = "none";
}

window.onclick = function(event) {
    const overlay = document.getElementById("popup-overlay");
    if (event.target === overlay) {
        CloseForm();
    }
}

document.getElementById('add-task-form').onsubmit = async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);

    const response = await fetch(form.action, {
        method: 'POST',
        body: data
    });

    if (response.ok) {
        // Optionally, update the task list dynamically here
        location.reload(); // Simple way: reload to see the new task
    } else {
        alert('Failed to add task');
    }
};

function confirmDelete(index, btn) {
    if (confirm("Are you sure you want to delete this task?")) {
        // Show trash can emoji centered for feedback
        btn.innerHTML = "&#128465;";
        btn.style.background = "#ff6666";
        btn.style.color = "#fff";
        btn.style.borderRadius = "50%";
        btn.style.display = "flex";
        btn.style.alignItems = "center";
        btn.style.justifyContent = "center";
        // Submit the hidden form after a short delay for effect
        setTimeout(() => {
            document.getElementById(`delete-form-${index}`).submit();
        }, 400);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const enableDeleteBtn = document.getElementById('Enable-Delete-Button');
    if (enableDeleteBtn) {
        enableDeleteBtn.addEventListener('click', function() {
            document.querySelectorAll('.delete-btn').forEach(btn => {
                btn.classList.add('enabled');
            });
        });
    }
});