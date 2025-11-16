// Grab HTML elements
const btn = document.getElementById("createBtn");
const status = document.getElementById("status");
const ctx = document.getElementById("bellChart").getContext("2d");

let chart = null;

// Fetch Bell state counts from backend
async function fetchBellState() {
  status.innerText = "Running simulation...";

  try {
    //const response = await fetch("http://localhost:8000/bellstate"); this one is for running project localy
    const response = await fetch("https://quantum-bellstate.onrender.com/bellstate")
    const data = await response.json();
    const counts = data.counts;

    status.innerText = "Simulation complete!";

    const labels = Object.keys(counts);
    const values = Object.values(counts);

    // Destroy previous chart if it exists
    if (chart) chart.destroy();

    // Draw chart
    chart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{
          label: "Measurement Counts",
          data: values,
          backgroundColor: "#4f46e5"
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });

  } catch (err) {
    console.error(err);
    status.innerText = "Error fetching data. Check if backend is running.";
  }
}

// Click event to button
btn.addEventListener("click", fetchBellState);
