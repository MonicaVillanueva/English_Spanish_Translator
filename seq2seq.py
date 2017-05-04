import tensorflow as tf

import tensorflow.contrib.legacy_seq2seq.python.ops.seq2seq.py
import tensorflow.models.tutorials.rnn.translate.seq2seq_model.py
# clonar repositorio


######################
## Original repository
######################

# http://git.hiddenunit.com/hakan/tersorflow/blob/9d84271a2039918994e57c2f962d2ee656f01541/tensorflow/python/ops/seq2seq.py





######################
## Explanation
######################

outputs, states = basic_rnn_seq2seq(encoder_inputs, decoder_inputs, cell)
# encoder_inputs are a list of tensors representing inputs to the encoder, i.e., corresponding to the letters A, B, C
# decoder_inputs are tensors representing inputs to the decoder, GO, W, X, Y, Z
# cell argument is an instance of the tf.contrib.rnn.RNNCell (You can use an existing cell, such as GRUCell or LSTMCell)

# outputs are a list of tensors corresponding to the outputs of the decoder in each time-step, W, X, Y, Z, EOS
# states are a list of tensors that represent the internal state of the decoder at every time-step.


outputs, states = embedding_rnn_seq2seq(
    encoder_inputs, decoder_inputs, cell,
    num_encoder_symbols, num_decoder_symbols,
    embedding_size, output_projection=None,
    feed_previous=False)

# The maximum number of discrete symbols that will appear: num_encoder_symbols on the encoder side, and num_decoder_symbols on the decoder side.
# feed_previous=False. This means that the decoder will use decoder_inputs tensors as provided (training). feed_previous=True, the decoder would only use the first element of decoder_inputs (test/make the model more robust to its own mistakes)
# when num_decoder_symbols is large return smaller output tensors, which will later be projected onto a large output tensor using output_projection

# We will use embedding_attention_seq2seq for our translation model below.





######################
## Models
######################

# bucketing, which is a method to efficiently handle sentences of different lengths