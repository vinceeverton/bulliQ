import { Text, View, Button } from "react-native";
import { useState } from "react";

export default function App() {
  const [route, setRoute] = useState("");

  const getCheckout = async () => {
    const res = await fetch("http://localhost:8000/checkout/40");
    const data = await res.json();
    setRoute(data.route.join(" → "));
  };

  return (
    <View style={{ padding: 40 }}>
      <Text style={{ fontSize: 28 }}>BullIQ 🎯</Text>
      <Button title="Get Checkout for 40" onPress={getCheckout} />
      <Text style={{ marginTop: 20, fontSize: 20 }}>{route}</Text>
    </View>
  );
}