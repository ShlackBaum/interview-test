stack_list = "[[{())}]"

class Stack:
    def __init__(self, stack_list):
        self.stack_string = stack_list
        self.stack_list = []
        self.stack_list[:0] = stack_list

    def isEmpty(self):
        if not self.stack_list:
            return False
        else:
            return True

    def push(self, element_to_add_on_top):
        self.stack_list.append(element_to_add_on_top)

    def poper(self):
        self.stack_list.pop()
        top_element_after=self.stack_list[-1]
        return top_element_after

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def pairing(self, elem):
        if elem == "{":
            pair = "}"
        if elem == "}":
            pair = "{"
        if elem == "[":
            pair = "]"
        if elem == "]":
            pair = "["
        if elem == "(":
            pair = ")"
        if elem == ")":
            pair = "("
        return pair

    def balance(self):
        if self.size() % 2 != 0:
            return "Несбалансированно"
        else:
            self.new_list = []
            self.new_list.append(self.peek())
            counter = 0
            limit = self.size()
            while counter < limit:
                if len(self.new_list) >= 2 and self.new_list[-1] == self.pairing(self.new_list[-2]):

                    self.new_list.pop(-1)
                    self.new_list.pop(-1)
                if self.size() > 1:
                    self.new_list.append(self.poper())
                counter +=1
            if not self.new_list:
                return "Сбалансировано"
            else:
                return "Несбалансировано"

if __name__ == '__main__':
    test_list = Stack(stack_list)
    print(test_list.balance())


