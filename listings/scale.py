# Apply a costant multiplicative random noise to each time series
def scale_dataset_entries(self, dataset, sigma=0.005):
  scales = np.random.normal(1.0, sigma, dataset.shape[0])
    return np.array([scale * xs for (xs, scale) in zip(dataset, scales)])
