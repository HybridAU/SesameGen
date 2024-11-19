#!/usr/bin/python3
"""
SesameGen is simple password generator that uses the Python Secrets module
to generate passwords. With a tkinter GUI it only uses the standard python
libraries and doesn't need anything extra installed to run.

Licence: MIT
Author: Michael Van Delft
Date: 2019-03-13
"""

import math
import secrets
import tkinter

LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

SPECIAL_CHARACTERS = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                      '+', ':', "'", '"', '<', '>', '.', '/', '|', '[', ']', ';']

# Characters like 'C', K' and 'S' are not a really ambiguous, but I can't always tell
# they are upper or lower case, so out they go.
AMBIGUOUS_CHARACTERS = ['8', 'B', 'c', 'C', 'g', '9', 'I', 'L', '1', 'l', '|', '0',
                        'o', 'O', 'k', 'K', 's', 'S', 'u', 'U', 'v', 'V', ';', ':',
                        "'", '"']


def generate_password(character_set, length):
    """
    Uses the secretes module to pick a given number of characters
    from the available character set. https://docs.python.org/3/library/secrets.html
    """
    # "complexity is the worst enemy of security" - Bruce Schneier.
    return ''.join(secrets.choice(character_set) for _character in range(length))


def calculate_entropy(character_set, length):
    """
    Calculates the bits of entropy used to generate the password.
    """
    return round(math.log2(len(character_set)**length), 1)


class Window(tkinter.Frame):

    def __init__(self):
        """
        Loads a pretty baisc tkinter form adds all of the controls and generates a password.
        """
        self.master = tkinter.Tk()
        self.master.title("SesameGen")

        # Create all the controls
        self.password_label = tkinter.Label(self.master, text="Password")
        self.password_entry = tkinter.Entry(self.master)
        self.generate_button = tkinter.Button(self.master, text="Generate", command=self.update_window)

        self.password_length_label = tkinter.Label(self.master, text="Length")
        self.password_length_scale = tkinter.Scale(self.master,
                                                   from_=0,
                                                   to=64,
                                                   showvalue=0,
                                                   orient=tkinter.HORIZONTAL,
                                                   command=self.update_window)
        self.character_count_label = tkinter.Label(self.master)
        self.entropy_label = tkinter.Label(self.master)

        # This seems like madness to me, why do I need to create a whole separate object just to
        # store the state of each check button!? Why can't I just read their state directly from
        # the button as and when I need to?
        self.lower_case_checkbutton_value = tkinter.IntVar()
        self.upper_case_checkbutton_value = tkinter.IntVar()
        self.numbers_checkbutton_value = tkinter.IntVar()
        self.special_characters_checkbutton_value = tkinter.IntVar()
        self.remove_ambiguous_checkbutton_value = tkinter.IntVar()

        self.lower_case_checkbutton = tkinter.Checkbutton(self.master,
                                                          text="Lower case",
                                                          variable=self.lower_case_checkbutton_value,
                                                          command=self.update_window)
        self.upper_case_checkbutton = tkinter.Checkbutton(self.master,
                                                          text="Upper case",
                                                          variable=self.upper_case_checkbutton_value,
                                                          command=self.update_window)
        self.numbers_checkbutton = tkinter.Checkbutton(self.master,
                                                       text="Numbers",
                                                       variable=self.numbers_checkbutton_value,
                                                       command=self.update_window)
        self.special_characters_checkbutton = tkinter.Checkbutton(self.master,
                                                                  text="Special",
                                                                  variable=self.special_characters_checkbutton_value,
                                                                  command=self.update_window)
        self.remove_ambiguous_checkbutton = tkinter.Checkbutton(self.master,
                                                                text="Remove ambiguous characters",
                                                                variable=self.remove_ambiguous_checkbutton_value,
                                                                command=self.update_window)

        # Set the layout of the controls on the window.
        self.password_label.grid(row=0, column=0, sticky=tkinter.W)
        self.password_entry.grid(row=0, column=1, columnspan=5, sticky=tkinter.W + tkinter.E)
        self.generate_button.grid(row=0, column=6, sticky=tkinter.E)

        self.password_length_label.grid(row=1, column=0, sticky=tkinter.W)
        self.password_length_scale.grid(row=1, column=1, columnspan=4, sticky=tkinter.W + tkinter.E)
        self.character_count_label.grid(row=1, column=5, sticky=tkinter.W)
        self.entropy_label.grid(row=1, column=6)

        self.lower_case_checkbutton.grid(row=2, column=1)
        self.upper_case_checkbutton.grid(row=2, column=2)
        self.numbers_checkbutton.grid(row=2, column=3)
        self.special_characters_checkbutton.grid(row=2, column=4)
        self.remove_ambiguous_checkbutton.grid(row=2, column=5)

        # set the
        self.lower_case_checkbutton.select()
        self.upper_case_checkbutton.select()
        self.numbers_checkbutton.select()
        self.special_characters_checkbutton.deselect()
        self.remove_ambiguous_checkbutton.select()
        self.password_length_scale.set(16)

        # Run once after loading, then called every time something changes.
        self.update_window(None)

    def update_window(self, _length=None):
        """
        Reads the values of all of the widgets and then generates a password
        based on the currently settings selected.
        """
        # The reason it takes a _length parameter is that when it's called by
        # the Scale widget, it passes the current value of the widget, the
        # problem is that it can also be called by the generate button or
        # one of the check buttons changing so we can't rely on the length
        # always being passed, instead we can just set it again regardless.
        _length = self.password_length_scale.get()

        character_set = []

        if self.lower_case_checkbutton_value.get():
            character_set += LOWER_CASE
        if self.upper_case_checkbutton_value.get():
            character_set += UPPER_CASE
        if self.numbers_checkbutton_value.get():
            character_set += NUMBERS
        if self.special_characters_checkbutton_value.get():
            character_set += SPECIAL_CHARACTERS
        if self.remove_ambiguous_checkbutton_value.get():
            for char in AMBIGUOUS_CHARACTERS:
                if char in character_set:
                    character_set.remove(char)

        self.password_entry.delete(0, tkinter.END)
        self.character_count_label["text"] = str(_length) + " Characters"
        if character_set:
            self.password_entry.insert(0, generate_password(character_set, _length))
            self.entropy_label["text"] = str(calculate_entropy(character_set, _length)) + " bits"
        else:  # If there are no characters in the list we can't generate a password or calculate entropy.
            self.entropy_label["text"] = "0 bits"


Window()
tkinter.mainloop()
