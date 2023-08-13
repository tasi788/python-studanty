from stackClass import *
operand = {'A':2, 'B':5, 'C':4, 'D':6, 'E':3}
operator = {'+','-','*','/'}
def evaluate(optr, op1, op2):
  if optr == '+': 	
    value = op1 + op2
  elif optr == '-':	  
    value = op1 - op2
  elif optr == '*':	
    value = op1 * op2
  elif optr == '/':	
    value = op1 / op2
  return value
def post_evaluate(postfix):
  myStack = Stack()
  for token in postfix:
    if token in operand:	#此句元為運算元，適用規則2
      myStack.push(operand[token])
    elif token in operator:	#此句元為運算子，適用規則3
      op2 = myStack.pop()
      op1 = myStack.pop()
      result = evaluate(token,op1,op2)
      myStack.push(result)
  result = myStack.pop()  #規則4
  return result

in_post = input()
print(post_evaluate(in_post))