class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_rev = l1[::-1]
        l2_rev = l2[::-1]
        length_1 = len(l1)
        length_2 = len(l2)
        num_1 = []
        num_2 = []

        i_1 = 0
        for line_1 in l1_rev:
            num = line_1 * 10 ** (length_1 - 1 - i_1)
            num_1.append(num)
            i_1 += 1
        i_2 = 0
        for line_2 in l2_rev:
            num = line_2 * 10 ** (length_2 - 1 - i_2)
            num_2.append(num)
            i_2 += 1

        total_str = str(int(sum(num_1)+int(sum(num_2))))
        list_total = list(total_str)
        list_total_rev = list_total[::-1]
        for ltv in list_total_rev:
            print(ltv, end = ' ' )


solution = Solution()
solution.addTwoNumbers([2,4,3], [5,6,4])

# Testcase

# [2,4,3]
# [5,6,4]

# [0]
# [0]

# [9,9,9,9,9,9,9]
# [9,9,9,9]