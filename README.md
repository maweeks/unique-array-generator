# Unique Array Generator

NOTE: This was a quick solve, should be tidied

## Problem

Given an array of strings, produce an array of unique strings with max length of `X` where the start of the string has as much of the string as possible - the end of the string is numbered.

### Examples

```py
inputX = ['Name A', 'Name A', 'Name B', 'Name C']
# process(inputX, maxLength8)
expected = ['Name A1','Name A2','Name B','Name C']

inputX = ['Name A', 'Name A', 'Name B', 'Name C']
# process(inputX, maxLength6)
expected = ['Name 1','Name 2','Name B','Name C']
```

## Usage

- Can run tests with `python test.py`
- Can import and use:

  ```python
  import scripty
  scripty.process(['abc', 'def'], 3)
  ```

## Solution

1. Cut the list to the max length
2. Find unique items in the array and save them in results straight away
3. If you got duplicates
   1. Generate a list of replacements with 1 digit on the end
   2. Check if enough of those replacements aren't in the results already
      1. If you have enough, return the results
      2. If you've not got enough - go deeper
         1. Generate a list of replacements with 2 digit on the end
         2. Check if enough of those replacements aren't in the results already
            1. If you have enough, return the results
            2. If you've not got enough - go deeper
               1. Generate a list of replacements with 3 digit on the end
               2. Check if enough of those replacements aren't in the results already
                  1. If you have enough, return the results
                  2. If you've not got enough - go deeper
                     1. Generate a list of replacements with 4 digit on the end
                     2. Check if enough of those replacements aren't in the results already
                        1. If you have enough, return the results
                        2. If you've not got enough - go deeper
                           1. Generate a list of replacements with 5 digit on the end
                           2. Check if enough of those replacements aren't in the results already
                              1. If you have enough, return the results
                              2. If you've not got enough - go deeper
                                 1. Generate a list of replacements with 6 digit on the end
                                 2. Check if enough of those replacements aren't in the results already
                                    1. If you have enough, return the results
                                    2. If you've not got enough - go deeper
                                       1. Generate a list of replacements with 7 digit on the end
                                       2. Check if enough of those replacements aren't in the results already
                                          1. If you have enough, return the results
                                          2. If you've not got enough - go deeper
                                             1. Generate a list of replacements with 8 digit on the end
                                             2. Check if enough of those replacements aren't in the results already
                                                1. If you have enough, return the results
                                                2. If you've not got enough - go deeper
                                                   1. Generate a list of replacements with 9 digit on the end
                                                   2. Check if enough of those replacements aren't in the results already
                                                      1. If you have enough, return the results
                                                      2. If you've not got enough - go deeper
                                                         1. If you run out of characters - cry 😭
4. Return the results 🚀
5. Party 🥳
