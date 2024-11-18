from abc import ABC, abstractmethod

# Step 1: Define the client interface
class Client(ABC):
    def __init__(self, name, car_model, car_price):
        self.name = name
        self.car_model = car_model
        self.car_price = car_price

    @abstractmethod
    def get_final_price(self):
        pass

    @abstractmethod
    def get_insurance_plan(self):
        pass

    @abstractmethod
    def get_service_plan(self):
        pass

    def save_to_file(self):
        filename = f"{self.name.replace(' ', '_')}_car_purchase.txt"
        with open(filename, "w") as file:
            file.write(f"Customer Name: {self.name}\n")
            file.write(f"Car Model: {self.car_model}\n")
            file.write(f"Base Price: ${self.car_price}\n")
            file.write(f"Final Price: ${self.get_final_price()}\n")
            file.write(f"Insurance Plan: {self.get_insurance_plan()}\n")
            file.write(f"Service Plan: {self.get_service_plan()}\n")
        return filename

# Step 2: Implement classes for each client type
class CashClient(Client):
    def get_final_price(self):
        # Apply discount for cash payment
        return self.car_price * 0.9

    def get_insurance_plan(self):
        return "Standard insurance with 2 years coverage."

    def get_service_plan(self):
        return "3 years free maintenance service."

class CreditClient(Client):
    def get_final_price(self):
        # No discount, added interest
        return self.car_price * 1.1

    def get_insurance_plan(self):
        return "Premium insurance with 5 years coverage."

    def get_service_plan(self):
        return "1 year free maintenance service."

class InstallmentClient(Client):
    def get_final_price(self):
        # Slightly increased price due to installments
        return self.car_price * 1.05

    def get_insurance_plan(self):
        return "Standard insurance with 3 years coverage."

    def get_service_plan(self):
        return "2 years free maintenance service."

# Step 3: Factory class to create clients based on type
class ClientFactory:
    @staticmethod
    def create_client(client_type, name, car_model, car_price):
        if client_type == "cash":
            return CashClient(name, car_model, car_price)
        elif client_type == "credit":
            return CreditClient(name, car_model, car_price)
        elif client_type == "installment":
            return InstallmentClient(name, car_model, car_price)
        else:
            raise ValueError("Unknown client type")

# Example usage:
client = ClientFactory.create_client("cash", "John Doe", "Toyota Corolla", 20000)
file_path = client.save_to_file()
file_path

