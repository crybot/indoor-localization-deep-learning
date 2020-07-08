def mag_warp(self, v, mu=1, sigma=0.1, max_length=3, max_peaks=4):
    new_v = np.copy(v)
    for row in range(v.shape[0]):
        peaks = round(np.random.uniform(1, max_peaks))
            for peak in range(peaks):
                length = round(np.random.uniform(1, max_length))
                    application_point = np.random.randint(0, v.shape[1]-length)
                    mass = np.random.normal(mu, sigma)
                    for point in range(application_point, application_point+length):
                        new_v[row][point] *= mass
                            return new_v
