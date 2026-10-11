from pyscript import document, display

members = ["Hope Benitez", "Jacob Minguillo", "Maya Peters", "Anna Kone"]

def check(e):  # we put e for the event handler
    # Getting the string values from input fields and combining into full name
    # Added .title() so names match even if typed in lowercase (ex. "hope benitez")
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()
    name = (first + " " + last).title()

    # Testing if value is present in list using 'in' keyword (returns Boolean: True or False)
    in_club = name in members

    # 5. Creating a list of possible output messages
    # Message at offset 0 = False (not in list)
    # Message at offset 1 = True (in list)
   
    response = [
        "Sorry " + name + ", your name is not on the list.",
        "Congratulations " + name + "! You're in CommArts."
    ]

    # Boolean value as the list offset (False = 0, True = 1)
    final_output = response[in_club]

    # Displaying the result
    display(final_output, target="result", append=False)


