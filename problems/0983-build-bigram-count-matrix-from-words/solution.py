import numpy as np

def bigram_counts(words):
    # Your code here
    chars = sorted(set(''.join(words)))
    vocab = ['.'] + chars
    stoi = {c: i for i, c in enumerate(vocab)}

    V = len(vocab)
    N = np.zeros((V, V), dtype=int)
    for w in words:
        seq = ['.'] + list(w) + ['.']
        for a, b in zip(seq, seq[1:]):
            N[stoi[a], stoi[b]] += 1

    return N.tolist()
