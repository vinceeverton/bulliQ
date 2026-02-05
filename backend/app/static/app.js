async function getCheckout() {
  const remaining = document.getElementById("remaining").value;
  if (!remaining) return;

  const res = await fetch(`/api/checkout/${remaining}`);
  const data = await res.json();

  document.getElementById("result").innerText =
    data.route.join(" → ");
}