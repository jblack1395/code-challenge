# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

# Calculate the hammand distance of two equal length strings.
def compute(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
#    n = 0 
#    for i in range(0, len(s1)): 
#       if s1[i] != s2[i]:
#          n += 1
#    return n
    return distance.levenshtein(s1, s2, normalized=True)
