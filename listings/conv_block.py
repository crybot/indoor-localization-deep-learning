def conv_block(input, filters=16, window=5, activation='relu',
               normalize=True,
               gauss_dropout=None,
               pool=False,
               decay=1e-4):
  conv = layers.Conv1D(filters, window,
                       input_shape=(None, BEACONS), padding='same',
                       kernel_regularizer=l2(decay))(input)
                       
  if activation is not None:
    conv = Activation(activation)(conv)
  if normalize:
    conv = layers.BatchNormalization()(conv)
  if gauss_dropout is not None:
    conv = GaussianDropout(gauss_dropout)(conv)
  if pool:
    conv = MaxPool1D(pool_size=2)(conv)

  return conv


