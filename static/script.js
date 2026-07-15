async function analyzeTicket() {

    const ticket = document.getElementById("ticket").value.trim();

    if (ticket === "") {
        alert("Please enter a ticket.");
        return;
    }

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ticket: ticket
            })
        });

        const data = await response.json();

        document.getElementById("result").style.display = "block";
        document.getElementById("category").innerText = data.category;
        document.getElementById("confidence").innerText = data.confidence;
        document.getElementById("response").innerText = data.response;

    } catch (error) {
        console.error(error);
        alert("Error connecting to Flask server.");
    }
}