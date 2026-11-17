async function predict() {
    const name = document.getElementById("name").value.trim();
    const hours = document.getElementById("hours").value;
    const marks = document.getElementById("marks").value;
    const attendance = document.getElementById("attendance").value;

    if (!name || hours === "" || marks === "" || attendance === "") {
        alert("Please fill all fields!");
        return;
    }

    const values = [Number(hours), Number(marks), Number(attendance)];
    if (!values.every(Number.isFinite)) {
        alert("Please enter valid numbers!");
        return;
    }

    if (values[0] < 0 || values[0] > 24 ||
        values[1] < 0 || values[1] > 100 ||
        values[2] < 0 || values[2] > 100) {
        alert("Study hours must be 0 to 24, and marks and attendance must be 0 to 100.");
        return;
    }

    try {
        let data;
        if (window.location.hostname.endsWith(".github.io")) {
            const prediction =
                9.222583126763006 +
                2.9813659287118552 * values[0] +
                0.7176852722454908 * values[1] +
                0.017163860158987583 * values[2];
            const predictedMarks = Math.round(Math.max(0, Math.min(100, prediction)) * 100) / 100;

            data = {
                predicted_marks: predictedMarks,
                performance: predictedMarks >= 75
                    ? "Excellent"
                    : predictedMarks >= 40
                        ? "Average"
                        : "Needs Improvement"
            };
        } else {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    hours: values[0],
                    marks: values[1],
                    attendance: values[2]
                })
            });

            data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Server error: " + response.status);
            }
        }

        if (!Number.isFinite(data.predicted_marks) || typeof data.performance !== "string") {
            throw new Error("The server returned an invalid prediction.");
        }

        const output = document.getElementById("output");
        output.replaceChildren();
        output.append(
            document.createTextNode("Student: " + name),
            document.createElement("br"),
            document.createTextNode("Predicted Marks: " + data.predicted_marks),
            document.createElement("br"),
            document.createTextNode("Performance: " + data.performance)
        );

        document.getElementById("result").style.display = "block";

    } catch (error) {
        alert("Error: " + error.message);
        console.error(error);
    }
}
