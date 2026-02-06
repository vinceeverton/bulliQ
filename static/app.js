async function getCheckout(score) {
    try {
        const res = await fetch(`/api/checkout/${score}`);
        const data = await res.json();

        const overlay = document.getElementById("checkoutOverlay");
        if (!overlay) return;

        overlay.innerText = data.checkout ?? "No checkout";
    } catch (e) {
        console.error("Error fetching checkout:", e);
    }
}