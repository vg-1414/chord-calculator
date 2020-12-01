
def print_welcome_message():
    """Prints the initial welcoming message."""
    print(
        '''
        Chord calculator
        ----------------
        Welcome to the chord calculator!  Use this program to find the note names
        and/or their frequencies for any chord you like.

        To begin, please select a root note.
        '''
    )

def print_note_names():
    """Displays a menu of the 12 chromatic note names."""
    print(
        '''
        Available note names
        --------------------
         1: A
         2: A#/Bb
         3: B
         4: C
         5: C#/Db
         6: D
         7: D#/Eb
         8: E
         9: F
        10: F#/Gb
        11: G
        12: G#/Ab
        '''
    )

def print_chord_types():
    """Displays a menu of the available chord types"""
    print(
        '''
        Three-tone chords (triads)
        --------------------------
         1. Major
         2. Minor
         3. Diminished
         4. Augmented
         5. Suspended second
         6. Suspended fourth

        Four-tone chords (sevenths)
        ---------------------------
         7. Major seventh
         8. Major sixth
         9. Minor seventh
        10. Minor sixth
        11. Dominant seventh
        12. Minor seventh flat five
        13. Minor/major seventh
        '''
        )

def print_chord_alterations():
    """Displays a menu of available chord alterations."""
    print(
        '''
        Chord alterations
        -----------------
        1. Raised fifth
        2. Flattened fifth
        3. Raised ninth
        4. Flattened ninth
        '''
    )

def print_chord_extensions():
    """Displays a menu of available chord extensions."""
    print(
        '''
        Chord extensions
        ----------------
        1. Ninth
        2. Eleventh
        3. Thirteenth
        '''
    )

def assign_root_note(root_note):
    """Assigns the selected note to the proper string value."""
    # This is inefficient and ugly, but hey I gotta start somewhere.
    # These numbers correspond directly to the print_note_names() output.
    if root_note == 1:
        root_note = "A"
    elif root_note == 2:
        root_note = "A#/Bb"
    elif root_note == 3:
        root_note = "B"
    elif root_note == 4:
        root_note = "C"
    elif root_note == 5:
        root_note = "C#/Db"
    elif root_note == 6:
        root_note = "D"
    elif root_note == 7:
        root_note = "D#/Eb"
    elif root_note == 8:
        root_note = "E"
    elif root_note == 9:
        root_note = "F"
    elif root_note == 10:
        root_note = "F#/Gb"
    elif root_note == 11:
        root_note = "G"
    elif root_note == 12:
        root_note = "G#/Ab"
    else:
        print("\nI'm not sure how you got this far, but that's not a valid option.\n")

    return root_note

def assign_chord_type(chord_type):
    """Assigns the selected chord type to the proper string value."""
    # Again, yuck, but it's all I can think of for now.
    # These numbers correspond directly to the print_chord_types() output.
    if chord_type == 1:
        chord_type = "Major triad"
    elif chord_type == 2:
        chord_type = "Minor triad"
    elif chord_type == 3:
        chord_type = "Diminished"
    elif chord_type == 4:
        chord_type = "Augmented"
    elif chord_type == 5:
        chord_type = "Suspended second"
    elif chord_type == 6:
        chord_type = "Suspended fourth"
    elif chord_type == 7:
        chord_type = "Major seventh"
    elif chord_type == 8:
        chord_type = "Major sixth"
    elif chord_type == 9:
        chord_type = "Minor seventh"
    elif chord_type == 10:
        chord_type = "Minor sixth"
    elif chord_type == 11:
        chord_type = "Dominant seventh"
    elif chord_type == 12:
        chord_type = "Minor seventh flat five"
    elif chord_type == 13:
        chord_type = "Minor/major seventh"
    else:
        print("\nI'm not sure how you got this far, but that's not a valid option.\n")

    return chord_type

def assign_alteration(alteration):
    """Assigns the selected alteration to the proper string value."""
    if alteration == 1:
        alteration = "Raised fifth"
    elif alteration == 2:
        alteration = "Flattened fifth"
    elif alteration == 3:
        alteration = "Raised ninth"
    elif alteration == 4:
        alteration = "Flattened ninth"
    else:
        print("\nI'm not sure how you got this far, but that's not a valid option.\n")

    return alteration

def assign_extension(extension):
    """Assigns the selected extension to the proper string value."""
    if extension == 1:
        extension = "Ninth"
    elif extension == 2:
        extension = "Eleventh"
    elif extension == 3:
        extension = "Thirteenth"
    else:
        print("\nI'm not sure how you got this far, but that's not a valid option.\n")

    return extension

def pick_root_note():
    """Stores the specified root note."""

    import calcmod

    # Prompt the user to make a selection, and verify its validity.
    while True:
        try:
            # First, make sure the provided value is an integer.
            root_note = int(input("Enter the number of the note you would like to use: "))

            # If that is fine, make sure it is in the correct range.
            while root_note not in range(1, 13):
                print("\nSorry, that's not a number in the available range.  Please try again.\n")
                root_note = int(input("Enter the number of the note you would like to use: "))

            # Huzzah, a legit value has been provided!  Assign the variable, let the user know, and break out.
            root_note = calcmod.assign_root_note(root_note)
            print("\nGreat, we will use", root_note, "as the root note.\n")
            break

        # If the user provided a string or float, make them start over.
        except ValueError:
            print("\nSorry, you need to enter a number with no decimals and no letters.  Please try again.\n")

    return root_note

def pick_chord_type():
    """Stores the specified chord type."""

    import calcmod

    while True:
        try:
            # Verify we have an integer...
            chord_type = int(input("Enter the number of the chord type you would like to use: "))

            # If so, verify it's in the correct range...
            while chord_type not in range(1, 14):
                print("\nSorry, that's not a number in the available range.  Please try again.\n")
                chord_type = int(input("Enter the number of the chord type you would like to use: "))

            # Great, now we have what we need!  Update the variable, let the user know, and break the loop.
            chord_type = calcmod.assign_chord_type(chord_type)
            print("\nOkay, we will use", chord_type.lower(), "as the chord type.\n")
            break

        # If the user specified a non-integer, make them start over.
        except ValueError:
            print("\nSorry, you need to enter a number with no decimals and no letters.  Please try again.\n")

    return chord_type

# Function: update dominant chord tones.
# Input: none.
# Output: updated intervals for the dominant chord.
def update_dominant_chord():

    import calcmod

    print("You selected the ever-alterable dominant seventh!")

    # Prompt if the user would like to alter the usual jazzy intervals.
    while True:
        try:
            # Prompt for chord alterations.
            altered_note_answer = str(input("\nWould you like to alter the fifth or add an altered ninth?  Enter 'y' or 'n': "))

            # Confirm altered note selection and break out.
            if altered_note_answer == "y":
                print("\nGreat, before we add that alteration let's check on extensions.")
                break

            # Move forward if there's no interest in altering.
            elif altered_note_answer == "n":
                print("\nOkay, moving on.\n")
                break

            # If the user enters a string that isn't 'y' or 'n' ask them to try again.
            else:
                print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")

        # If the user enters an int or float at any point, make them start over.
        except ValueError:
            print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")

    # Prompt if the user would like to add chord extensions.
    while True:
        try:
            # Prompt for chord extensions.
            extend_chord_answer = str(input("\nWould you like to add any extended notes to your chord?  Enter 'y' or 'n': "))

            # Confirm chord extension answer and break out.
            if extend_chord_answer == "y":
                print("\nOkay, let's start updating the chord tones!")
                break

            # Move forward if there's no interest in altering.
            elif extend_chord_answer == "n":
                print("\nOkay, moving on.\n")
                break

            # Invalid input gets looped back to the start.
            else:
                print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")

        # If the user enters an int or float at any point, make them start over.
        except ValueError:
            print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")

    # Present the list of available dominant chord alterations if the user
    # specified they want to jazz it up.
    if altered_note_answer == 'y':
        calcmod.print_chord_alterations()

        # Collect their answer and validate the input.
        while True:
            try:
                # Verify the answer is an integer
                alteration = int(input("Enter the number of the chord alteration you would like to make: "))

                # Now verify that integer is in range
                while alteration not in range(1, 5):
                    print("\nSorry, that's not a number in the available range.  Please try again.\n")
                    alteration = int(input("Enter the number of the chord alteration you would like to make: "))

                # Okay, assign that alteration and break out of the loop.
                alteration = calcmod.assign_alteration(alteration)
                print("\nAdding a", alteration.lower(), "as a chord alteration.")
                break

            # If the user specified a non-integer, make them start over.
            except ValueError:
                print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")
    else:
        alteration = ""

    # Present the list of available dominant chord extensions if the user
    # specified they want to extend the chord.
    if extend_chord_answer == 'y':
        calcmod.print_chord_extensions()

        # Collect their answer and validate the input.
        while True:
            try:
                # Verify the answer is an integer
                extension = int(input("Enter the number of the chord extension you would like to add: "))

                # Now verify that integer is in range
                while extension not in range(1, 4):
                    print("\nSorry, that's not a number in the available range.  Please try again.\n")
                    extension = int(input("Enter the number of the chord extension you would like to add: "))

                # Okay, assign that extension and break out of the loop.
                extension = calcmod.assign_extension(extension)
                print("\nAdding a", extension.lower(), "as a chord extension.\n")
                break

            # If the user specified a non-integer, make them start over.
            except ValueError:
                print("\nSorry, you need to enter a simple 'y' or 'n' to move forward.  Please try again.\n")
    else:
        extension = ""

    return alteration, extension

# Function: sort a list to generate a scale.
# Input: user selected root note value.
# Output: a properly sorted list that reflects a chromatic scale.
def sort_chromatic_scale(root_note):

    # Use the 'A' chromatic scale as a starting point.
    chromatic_scale = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    # Assign our root to the first letter available in the list
    root = 'A'

    # While the static assignment doesn't match the user's input, rearrange the list.
    while root != root_note:
        # Pop the incorrect root out of the list
        popped = chromatic_scale.pop(0)
        # Append it to the end of the list
        chromatic_scale.append(popped)
        # Update the root value with the new first value in the list
        root = chromatic_scale[0]       

    # Return the chromatic scale
    return chromatic_scale

# Function: calculate the correct notes from a chromatic scale.
# Input: a chromatic scale and a chord type.
# Output: a list containing the notes that the user requested.
def extract_chord_tones(chromatic_scale, chord_type, dominant_updates = ""):

    # Cheat sheet for the chromatic chord
    # tones and their element positions.
    #  0 = root
    #  1 = minor second / flat ninth
    #  2 = major second / ninth
    #  3 = minor third / raised ninth
    #  4 = major third
    #  5 = perfect fourth / eleventh
    #  6 = raised fourth / tritone / diminished fifth
    #  7 = perfect fifth
    #  8 = minor sixth / raised fifth
    #  9 = major sixth / thirteenth
    # 10 = minor seventh
    # 11 = major seventh

    # Triad formulas
    major_triad_formula = [0, 4, 7]       # Root, major third, perfect fifth
    minor_triad_formula = [0, 3, 7]       # Root, minor third, perfect fifth
    diminished_triad_formula = [0, 3, 6]  # Root, minor third, diminished fifth
    augmented_triad_formula = [0, 4, 8]   # Root, major third, augmented fifth
    suspended_fourth_formula = [0, 5, 7]  # Root, perfect fourth, perfect fifth
    suspended_second_formula = [0, 2, 7]  # Root, major second, perfect fifth

    # Seventh chord formulas: the names.
    major_seventh_formula = [0, 4, 7, 11]           # Root, major third, perfect fifth, major seventh
    major_sixth_formula = [0, 4, 7, 9]              # Root, major third, perfect fifth, major sixth
    minor_seventh_formula = [0, 3, 7, 10]           # Root, minor third, perfect fifth, minor seventh
    minor_sixth_formula = [0, 3, 7, 8]              # Root, minor third, perfect fifth, minor sixth
    dominant_seventh_formula = [0, 4, 7, 10]        # Root, major third, perfect fifth, minor seventh
    minor_seventh_flat_five_formula = [0, 3, 6, 10] # Root, minor third, diminished fifth, minor seventh
    minor_major_seventh_formula = [0, 3, 7, 11]     # Root, minor third, perfect fifth, major seventh

    # Take the selected chord type and insert underscores to match the formula lists.
    chord_type_formatted = chord_type.replace(" ", "_")
    chord_type_formatted = chord_type_formatted.replace("/", "_")
    chord_type_formatted = chord_type_formatted.lower()

    # There has got to be a better way.  This is hideous.
    if chord_type_formatted == "major_triad":
        formula = major_triad_formula
    elif chord_type_formatted == "minor_triad":
        formula = minor_triad_formula
    elif chord_type_formatted == "diminished":
        formula = diminished_triad_formula
    elif chord_type_formatted == "augmented":
        formula = augmented_triad_formula
    elif chord_type_formatted == "suspended_second":
        formula = suspended_second_formula
    elif chord_type_formatted == "suspended_fourth":
        formula = suspended_fourth_formula
    elif chord_type_formatted == "major_seventh":
        formula = major_seventh_formula
    elif chord_type_formatted == "major_sixth":
        formula = major_sixth_formula
    elif chord_type_formatted == "minor_seventh":
        formula = minor_seventh_formula
    elif chord_type_formatted == "minor_sixth":
        formula = minor_sixth_formula
    elif chord_type_formatted == "dominant_seventh":
        formula = dominant_seventh_formula
    elif chord_type_formatted == "minor_seventh_flat_five":
        formula = minor_seventh_flat_five_formula
    elif chord_type_formatted == "minor_major_seventh":
        formula = minor_major_seventh_formula
    else:
        print("I'm not sure how you got this far, but that is an invalid option.")

    # Initialize an empty list to hold the notes as we find them.
    chord_tones = []

    # For each tone in the chord, append its value from the chromatic scale to our tones list.
    for tones in formula:
        chord_tones.append(chromatic_scale[tones])

    # If a dominant update exists...
    if len(dominant_updates) >= 1:

        # ...add any alterations to the list.
        if dominant_updates[0] != "":
            alteration = dominant_updates[0]
            if alteration == "Raised fifth":
                # Remove the existing fifth, which should be the third element
                chord_tones.pop(2) 
                alteration = 8
            elif alteration == "Flattened fifth":
                # Remove the existing fifth, which should be the third element
                chord_tones.pop(2) 
                alteration = 6
            elif alteration == "Raised ninth":
                alteration = 3
            elif alteration == "Flattened ninth":
                alteration = 1
            else:
                print("Well, something weird happened and your alteration was not added.")

            chord_tones.append(chromatic_scale[alteration])

        # ...add any extensions to the list.
        if dominant_updates[1] != "":
            extension = dominant_updates[1]
            if extension == "Ninth":
                extension = 2
            elif extension == "Eleventh":
                extension = 5
            elif extension == "Thirteenth":
                extension = 9
            else:
                print("Well, something unusual happened and your extension was not added.")

            chord_tones.append(chromatic_scale[extension])

    return chord_tones

# Create a list of the Hertz values for the first octave range.
C1 = 32.7032

# Initialize an empty list to contain the first octave's Hertz values.
octave1_static = []

# Use a while loop to determine the frequencies.
# There are twelve tones to account for.
x = 0
while x < 13:
    # Calculate the current frequency's value.
    current_frequency = C1 * 2**(x/12)

    # Add it to the octave1 list.
    octave1_static.append(current_frequency)

    x = x + 1

# Function: calculate all requested frequencies.
# Input: the user's specified chord tones.
# Output: a collection of lists that contain each note's frequency values from octave ranges 1 through 7.
def calculate_frequencies(chord_tones):

    # Use a C chromatic scale to line up our notes with the octave1_static list.
    c_chromatic_scale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

    # Create an empty master list to contain lists for each note's frequency values
    chord_frequencies = []

    # Iterate through the individual notes, and store their frequency values in the master list.
    for note in chord_tones:
        index = c_chromatic_scale.index(note)       # Grab the index of our current note
        frequency = octave1_static[index]           # Use that index to grab the frequency of note1
        note_frequencies = []                       # Create an empty list to start storing frequency values
        x = 1
        while x < 65:                               # To get the 7th octave frequency, you need to multiply by 64
            note_frequencies.append(x * frequency)
            x = x * 2                               # Multiply by 1, 2, 4, 8, 16, 32, and 64

        chord_frequencies.append(note_frequencies)

    return chord_frequencies

# Function: determine if user wants to calculate frequencies.
# Input: the chord_tones list.
# Output: frequencies (or "nah") stored in chord_frequencies
def include_frequencies(chord_tones):

    import calcmod

    # Set the frequency answer to an empty string and then prompt the user to make a decision.
    frequency_answer = ""
    while len(frequency_answer) < 1:
        answer = input("Would you like to also calculate the frequencies for each note in the chord?  Enter 'y' or 'n': ")
        if answer == 'y':
            chord_frequencies = calcmod.calculate_frequencies(chord_tones)
            frequency_answer = "y"
        elif answer == 'n':
            print("\nOkay, moving on.\n")
            chord_frequencies = "nah"
            frequency_answer = "n"
        else:
            print("\nSorry, you need to enter a simple 'y' or 'n' to continue.  Please try again.\n")

    return chord_frequencies

# Function: display the results on the screen.
# Input: all user input and program calculations.
# Output: a pretty display of notes, and possibly their frequencies, stored in final_results.
def print_results(root_note, chromatic_scale, chord_type, chord_tones, chord_frequencies, dominant_updates = ""):

    # Format the chromatic_scale list as a space-separated string.
    chromatic_scale_string = ' '.join(chromatic_scale)

    # Begin creating the final_results string.
    final_results = (
        "\nOf these available notes in the %s chromatic scale:\n\n"
        "%s\n\nThe %s %s chord"
        % (root_note, chromatic_scale_string, root_note, chord_type.lower()))

    # If the chord is a modified dominant seventh...
    if len(dominant_updates) > 1:
        final_results = final_results + ", with your specified modifications, contains the following notes:\n"
    else:
        final_results = final_results + " contains only the following notes:\n"

    # Now print each note on its own line
    for note in chord_tones:
        index = chord_tones.index(note)
        final_results = final_results + "\n   ~ " + note + " ~\n\n"

        # If the user wants frequency values, provide them now.
        if chord_frequencies != "nah":
            final_results = final_results + "   " + note + "'s frequencies in octaves 1 through 7 are:\n\n" 
            for octave in chord_frequencies[index]:
                final_results = final_results + "      " + "{0:0.2f}".format(octave) + "Hz\n"

    # Return the results in case the user wants to save them to file.
    return final_results

# Function: export the results to a text file.
# Input: the final_results string from print_results()
# Output: the chord-results.txt file.
def export_results(final_results):

    # Use a loop to make sure we get valid input.
    export_answer = ""
    while len(export_answer) < 1:
        answer = input("Would you like to export these results to a text file?  Please enter 'y' or 'n': ")
        if answer == "y":
            # Create chord-results.txt if it isn't there, but append to it if it is...
            results_file = open("chord-results.txt", "a")
            # Dump the results into the file.
            results_file.write(final_results)
            # Close the file out.
            results_file.close()
            # Let the user know and satisfy the condition.
            print("\nGreat, your results are stored in chord-results.txt and this chord is now complete.\n")
            export_answer = "y"
        elif answer == "n":
            print("\nOkay, this chord is now complete.\n")
            export_answer = "n"
        else:
            print("\nSorry, you need to enter a simple 'y' or 'n' to continue.  Please try again.")
