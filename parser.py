
TT_EOF = "EOF"
TT_INT = "INT"
TT_ADD = "ADD"

class Lexer:
    def __init__(self, string):
        self.string = string
        self.curr = None
    def next(self):
        self.curr, self.string = self.lex()
        return self.curr
    def peek(self):
        return self.lex()[0]
    def lex(self):
        copy = self.string
        if not copy:
            return [TT_EOF], ""
        if copy[0] in "\n \t":
            while self.string and self.string[0] in "\n \t":
                self.string = self.string[1:]
            copy = self.string
        elif copy[0] in "0123456789":
            res = ""
            while copy and copy[0] in "0123456789":
                res += copy[0]
                copy = copy[1:]
            token = [TT_INT, int(res)]
        elif copy[0] == "+":
            token = [TT_ADD]
            copy = copy[1:]
        return token, copy



l = Lexer("1 + 2 + 34")
print(l.next())
while l.curr[0] != TT_EOF:
    print(l.next())