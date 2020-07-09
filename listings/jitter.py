def jitter(self, v, sigma=0):
    return np.add(v, np.random.normal(0, sigma, v.shape))


