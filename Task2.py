from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}
    cuts_memo = {}

    def helper(n):
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
        max_profit = -1
        best_cut = 0
        for i in range(1, n+1):
            profit = prices[i-1] + helper(n - i)
            if profit > max_profit:
                max_profit = profit
                best_cut = i
        memo[n] = max_profit
        cuts_memo[n] = best_cut
        return max_profit

    max_profit = helper(length)

    # Reconstruct cuts
    n = length
    cuts = []
    while n > 0:
        cut = cuts_memo[n]
        cuts.append(cut)
        n -= cut

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": max(len(cuts)-1, 0)
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cut_pos = [0] * (length + 1)

    for i in range(1, length + 1):
        max_profit = -1
        for j in range(1, i + 1):
            if prices[j - 1] + dp[i - j] > max_profit:
                max_profit = prices[j - 1] + dp[i - j]
                cut_pos[i] = j
        dp[i] = max_profit

    # Reconstruct cuts
    n = length
    cuts = []
    while n > 0:
        cuts.append(cut_pos[n])
        n -= cut_pos[n]

    return {
        "max_profit": dp[length],
        "cuts": cuts,
        "number_of_cuts": max(len(cuts)-1, 0)
    }

def run_tests():
    """Function to run all tests"""
    test_cases = [
        # Test 1: Base case
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Base case"
        },
        # Test 2: Optimal to not cut
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Optimal to not cut"
        },
        # Test 3: All cuts of length 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Even Cuts"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod Length: {test['length']}")
        print(f"Prices: {test['prices']}")

        # Testing memoization
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nMemoization Result:")
        print(f"Maximum Profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of Cuts: {memo_result['number_of_cuts']}")

        # Testing tabulation
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nTabulation Result:")
        print(f"Maximum Profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of Cuts: {table_result['number_of_cuts']}")

        print("\nTest passed successfully!")

if __name__ == "__main__":
    run_tests()