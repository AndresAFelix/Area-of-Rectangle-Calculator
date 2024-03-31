# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Main function
def main():
    # Input length and width from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area
    area = calculate_rectangle_area(length, width)

    # Display the result
    print("The area of the rectangle is:", area)

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    main()