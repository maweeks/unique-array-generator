# Unique Array Generator

## Problem

Given an array of strings, produce an array of unique strings with max length of `X` where the start of the string has as much of the string as possible - the end of the string is numbered.

### Examples

```py
inputX=["Name A", "Name A", "Name B", "Name C"]
# process(inputX, maxLength8)
expected=["Name A1","Name A2","Name B","Name C"]

inputX=["Name A", "Name A", "Name B", "Name C"]
# process(inputX, maxLength6)
expected=["Name 1","Name 2","Name B","Name C"]
```
