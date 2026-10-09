async function analyzeIssue() {

    const question =
        document.getElementById("question").value.trim();

    const answer =
        document.getElementById("answer");

    const loading =
        document.getElementById("loading");

    const result =
        document.getElementById("result");

    const button =
        document.getElementById("analyzeButton");


    if (!question) {
        alert("Please describe an Azure issue.");
        return;
    }


    loading.innerText = "Analyzing issue...";

    answer.innerText = "";

    result.classList.add("hidden");

    button.disabled = true;


    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error("Request failed");
        }


        answer.innerText = data.answer;

        result.classList.remove("hidden");


    } catch (error) {

        answer.innerText =
            "The assistant could not process the request.";

        result.classList.remove("hidden");

    } finally {

        loading.innerText = "";

        button.disabled = false;

    }
}