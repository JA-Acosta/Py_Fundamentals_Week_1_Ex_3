'''
>>> JAAR
>>> 07/12/2023
>>> Practicing Fundamentals Program 3
>>> Version 1
'''
'''
>>> Generates a program that checks if a string is a palindrome and will reverse the string for the user to verify. The string length will then be used to generate a random number (inclusive) which will serve as n for the fibonacci sequence. Finally, a total of 5 numbers will be selected from the same range to calculate an average.
'''

import random

def main() :
    # Assume the user input will never be less than 1.
    inputted_string = input('Enter a word/phrase, and I will check if it is a palindrome: ').lower()
    string_len = len(inputted_string)
    reversed_input = inputted_string[::-1]

    palindrome_string_test = None
    if reversed_input == inputted_string :
        palindrome_string_test = 'is'
    else :
        palindrome_string_test = 'is not'

    print(f'\nThe word/phrase you inputted {palindrome_string_test} a palindrome. Here it is in reverse:\n\t{reversed_input}\n\n\tNOTE THAT YOUR INPUT WAS CONVERTED TO LOWERCASE FOR THE PURPOSE OF ACCURATELY ASSESSING IT FREE OF EXTENUATING FACTORS.\n\n')

    print(f'That was fun! Now lets get a little creative. I\'m going to generate a random number based on the length of your word/phrase and calculate the fibonacci sequence using that number as n.')
    random_numbers = [random.randint(0, string_len)]

    fibonacci_sequence = [0, 1]
    if random_numbers[0] > 1 :
        print(f'{random_numbers[0]}')
        for n in range(2, random_numbers[0] + 1) :
            fibonacci_sequence.append(fibonacci_sequence[n-1] + fibonacci_sequence[n-2])
    fibonacci_solution = fibonacci_sequence[random_numbers[-1]]
    print(f'''
        \tFor n = {random_numbers[0]}
        \tThe fibonacci sequence is: {fibonacci_solution}
        ''')

    print('Finally lets generate another 4 random numbers and calculate the average.')

    average_random_ints = None
    for _ in range(0, 4) :
        generated_rand = random.randint(0, string_len)
        while string_len > 4 and generated_rand in random_numbers :
            generated_rand = random.randint(0, string_len)
        random_numbers.append(generated_rand)
    average_random_ints = sum(float(n) for n in random_numbers) / len(random_numbers)

    print(f'''
        \tRandom numbers: {", ".join(str(n) for n in random_numbers)}
        \tAverage: {average_random_ints}
        ''')


    # fibonacci_solution, five rand generated, average random ints

if __name__ == '__main__' :
    main()