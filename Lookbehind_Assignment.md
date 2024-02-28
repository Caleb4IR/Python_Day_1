# Lookbehind
- Process to check what is before the match
- Matches character(s)/group before the actual match
- There are 2 types of Lookbehind assertions:
    - Positive lookbehind
    - Negative lookbehind

## Positive lookbehind
- Regex engine searches for an element ( character, characters or a group) just before the item matched.
- If it finds that specific element before the match it declares a successful match otherwise it declares it a failure.

```
/(?<=element)match/
```

- In this syntax, "match" represents the word to be matched, and "element" represents the item or token to be checked preceding the "match" item. The entire lookbehind expression is a grouped expression enclosed in parentheses. The structure begins with an opening parenthesis, followed immediately by a question mark, then a less than symbol and an equal sign. Following this, comes the element that must precede the actual match, followed by a closing parenthesis, and then the element to be matched.

## Negative lookbehind
- In the regex engine, it initially locates a match for an item and then retraces its steps to attempt matching a specified item that immediately precedes the main match. If the traceback results in a successful match, the overall match fails; otherwise, it succeeds.

```
/ (?<!element)match /
```
- In this context, "match" refers to the item being matched, while "element" refers to the character, characters, or group in the regular expression that should not precede the match in order for it to be considered successful. Therefore, if you wish to prevent matching a token when a specific token precedes it, you can employ negative lookbehind.
