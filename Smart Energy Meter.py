# Smart Energy Meter
# Python Project for EEE Students

class SmartEnergyMeter:

    def __init__(self, voltage, current, power_factor, tariff):
        self.voltage = voltage
        self.current = current
        self.power_factor = power_factor
        self.tariff = tariff

    # Calculate active power
    def calculate_power(self):
        power = self.voltage * self.current * self.power_factor
        return power / 1000  # Convert W to kW

    # Calculate energy consumed
    def calculate_energy(self, hours):
        power = self.calculate_power()
        return power * hours

    # Calculate electricity bill
    def calculate_bill(self, energy):
        return energy * self.tariff

    def display(self, hours):
        power = self.calculate_power()
        energy = self.calculate_energy(hours)
        bill = self.calculate_bill(energy)

        print("\n====================================")
        print("        SMART ENERGY METER")
        print("====================================")

        print(f"Voltage          : {self.voltage:.2f} V")
        print(f"Current          : {self.current:.2f} A")
        print(f"Power Factor     : {self.power_factor:.2f}")
        print(f"Power            : {power:.2f} kW")
        print(f"Operating Hours  : {hours:.2f} hours")
        print(f"Energy Consumed  : {energy:.2f} kWh")
        print(f"Tariff           : ₹{self.tariff:.2f}/kWh")
        print(f"Electricity Bill : ₹{bill:.2f}")

        print("====================================")


# User input
voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
power_factor = float(input("Enter Power Factor: "))
hours = float(input("Enter Operating Hours: "))
tariff = float(input("Enter Tariff (₹/kWh): "))

# Validate inputs
if voltage <= 0 or current < 0:
    print("Invalid voltage or current!")
elif power_factor <= 0 or power_factor > 1:
    print("Power factor must be between 0 and 1!")
elif hours < 0 or tariff < 0:
    print("Hours and tariff cannot be negative!")
else:
    meter = SmartEnergyMeter(
        voltage,
        current,
        power_factor,
        tariff
    )

    meter.display(hours)
