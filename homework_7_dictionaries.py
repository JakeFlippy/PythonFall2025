#Similar to homework 4, write a program that takes a series of commands that allow the user to manipulate text in various ways. This time, you will be using a dictionary to keep track of words that should be replaced with other words. The commands should be as follows:

#add: Adds a new substitution to the dictionary by asking for a word to be replaced and a word to replace it with.
#describe: Prints out all active substitutions in the dictionary.
#run: Ask the user for a sentence. Use your dictionary to make all of the necessary substitutions, then print out the resulting sentence.
#exit: Exit the program.

def run_substitution_program():
    substitutions = {}  # Dictionary to store word substitutions

    while True:
        command = input("Enter command (add, describe, run, #exit): ")

        if command == "add":
            word_to_replace = input("Enter the word to be replaced: ")
            replacement_word = input("Enter the word to replace it with: ")
            substitutions[word_to_replace] = replacement_word
            print("Substitution " {word_to_replace} "->" {replacement_word} " added.")

        elif command == "describe":
            if substitutions:
                print("Active substitutions:")
                for old_word, new_word in substitutions.items():
                    print("  "{old_word} "will be replaced by" {new_word})
            else:
                print("No active substitutions.")

        elif command == "run":
            sentence = input("Enter a sentence: ")
            processed_sentence = []
            words = sentence.split()  

            for word in words:
                if word.lower() in substitutions:
                    processed_sentence.append(substitutions[word.lower()])
                else:
                    processed_sentence.append(word)

            print("Resulting sentence:", " ".join(processed_sentence))

        elif command == "#exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid command. Please use 'add', 'describe', 'run', or '#exit'.")

# Run the program
run_substitution_program()
