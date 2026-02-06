function getCheckout(score) {
    fetch(`/api/checkout/${score}`)
        .then(res => res.json())
        .then(data => {
            const checkoutEl = document.getElementById("checkoutOverlay");
            const scoreEl = document.getElementById("scoreOverlay");

            if (!checkoutEl || !scoreEl) return;

            scoreEl.innerText = `Score: ${score}`;

            if (data.route && Array.isArray(data.route)) {
                checkoutEl.innerText = "Checkout: " + data.route.join(" → ");
            } else if (data.checkout) {
                checkoutEl.innerText = "Checkout: " + data.checkout;
            } else {
                checkoutEl.innerText = "Checkout: —";
            }
        })
        .catch(() => {
            const checkoutEl = document.getElementById("checkoutOverlay");
            if (checkoutEl) checkoutEl.innerText = "Checkout: Error";
        });
}