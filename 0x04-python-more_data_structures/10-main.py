#!/usr/bin/python3
best_score = __import__('10-best_score').best_score
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
mwalitumpa = 1
best_key = best_score(0)
print("Best score: {}".format(best_key))
