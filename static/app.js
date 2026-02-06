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
function updateCheckout(score) {
    fetch(`/api/checkout/${score}`)
        .then(res => res.json())
        .then(data => {
            const overlay = document.getElementById("checkoutOverlay");

            if (data.checkout) {
                overlay.innerText = `Checkout: ${data.checkout.join(" → ")}`;
            } else {
                overlay.innerText = data.message || "No checkout";
            }
        })
        .catch(() => {
            document.getElementById("checkoutOverlay").innerText = "Error";
        });
}

// TEMP TEST — replace later with real score detection
setInterval(() => {
    const testScores = [170, 121, 100, 60, 40, 32];
    const score = testScores[Math.floor(Math.random() * testScores.length)];
    updateCheckout(score);
}, 3000);