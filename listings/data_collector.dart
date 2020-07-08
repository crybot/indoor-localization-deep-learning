class DataCollector {
  /* class fields */
  ...

  DataCollector(this._selectedDevices,
      {this.target = const Point(0.0, 0.0),
      this.interval = const Duration(milliseconds: 1000),
      this.chunkSize = 30}) {
    ...
  }

  Stream<List<num>> startCollecting({Duration timeout}) {
    _compass.listen();
    Stream<List<num>> signalsStream = _bluetooth
        .scan(timeout: timeout, scanMode: ScanMode.lowLatency)
        .transform(ChunkCollector(_selectedDevices, interval, chunkSize));

    // Add other parameters to the data
    return signalsStream.map((signals) {
      // Sample the previous location from N(p; [x,y]^T, sigma*I)
      final s = 0.5;
      final previousX = Normal.generate(1, mean: target.x, variance: s).first;
      final previousY = Normal.generate(1, mean: target.y, variance: s).first;
      return [
        previousX,
        previousY,
        target.x,
        target.y,
        _compassValue,
        ...signals
      ];
    });
  }

  ...
}
