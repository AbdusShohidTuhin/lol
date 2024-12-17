class SoilTreatment:
    def __init__(self, soil_type, ph, organic_matter):
        self.soil_type = soil_type
        self.ph = ph
        self.organic_matter = organic_matter
        self.growth_rate = 0

    def apply_inorganic_fertilizer(self, nitrogen, phosphorus, potassium):
        self.growth_rate += 0.5 * (nitrogen + phosphorus + potassium)
        self.ph -= 0.1  # Slight acidity increase
        result = f"Applied inorganic fertilizer: Nitrogen = {nitrogen}, Phosphorus = {phosphorus}, Potassium = {potassium}, Growth rate = {self.growth_rate}, pH = {self.ph}"
        self.save_result(result)
        return result

    def apply_biochar(self, amount):
        self.growth_rate += 0.3 * amount
        self.ph += 0.2  # pH buffering effect
        self.organic_matter += 0.1 * amount
        result = f"Applied biochar: Amount = {amount}, Growth rate = {self.growth_rate}, pH = {self.ph}, Organic matter = {self.organic_matter}"
        self.save_result(result)
        return result

    def apply_compost(self, amount):
        self.growth_rate += 0.4 * amount
        self.organic_matter += 0.2 * amount
        result = f"Applied compost: Amount = {amount}, Growth rate = {self.growth_rate}, Organic matter = {self.organic_matter}"
        self.save_result(result)
        return result

    def evaluate_soil_health(self):
        health_score = (self.growth_rate + self.organic_matter) / 2
        result = f"Soil Health Score: Growth rate = {self.growth_rate}, Organic matter = {self.organic_matter}, Health Score = {health_score:.2f}"
        self.save_result(result)
        return result

    def save_result(self, result):
        with open("soil_treatment_results.txt", "a") as file:
            file.write(result + "\n")

# Example usage
if __name__ == "__main__":
    soil_type = input("Enter soil type: ")
    ph = float(input("Enter initial pH level: "))
    organic_matter = float(input("Enter initial organic matter content: "))

    soil = SoilTreatment(soil_type=soil_type, ph=ph, organic_matter=organic_matter)

    while True:
        print("\nChoose an option:")
        print("1. Apply Inorganic Fertilizer")
        print("2. Apply Biochar")
        print("3. Apply Compost")
        print("4. Evaluate Soil Health")
        print("5. Save All Results to File")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            nitrogen = float(input("Enter nitrogen amount: "))
            phosphorus = float(input("Enter phosphorus amount: "))
            potassium = float(input("Enter potassium amount: "))
            result = soil.apply_inorganic_fertilizer(nitrogen, phosphorus, potassium)
            print(result)
        elif choice == "2":
            amount = float(input("Enter biochar amount: "))
            result = soil.apply_biochar(amount)
            print(result)
        elif choice == "3":
            amount = float(input("Enter compost amount: "))
            result = soil.apply_compost(amount)
            print(result)
        elif choice == "4":
            result = soil.evaluate_soil_health()
            print(result)
        elif choice == "5":
            print("All results have been saved to file.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
