window.onload = () => {
    console.log("BulliQ Script Active");
    const calibrateBtn = document.getElementById('calibrateBtn');
    const checkoutBtn = document.getElementById('checkoutBtn');
    const scoreInput = document.getElementById('scoreInput');

    if (checkoutBtn) {
        checkoutBtn.onclick = () => {
            const score = scoreInput.value;
            console.log("Requesting checkout for:", score);
            if (score) getCheckout(score);
        };
    }
    
    if (calibrateBtn) {
        calibrateBtn.onclick = async () => {
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
        };
    }
}; // This brace now correctly closes the window.onload function

async function getCheckout(score) {
    const overlay = document.getElementById("checkoutOverlay");
    console.log("Checking score:", score); 

    try {
        const res = await fetch(`/api/checkout/${score}`);
        const data = await res.json();

        if (data.checkout) {
            overlay.innerText = data.checkout.join(" - ");
            
            // FORCE VISIBILITY
            overlay.style.setProperty('display', 'block', 'important');
            console.log("Overlay should now be visible with text:", overlay.innerText);

            setTimeout(() => {
                overlay.style.display = "none";
            }, 5000);
        } else {
            console.log("No checkout for score:", score);
        }
    } catch (err) {
        console.error("Fetch error:", err);
    }
}
