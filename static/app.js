async function getCheckout() {
  const remaining = document.getElementById("remaining").value;
  if (!remaining) return;

  const res = await fetch(`/api/checkout/${remaining}`);
  const data = await res.json();

  const resultEl = document.getElementById("result");

if (data.route && Array.isArray(data.route)) {
    resultEl.innerText = data.route.join(" → ");
} else if (data.checkout) {
    resultEl.innerText = data.checkout;
} else {
    resultEl.innerText = "";
}
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("calibrateBtn");
    if (!btn) return;

    btn.onclick = async () => {
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
});
async function getCheckout(score) {
    try {
        const res = await fetch(`/api/checkout/${score}`);
        const data = await res.json();

        const checkoutEl = document.getElementById("checkoutOverlay");
        const scoreEl = document.getElementById("scoreOverlay");

        scoreEl.innerText = `Score: ${score}`;

        if (data.route && Array.isArray(data.route)) {
            checkoutEl.innerText = "Checkout: " + data.route.join(" → ");
        } else if (data.checkout) {
            checkoutEl.innerText = "Checkout: " + data.checkout;
        } else {
            checkoutEl.innerText = "Checkout: —";
        }
    } catch (e) {
        document.getElementById("checkoutOverlay").innerText = "Checkout: Error";
    }
  } catch(e) {
            document.getElementById("checkoutOverlay").innerText = "Error";
        };
      }
