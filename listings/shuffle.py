# Shuffle each entry of the given 2D dataset according to an array of permutations
def shuffle_dataset_entries(self, dataset, permutations):
    return np.array([np.concatenate(np.array(np.array_split(xs, len(p)))[p]) 
        for (xs, p) in zip(dataset, permutations)])

