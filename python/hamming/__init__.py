# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

# Calculate the hammand distance of two equal length strings.
def compute(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(t1 != t2 for t1,t2 in  zip(s1, s2))
