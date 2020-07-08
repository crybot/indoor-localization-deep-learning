def build_model(config):
  aux_input = Input(shape=(2, ), name='aux_input')
  main_input = Input(shape=(DOWNSAMPLED_LENGTH, BEACONS), name='main_input')
  compass_input = Input(shape=(1, ), name='compass_input') # only compass
  # Memory input to the network: it is a value between [0, 1] 
  memory_input = Input(shape=(1,), name='memory_input') 
  ... 
  ########################## CONVOLUTIONAL LAYERS ################################
  # First block
  conv = conv_block(main_input, kernels, window,
                    input_shape=(DOWNSAMPLED_LENGTH, BEACONS), decay=decay,
                    activation=activation)
  # Second block
  conv = conv_block(conv, kernels, window, activation, decay=decay, gauss_dropout=gauss/2, pool=True)
  # Third block
  kernels *= 2
  conv = conv_block(conv, kernels, window, activation, decay=decay, gauss_dropout=gauss, pool=True)
  # Fourth block
  kernels *= 2
  conv = conv_block(conv, kernels, window, activation, decay=decay, gauss_dropout=gauss, pool=True)
  # Series of non pooling convolutional blocks
  for i in range(CNN_layers):
    conv = conv_block(conv, kernels, window, activation, decay=decay)
  # Last CNN block
  kernels *= 2
  conv = conv_block(conv, kernels, window, activation, decay=decay)
  # Global pooling layer
  conv = layers.GlobalAvgPool1D()(conv)
  flattened = layers.Flatten()(conv)
  flattened = layers.Dropout(config['dropout_rate'])(flattened) # Apply dropout to approximate model set averaging
  flattened = layers.concatenate([flattened, compass_input])
  aux_output = Dense(64, activation='relu')(flattened)
  aux_output = Dense(2, activation='linear', name='aux_output')(aux_output)
  # Reshape the memory tensor (which is actually a scalar) to match aux_input shape
  coefficient = layers.RepeatVector(aux_input.shape[1])(memory_input)
  coefficient = layers.Flatten()(memory_input)
  weighted_aux_input = layers.multiply([coefficient, aux_input])
  merged = layers.concatenate([aux_output, weighted_aux_input, memory_input]) # merge beacons and other inputs
  ############################## DENSE LAYERS ####################################
  layer2 = Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2())(merged)
  output = Dense(2, activation='linear', name='main_output')(layer2)
  return Model(inputs=[main_input, compass_input, aux_input, memory_input],
                outputs=[output, aux_output])
