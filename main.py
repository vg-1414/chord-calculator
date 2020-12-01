
# Import the custom calcmod module.
import calcmod

# Function: The primary main() wrapper to house the complete program.
# Input: none.
# Output: the entire program.
def main():

    # Welcome the user to the program and give a brief description.
    calcmod.print_welcome_message()

    # Set calculate_chord to 'y' for use with a while loop
    calculate_chord = "y"
    while calculate_chord == "y":

        # Present the list of available note names.
        calcmod.print_note_names()

        # Prompt the user to make a selection, and verify its validity.
        root_note = calcmod.pick_root_note()

        # Present the list of available chord types.
        calcmod.print_chord_types()

        # Prompt the user to make a selection, and verify its validity.
        chord_type = calcmod.pick_chord_type()

        # If the user selects a dominant chord...
        if chord_type == "Dominant seventh":
            # ...give them the option to alter it for jazzier sounds.
            dominant_updates = calcmod.update_dominant_chord()

        # Sort the chromatic scale to match the user's root note selection.
        chromatic_scale = calcmod.sort_chromatic_scale(root_note)

        # If the dominant_updates list exists...
        if "dominant_updates" in locals():
            # ...include it as an argument for extraction.
            chord_tones = calcmod.extract_chord_tones(chromatic_scale, chord_type, dominant_updates)
        else:
            chord_tones = calcmod.extract_chord_tones(chromatic_scale, chord_type)

        # Determine if the user wants to calculate frequencies
        chord_frequencies = calcmod.include_frequencies(chord_tones)

        # First check if any dominant updates are available.
        if "dominant_updates" in locals():
            # If so, specify them as an argument.
            final_results = calcmod.return_results(root_note, chromatic_scale, chord_type, chord_tones, chord_frequencies, dominant_updates)
        else:
            final_results = calcmod.return_results(root_note, chromatic_scale, chord_type, chord_tones, chord_frequencies)

        # Print out the results on the screen.
        print(final_results)

        # Ask the user if they would like to export the results.
        calcmod.export_results(final_results)

        # Determine whether to continue or exit the program,
        # using a while loop to validate input.
        run_again_answer = ""
        while len(run_again_answer) < 1:
            answer = input("Would you like to calculate another chord?  Please enter 'y' or 'n': ")
            # If yes, start at the top.
            if answer == "y":
                run_again_answer = "y"
                calculate_chord = "y"
            # Otherwise, bail out and thank the user for using the program.
            elif answer == "n":
                print("\nOkay, thank you for using the chord calculator!\n")
                run_again_answer = "n"
                calculate_chord = "n"
            else:
                print("\nSorry, you need to enter a simple 'y' or 'n' to continue.  Please try again.\n")

# Run the program!
main()
