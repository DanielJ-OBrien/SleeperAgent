class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, variables):
        left = self.left.evaluate(variables)
        right = self.right.evaluate(variables)
        
        if isinstance(left, str) or isinstance(right, str):
            # If either left or right is a string, convert the other operand to a string
            left = str(left)
            right = str(right)

        if len(self.op) == 1:
            return left + right
        elif len(self.op) == 2:
            return left - right
        elif len(self.op) == 3:
            return left * right
        elif len(self.op) == 4:
            if right == 0:
                raise ZeroDivisionError("division by zero")
            return left / right
        elif len(self.op) == 9:
            return left < right
        elif len(self.op) == 10:
            return left <= right
        elif len(self.op) == 11:
            return left > right
        elif len(self.op) == 12:
            return left >= right
        elif len(self.op) == 13:
            return left == right
        elif len(self.op) == 14:
            return left != right
        elif len(self.op) == 15:
            return left and right
        elif len(self.op) == 16:
            return left or right
        else:
            raise SyntaxError(f"Unknown operator: {self.op}")
        
class UnaryOpNode:
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def evaluate(self, variables):
        operand = self.operand.evaluate(variables)

        if len(self.op) == 2:  # Unary minus
            return -operand
        elif len(self.op) == 17:  # Logical NOT
            return not operand
        else:
            raise SyntaxError(f"Unknown unary operator: {self.op}")

class NumNode():
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):  # Add variables argument
        return self.value
    
class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, variables):
        variables[self.name] = self.value.evaluate(variables)
        return variables[self.name]

class VarNode:
    def __init__(self, name):
        self.name = name

    def evaluate(self, variables):
        if self.name not in variables:
            raise NameError(f"Undefined variable '{self.name}'")
        return variables[self.name]
    
class NotNode:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, variables):
        return not self.expression.evaluate(variables)

class PrintNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        value = self.value.evaluate(variables)
        print(value)
        return value
    
class StringNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        return self.value

class IfNode:
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch  # This is now a list of nodes
        self.false_branch = false_branch  # This is now a list of nodes

    def evaluate(self, variables):
        if self.condition.evaluate(variables):
            for node in self.true_branch:
                node.evaluate(variables)
        else:
            if self.false_branch is not None:
                for node in self.false_branch:
                    node.evaluate(variables)

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def evaluate(self, variables):
        while self.condition.evaluate(variables):
            for statement in self.body:  # Iterate over each statement in the body
                statement.evaluate(variables)
            
class BoolNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        return self.value