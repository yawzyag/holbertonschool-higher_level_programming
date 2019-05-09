#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        sorted_best = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
        best = list(sorted_best[0])[0]
        return best
