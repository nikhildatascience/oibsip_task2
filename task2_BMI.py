def calculate_BMI(weight, height):
    return weight / (height ** 2)
def classify_BMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Please enter your weight in kilograms (kg): "))
        height = float(input("Now, enter your height in meters (m): "))
        if weight <= 0 or height <= 0:
            print("Your weight and height must be positive numbers. Please try again.")
            return
        bmi = calculate_BMI(weight, height)
        category = classify_BMI(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Based on your BMI, you are classified as: {category}.\n")
    except ValueError:
        print("Please try again with proper numerical values.")
if __name__ == "__main__":
    main()
