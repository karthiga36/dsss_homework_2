import random


def generateRamdomValue(mini, maxi):
    """Generate a random integer between min_val and max_val."""
    return random.randint(mini, maxi)

def pickRandomOperator():
    """Randomly choose an operator: +, -, or *."""
    return random.choice(['+', '-', '*'])


def evaluate(num1, num2, operator):
    """Create a math expression and calculate its result based on the operator."""
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return expression, result

def math_quiz():
    """Execute quiz."""
    #Initializing score and total questions
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Looping through total questions
    for _ in range(total_questions):
        num1 = generateRamdomValue(1, 10)
        num2 = generateRamdomValue(1, 5)
        operator = pickRandomOperator()

        problem, answer = evaluate(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        #Try-except block for handling expception in user entered input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        #Print success/failure message based on user answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
