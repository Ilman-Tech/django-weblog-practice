const form = document.getElementById('profile-form')
const saveButton = document.getElementById('save-button')

if (saveButton.disabled) {
    saveButton.style.cursor = "no-drop";
    saveButton.style.backgroundColor = "#d3d3d3";
    saveButton.style.color = "#000"
}
;

form.addEventListener("input", function () {
    saveButton.disabled = false;
    saveButton.style.cursor = "pointer";
    saveButton.style.backgroundColor = "#222";
    saveButton.style.color = "#fff";
});

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(form);

    const csrfToken = formData.get("csrfmiddlewaretoken")

    fetch('/profile/', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
        body: formData,
    }).then(function (response) {
        return response.json()
    }).then(function (data) {

        if (data) {

            const oldMessage = document.querySelector(".notification")

            if (oldMessage) {
                oldMessage.remove()
            }
            ;

            const message = document.createElement('div')
            message.classList.add('notification')
            message.textContent = data.message

            if (data.success) {
                message.classList.add('success')

                document.title = "profile - " + data.username;

                const h2Username = document.getElementById('profileUsername')
                h2Username.textContent = data.username

                saveButton.disabled = true
                saveButton.style.cursor = "no-drop";
                saveButton.style.backgroundColor = "#d3d3d3";
                saveButton.style.color = "#000"

            } else {
                message.classList.add('error')
            }

            document.body.appendChild(message)

            setTimeout(function () {
                message.remove();
            }, 3000);

        }

    }).catch(function (error) {
        console.log(error)
    });
});