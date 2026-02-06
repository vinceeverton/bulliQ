async function getCheckout(score) {
    try {
        const res = await fetch(`/api/checkout/${score}`);

        // 1. Check if the response was successful (status 200-299)
        if (!res.ok) {
            const errorText = await res.text(); // Read the error page/text
            console.error(`Server error (${res.status}):`, errorText);
            return;
        }

        // 2. Safely parse JSON
        const data = await res.json();

        const overlay = document.getElementById("checkoutOverlay");
        if (!overlay) return;

        overlay.innerText = data.checkout ?? "No checkout";
        overlay.style.display = "block";

        setTimeout(() => {
            overlay.style.display = "none";
        }, 5000);
    } catch (error) {
        // This will now only catch network issues or JSON syntax errors
        console.error("Error fetching checkout:", error);
    }
}
