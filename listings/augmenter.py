class TimeseriesDataAugmenter():
    def __init__(self, dataset, target,
            jittering=True,
            shuffling=True,
            scaling=True,
            magnitude_warp=True):
        self.dataset = np.copy(dataset)
        self.target = np.copy(target)

    def augment(self, 
            iterations=10, 
            seed=42, 
            deactivation_rate=0.2, 
            scale_sigma=0.008, 
            warp_sigma=0.04):
        ...

    def mag_warp(self, v, mu=1, sigma=0.1, max_length=3, max_peaks=4):
        ... 

    def replace_dataset_entries(self, dataset, placeholder=-200, p=0.2):
        ... 

    def scale_dataset_entries(self, dataset, sigma=0.005):
        ... 

    def shuffle_dataset_entries(self, dataset, permutations):
        ... 
