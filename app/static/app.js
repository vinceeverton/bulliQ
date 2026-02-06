async function getCheckout(score) {
    const cleanScore = Math.floor(Number(score));
    if (isNaN(cleanScore) || cleanScore < 2) return;

    const overlay = document.getElementById("checkoutOverlay");
    if (!overlay) return;

    try {
        const res = await fetch(`/api/checkout/${cleanScore}`);
        const data = await res.json();

        if (data.checkout) {
            overlay.innerText = data.checkout.join(" - ");
            overlay.style.display = "block";
            console.log("Displayed:", overlay.innerText);
            
            setTimeout(() => { overlay.style.display = "none"; }, 5000);
        }
    } catch (err) {
        console.error("Fetch error:", err);
    }
}
