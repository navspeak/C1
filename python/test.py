import logging
from pathlib import Path
from tqdm import tqdm
import textwrap

logging.basicConfig(
    level=logging.INFO,  # Set the minimum level to capture
    format='%(asctime)s | %(levelname)s | %(message)s')


data = [1, 2, 3]
for i, j in tqdm(zip(data, data[::-1])):
    pass
print(i, j)
 

logging.debug("Debugging a variable")
logging.info("Starting model training")
logging.warning("Data file is missing some columns")
logging.error("Failed to connect to database")
logging.critical("System crash - shutting down")


def longest_unique_substring(s):
    if not s: return 0
    seen = set()
    l,r = 0,0
    max_len = 0
    while r < len(s):
        while s[r] in seen:
            seen.remove(s[l])
            # print(seen)
            l = l + 1
        seen.add(s[r])
        # print(seen)
        max_len = max(max_len, r-l+1)
        r = r + 1
    return max_len




# # Print the output
# print(f"Test 1 ('abcabcbb'): {longest_unique_substring('abcabcbb')} (Expected: 3)")
# print(f"Test 2 ('bbbbb'): {longest_unique_substring('bbbbb')} (Expected: 1)")
# print(f"Test 3 ('pwwkew'): {longest_unique_substring('pwwkew')} (Expected: 3)")
# print(f"Test 4 (''): {longest_unique_substring('')} (Expected: 0)")
# print(f"Test 5 ('dvdf'): {longest_unique_substring('dvdf')} (Expected: 3)")
# print(f"Test 6 ('abba'): {longest_unique_substring('abba')} (Expected: 2)")
# print(f"Test 7 ('tmmzuxt'): {longest_unique_substring('tmmzuxt')} (Expected: 5)")

def three_sum(nums):
    if len(nums) < 3: return [[]]
    nums.sort()
    result = []
    print(nums)
    for i in range(len(nums)):
        if i > 0  and nums[i] == nums[i-1]: continue
        j,k = i + 1, len(nums) -1
        target = -nums[i]

        while j < k:
            if nums[j]+ nums[k] == target:
                result.append([nums[i],nums[j], nums[k]])
                j = j+1
                k = k-1
                while(j < k and nums[j] == nums[j+1]):
                    j = j+1
                while( k > j and nums[k] == nums[k-1]):
                    k = k-1
            elif nums[j]+ nums[k] > target:
                k = k -1
            else:
                j = j + 1
    return result

    
# Print the output
print(f"Test 7 ('[-1, 0, 1, 2, -1, -4]'): {three_sum([-1, 0, 1, 2, -1, -4])} (Expected: [[-1, -1, 2], [-1, 0, 1]])")

def generate_salary_statement(*args):
    print(type(args))
    employee_name, base, bonus, deduction = args
    return f"""Salary Statement for {employee_name}
Basic Salary: ₹{base} 
Bonus: ₹{bonus} 
Deductions: ₹{deduction}
Gross Salary: ₹{base+bonus} 
Net Salary: ₹{base+bonus-deduction}"""

    

def evaluate_top_subjects(maths, science, english):
    # Write your code here
    subjects = ['Maths', 'Science', 'English']
    result = []

    for m, s, e in zip(maths, science, english):
        scores = [m, s, e]
        max_score = max(scores)
        top_subjects = [subject for subject, score in zip(subjects, scores) if score == max_score]
        result.append(','.join(top_subjects))

    return result

# Print the Output
print(evaluate_top_subjects(maths, science, english))
 
