#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#

SPECIAL_CHARS_MAPPING = {
    "I": "_I",
    "1": "_1",
    "2": "_2",
    "3": "_3",
    "4": "_4",
    "5": "_5",
    "6": "_6",
    "7": "_7",
    "8": "_8",
    "9": "_9",
    "0": "_0",
    " ": "space",
    ".": "dot",
    "-": "dash",
    ",": "comma",
    ";": "semicolon",
    ":": "colon",
    "'": "apostrophe",
    "\"": "quotation",
    "+": "plus",
    "=": "equals",
    "(": "paren_left",
    ")": "paren_right",
    "*": "asterisk",
    "&": "ampersand",
    "^": "caret",
    "%": "percent",
    "$": "$",
    "#": "pound",
    "@": "at",
    "!": "exclamation",
    "?": "question_mark",
    "\\": "back_slash",
    "/": "forward_slash",
    "{": "curly_left",
    "}": "curly_right",
    "[": "bracket_left",
    "]": "bracket_right",
    "|": "bar",
    "<": "less_than",
    ">": "greater_than",
    "_": "underscore"
}


def obfuscate(user_input):
    user_output = ''
    for c in user_input:
        char = c
        if c in SPECIAL_CHARS_MAPPING:
            char = SPECIAL_CHARS_MAPPING[c]
        user_output += char + "."
    return user_output[0:-1]


def main():
    while True:
        print "Input:",
        user_input = raw_input()
        user_output = obfuscate(user_input)
        print "[NSMutableString string].%s" % user_output


if __name__ == '__main__':
    main()
