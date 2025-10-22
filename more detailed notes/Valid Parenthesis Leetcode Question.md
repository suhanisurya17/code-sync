# 🧩 Valid Parentheses — Problem Breakdown & Tracing

## 📌 Problem Statement

- **Input:** A string `s` containing only the characters `'(', ')', '{', '}', '[' and ']'`
- **Output:** Return `True` if the input string is valid, otherwise `False`

## ✅ Validity Rules

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

---

## 🧠 Pre-Solution Brainstorming

### 🔧 Data Structures
- **Stack**: to track unmatched opening brackets
- **Dictionary**: to map closing brackets to their corresponding opening brackets

### 🗝️ Key Steps
1. Initialize an empty stack
2. Define valid bracket pairings using a dictionary
3. Iterate through each character in the string:
   - If it's an opening bracket, push to stack
   - If it's a closing bracket:
     - Check if stack is empty or top of stack doesn't match → return `False`
     - Otherwise, pop from stack
4. After iteration, return `True` if stack is empty

---

## 🧪 Code Implementation

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matches:
                if not stack or stack.pop() != matches[char]:
                    return False
            else:
                stack.append(char)

        return not stack



**#using example s = '()'**
if char in matches = **false** since its an opening bracket
moves to else
stack =\['(']

**second round of loop**
evaluating ')'
if char in matches = **true** since its a closing bracket
if char not in stack = **true** so it is returning false here - bug

**how to fix the second if statement**
checking if the stack was previously empty or if the previous value in the stack is not an opening

**rewriting that statement**
if not stack = **false**  because we had '(' in the stack already
so moves onto second part of conditional which is stack.pop() != matches\[char]

**final new statement:**
if not stack or stack.pop() != matches\[char]:
which it matches since ')':'('
so it pops '(' from the stack
now we have empty stack = \[]
return not stack #returning if stack is empty or not

**#using example s= '(){}\[]'**
**first round of loop**
**evaluating '('**
if char in matches = false since its an opening bracket
else -> appends to stack
stack = \['(']

**second round of loop**
**evaluating ')'**
if char in matches = true since its an opening bracket
if not stack or stack.pop != matches\[char]
1\.	false
2\.	false
stack is empty now bc of push
**stack = \[ ]**

**moves to next set and repeats**

**#using example '({})'**
**first loop iteration -> evaluating '('**
since it is an opening bracket, it gets appended to the stack
stack = \['(']

**second loop iteration -> evaluating '{'**
since it is also an opening bracket, it gets appended to the stack
stack = \['(', '{']

**third loop iteration -> evaluating '}'**
since it is a closing bracket, moves onto second conditional
since stack is not empty, moves onto evaluating the match
since both statements return **false**, a pop action occurs
stack = \['(']

**fourth loop iteration -> evaluating ')'**
since it is a closing bracket, moves onto second conditional
since stack is not empty, moves onto evaluating the match
since both statements return **false**, a pop action occurs
stack = \[ ]

so since stack is empty at the end, return true so it is a valid parenthesis






