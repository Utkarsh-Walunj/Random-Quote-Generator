import random

# List of quotes
quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
]

def get_random_quote():
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        user_input = input("Press Enter to get a random quote or 'Q' to quit: ")
        if user_input.lower() == 'q':
            break
        else:
            print(get_random_quote())

if __name__ == "__main__":
    main()
