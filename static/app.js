async function getCheckout() {
  const remaining = document.getElementById("remaining").value;
  if (!remaining) return;

  const res = await fetch(`/api/checkout/${remaining}`);
  const data = await res.json();

  document.getElementById("result").innerText =
    data.route.join(" → ");
}
document.getElementById("calibrateBtn").onclick = async () => {
  const response = await fetch("/calibrate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      points: [{ x: 100, y: 100 }]
    })
  });

  const result = await response.json();
  alert(result.status);
};