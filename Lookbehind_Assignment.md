# Lookbehind
- Process to check what is before the match
- Matches character(s)/group before the actual match
- There are 2 types of Lookbehind assertions:
    - Positive lookbehind
    - Negative lookbehind

## Positive lookbehind
- Regex engine searches for an element ( character, characters or a group) just before the item matched.
- If it finds that specific element before the match it declares a successful match otherwise it declares it a failure.

- /(?<=element)match/

- In this syntax, "match" represents the word to be matched, and "element" represents the item or token to be checked preceding the "match" item. The entire lookbehind expression is a grouped expression enclosed in parentheses. The structure begins with an opening parenthesis, followed immediately by a question mark, then a less than symbol and an equal sign. Following this, comes the element that must precede the actual match, followed by a closing parenthesis, and then the element to be matched.