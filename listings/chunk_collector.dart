class ChunkCollector extends StreamTransformerBase<ScanResult, List<num>> {
  /* class fields */
  ...

  ChunkCollector(this.devices, this.interval, this.size);

  // add {avg(list)}^(list.length - size) elements to list.
  Iterable<int> _normalizeList(Iterable<int> list, int size) {
    if (list.length > size) {
      return list.take(size);
    }
    if (list.length < size) {
      final int mean = (list.reduce((a, b) => a + b) / list.length).round();
      return List.from(list)..addAll(List.filled((size - list.length), mean));
    }
    return list;
  }

  List<int> processChunk(Map<String, List<int>> signals) {
    // Make sure we sampled from all of the selected devices.
    // If not, add a placeholder (-200) for that device
    for (String deviceName in devices) {
      signals.putIfAbsent(deviceName, () => [-200]);
    }
    // Normalize and flatten the measurements into a row vector
    final flattened =
        signals.values.expand((xs) => _normalizeList(xs.toList(), size)).toList();
    return flattened;
  }

  Stream<List<num>> bind(Stream<ScanResult> stream) async* {
    // Connect to the stream and transform it in chunks of size this.size
    ...
  }
}
