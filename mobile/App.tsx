import { Text, View, Button } from "react-native";
import { useState } from "react";

const API_URL = "http://172.20.10.3:22"; // change to Pi IP

export default function App() {
  const [route, setRoute] = useState<string>("");

  const fetchCheckout = async () => {
    const res = await fetch(`${API_URL}/checkout/40`);
    const data = await res.json();
    setRoute(data.route.join(" → "));
  };

  return (
    <View style={{ padding: 40 }}>
      <Text style={{ fontSize: 28 }}>BullIQ</Text>
      <Button title="Get Checkout" onPress={fetchCheckout} />
      <Text style={{ marginTop: 20 }}>{route}</Text>
    </View>
  );
}