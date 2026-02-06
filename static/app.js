async function getCheckout(score) {
    const overlay = document.getElementById("checkoutOverlay");
    if (!overlay) return;

    try {
        const res = await fetch(`/api/checkout/${score}`);
        const data = await res.json();

        // If the API found a checkout
        if (data.checkout) {
            // Join array ["20", "D20"] into "20 - D20"
            overlay.innerText = Array.isArray(data.checkout) ? data.checkout.join(" - ") : data.checkout;
            overlay.style.display = "block";
            
            console.log("Showing checkout:", overlay.innerText);

            setTimeout(() => {
                overlay.style.display = "none";
            }, 5000);
        } else {
            // If no checkout (like score 501), show the message
            overlay.innerText = data.message || "No Checkout";
            overlay.style.display = "block";
            setTimeout(() => { overlay.style.display = "none"; }, 3000);
        }
    } catch (error) {
        console.error("Error fetching checkout:", error);
    }
}
