# Replace each dataset entry with a placeholder with probability `p`
def replace_dataset_entries(self, dataset, placeholder=-200, p=0.2):
    us = np.random.uniform(size=len(dataset))
    return np.array([np.where(u > p, xs, placeholder) 
        for (u, xs) in zip(us, dataset)])
