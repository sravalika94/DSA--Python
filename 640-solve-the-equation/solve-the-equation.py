class Solution:
    def solveEquation(self, equation):

        def evaluate(exp):
            coef = 0
            const = 0
            sign = 1
            i = 0

            while i < len(exp):
                if exp[i] == '+':
                    sign = 1
                    i += 1
                elif exp[i] == '-':
                    sign = -1
                    i += 1

                num = 0
                hasNum = False

                while i < len(exp) and exp[i].isdigit():
                    num = num * 10 + int(exp[i])
                    hasNum = True
                    i += 1

                if i < len(exp) and exp[i] == 'x':
                    coef += sign * (num if hasNum else 1)
                    i += 1
                else:
                    const += sign * num

            return coef, const

        left, right = equation.split("=")

        lcoef, lconst = evaluate(left)
        rcoef, rconst = evaluate(right)

        coef = lcoef - rcoef
        const = rconst - lconst

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"

        return "x=" + str(const // coef)