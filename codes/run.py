num_classes = 3
max_seq_len = 1000

from transformer_v3 import Semi_Transformer
model = Semi_Transformer(num_classes=num_classes , 
                        seq_len = max_seq_len)
outputs, features = model(imgs) # outputs is the classification layer output (do cross entropy loss)
                                #features are used as video embedding



