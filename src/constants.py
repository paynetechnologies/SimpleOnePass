''' constants '''

class constants:

    """ Global file declarations """

E = {
    "null-character":
        "Null character in input stream, replaced with U+FFFD.",
    "invalid-codepoint":
        "Invalid codepoint in stream.",
}

tokenTypes = {
    "Doctype": 0,
    "Characters": 1,
    "SpaceCharacters": 2,
    "StartTag": 3,
    "EndTag": 4,
    "EmptyTag": 5,
    "Comment": 6,
    "ParseError": 7
}