# goit-neo-algo2-hw-02

## Task 1. Optimising the 3D Printer Queue in the University Lab

Develop a program to optimise a 3D printing task queue, considering the priorities and technical limitations of the printer, using a greedy algorithm.

Task Description

Use input data in the form of a list of print jobs, where each job contains: ID, model volume, priority, and printing time.
Implement the main function optimize_printing, which should:
Take into account the priorities of the tasks.
Group models for simultaneous printing.
Check volume and quantity constraints.
Calculate the total printing time.
Return the optimal printing order.
Output the optimal printing order and the total time required to complete all tasks.


Technical Requirements

Expected output format for the optimize_printing function:

{
    "print_order": ["M1", "M2", "M3"],  # order of print jobs
    "total_time": 360  # total time in minutes
}



2. Input data format for the jobs:

print_jobs = [
    {
        "id": str,  # unique identifier
        "volume": float,  # volume in cm³ (> 0)
        "priority": int,  # priority (1, 2 or 3)
        "print_time": int  # printing time in minutes (> 0)
    }
]


3. Printer constraints format:

printer_constraints = {
    "max_volume": float,  # maximum volume for printing
    "max_items": int  # maximum number of models
}

4. Task priorities:

1 (highest) — Coursework/Theses
2 — Lab Work
3 (lowest) — Personal Projects

Program Template


from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimises the 3D printing queue according to priorities and printer constraints

    Args:
        print_jobs: List of print jobs
        constraints: Printer constraints

    Returns:
        Dict with the print order and total time
    """
    # Your code should go here

    return {
        "print_order": None,
        "total_time": None
    }

# Testing
def test_printing_optimization():
    # Test 1: Models with the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Models with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # lab work
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # thesis
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # personal project
    ]

    # Тест 3: Exceeding volume constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\\nTest 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()


Expected result:

Test 1 (same priority): 
Print order: ['M1', 'M2', 'M3'] 
Total time: 270 minutes 

Test 2 (different priorities): 
Print order: ['M2', 'M1', 'M3'] 
Total time: 270 minutes 

Test 3 (exceeding constraints): 
Print order: ['M1', 'M2', 'M3'] 
Total time: 450 minutes 



## Task 2. Optimal Rod Cutting for Maximum Profit (Rod Cutting Problem)

Develop a program to find the optimal way to cut a rod in order to achieve the maximum profit. You need to implement two approaches: using recursion with memoization and using tabulation.

Task Description

The input consists of the length of the rod and an array of prices, where price[i] is the price of a rod of length i+1.
You need to determine how to cut the rod in order to achieve the maximum profit.
Implement both dynamic programming approaches.
Output the optimal cutting strategy and the maximum profit.


Technical Requirements

1. Input data format:


length = 5 # length of the rod
prices = [2, 5, 7, 8, 10] # prices for lengths 1, 2, 3, 4, 5


2. Constraints:

The length of the rod must be greater than 0.
All prices must be greater than 0.
The price array cannot be empty.
The length of the price array must correspond to the length of the rod.


Acceptance Criteria

The program implements two methods (10 points for each method):

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using memoization
    """
    pass

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using tabulation
    """
    pass


2. Each method returns a dictionary:

Maximum profit (10 points).
List of segment lengths (10 points).
Total number of cuts (10 points).


Expected Output Format

{
    "max_profit": 12, # maximum profit
    "cuts": [2, 2, 1], # list of segment lengths
    "number_of_cuts": 2 # number of cuts
}


Program Template:

from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using memoization

    Args:
        length: the length of the rod
        prices: a list of prices, where prices[i] is the price for a rod of length i+1

    Returns:
        A dictionary containing the maximum profit and the list of cuts
    """
    
		# Your code should be here
    
    return {
        "max_profit": None,
        "cuts": None,
        "number_of_cuts": None
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using tabulation

    Args:
        length: the length of the rod
        prices: a list of prices, where prices[i] is the price for a rod of length i+1

    Returns:
        A dictionary containing the maximum profit and the list of cuts
    """
    
    # Your code should be here

    return {
        "max_profit": None,
        "cuts": None,
        "number_of_cuts": None
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
        print(f"\\nТест: {test['name']}")
        print(f"Rod Length: {test['length']}")
        print(f"Prices: {test['prices']}")

        # Testing memoization
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\\nMemoization Result:")
        print(f"Maximum Profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of Cuts: {memo_result['number_of_cuts']}")

        # Testing tabulation
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\\nTabulation Result:")
        print(f"Maximum Profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of Cuts: {table_result['number_of_cuts']}")

        print("\\nTest passed successfully!")

if __name__ == "__main__":
    run_tests()


Expected Result:

Test: Base Case
Rod Length: 5
Prices: [2, 5, 7, 8, 10]

Memoization Result:
Maximum Profit: 12
Cuts: [1, 2, 2]
Number of Cuts: 2

Tabulation Result:
Maximum Profit: 12
Cuts: [2, 2, 1]
Number of Cuts: 2

Test passed successfully!

Test: Optimal to Not Cut
Rod Length: 3
Prices: [1, 3, 8]

Memoization Result:
Maximum Profit: 8
Cuts: [3]
Number of Cuts: 0

Tabulation Result:
Maximum Profit: 8
Cuts: [3]
Number of Cuts: 0

Test passed successfully!

Test: Even Cuts
Rod Length: 4
Prices: [3, 5, 6, 7]

Memoization Result:
Maximum Profit: 12
Cuts: [1, 1, 1, 1]
Number of Cuts: 3

Tabulation Result:
Maximum Profit: 12
Cuts: [1, 1, 1, 1]
Number of Cuts: 3

Test passed successfully!