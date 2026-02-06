document.addEventListener('DOMContentLoaded', () => {
    const calibrateBtn = document.getElementById('calibrateBtn');
    const checkoutBtn = document.getElementById('checkoutBtn');
    const scoreInput = document.getElementById('scoreInput');

    // 1. Checkout Button Logic
    if (checkoutBtn) {
        checkoutBtn.addEventListener('click', () => {
            const score = scoreInput.value;
            if (score) {
                getCheckout(score);
            } else {
                alert("Please enter a score first!");
            }
        });
    }

    // 2. Calibration Button Logic
    if (calibrateBtn) {
        calibrateBtn.addEventListener('click', async () => {
            console.log("Sending calibration request...");
            try {
                const response = await fetch('/calibrate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ timestamp: Date.now(), action: 'calibrate' })
                });
                const data = await response.json();
                alert("Server says: " + data.status);
            } catch (err) {
                console.error("Calibration failed:", err);
            }
        });
    }
});

async function getCheckout(score) {
    const overlay = document.getElementById("checkoutOverlay");
    try {
        const res = await fetch(`/api/checkout/${score}`);
        const data = await res.json();

        if (data.checkout) {
            overlay.innerText = data.checkout.join(" - ");
            overlay.style.display = "block";
            // Hide after 5 seconds
            setTimeout(() => { overlay.style.display = "none"; }, 5000);
        } else {
            alert(data.message || "No checkout available");
        }
    } catch (error) {
        console.error("Error fetching checkout:", error);
    }
}
