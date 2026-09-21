import numpy as np

def bigram_avg_nll(P, words, stoi):
    """Average negative log-likelihood of words under a bigram model."""
    total = 0.0
    n = 0
    for w in words:
        seq = '.' + w + '.'
        for c1, c2 in zip(seq, seq[1:]):
            p = P[stoi[c1], stoi[c2]]
            total += np.log(p)
            n += 1
            
    if n == 0:
        return 0.0

    return round(float(-total / n), 4)
