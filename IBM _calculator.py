#IBM calculator
"""
PROJECT DESCRIPTION :
Create a command-line BMI calculator in Python. Prompt users for their weight (in kilograms) and height (in meters).
 Calculate the BMI and classify it into categories (e.g., underweight, normal, overweight) based on predefined ranges.
 Display the BMI result and category to the user.
 """
def calculate_bmi(weight_kg, height_m):
    """
    Calculates BMI and returns the result along with the category.
    :param weight_kg: Weight in kilograms
    :param height_m: Height in meters
    :return: Tuple (BMI, category)
    """
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

def main():
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        bmi, category = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi:.2f} ({category}).")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
