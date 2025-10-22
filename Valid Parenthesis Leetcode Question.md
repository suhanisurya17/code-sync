**pre-solution brainstorming:**

\#input: a string

\#output: boolean t or f if its a valid parenthesis

\#data structure: stack and dictionary



**#key steps**

\#initialize stack

\#initialize valid pairings



**solution:**

class Solution:

&nbsp;   def isValid(self, s: str) -> bool:

&nbsp;    	stack = \[]

&nbsp;	matches = {']':'\[', '}':'{', ')':'('}

&nbsp;	



&nbsp;       for char in stack:

&nbsp;           if char not in stack or stack.pop() != matches\[char]:

&nbsp;               return False

&nbsp;           else:

&nbsp;               stack.append(char)

&nbsp;       

&nbsp;       return True



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





