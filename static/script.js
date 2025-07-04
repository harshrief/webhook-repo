async function loadEvents() {
    const response = await fetch('/events');
    const data = await response.json();

    const list = document.getElementById('events');
    list.innerHTML = '';

    data.forEach(event => {
        const li = document.createElement('li');
        li.textContent = event.message;
        list.appendChild(li);
    });
}

loadEvents();
setInterval(loadEvents, 15000);

