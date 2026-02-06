async function getCheckout(score) {
    const cleanScore = Math.floor(Number(score));
    if (isNaN(cleanScore) || cleanScore < 2) return;

    const overlay = document.getElementById("checkoutOverlay");
    if (!overlay) {
        console.error("Could not find checkoutOverlay in the HTML!");
        return;
    }

    try {
        // Use the absolute path starting with /api
        const res = await fetch(`/api/checkout/${cleanScore}`);
        
        if (!res.ok) {
            console.error(`API Error: ${res.status}`);
            return;
        }

        const data = await res.json();

        if (data.checkout) {
            // Join the array: ["T20", "D20"] -> "T20 - D20"
            overlay.innerText = Array.isArray(data.checkout) ? data.checkout.join(" - ") : data.checkout;
            overlay.style.display = "block";
            
            // Keeps it on screen for 5 seconds
            setTimeout(() => { overlay.style.display = "none"; }, 5000);
        }
    } catch (err) {
        console.error("Fetch failed:", err);
    }
}
