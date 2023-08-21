# Benchmark Models

To test the performance of cutting-edge CGEC approaches on our FlaCGEC dataset, we adopt three mainstream benchmark CGEC models, which have either Seq2Edit or Seq2Seq architecture. 

**GECToR-Chinese** is a Seq2Edit model which is derived from an English GEC model, namely GECToR. GECToR predicts the edits, including insertion, deletion, and substitution, to correct sentences. Due to the different format of tokens between English and Chinese, modification on the tokenizer is made to accommodate GECToR to Chinese.

**Chinese BART** is a Seq2Seq model that treats GEC tasks as machine translation, which translates source sentences into target sentence token by token. It follows Transformer architecture and combines multiple pre-training schemes. When it comes to CGEC tasks, we adopt the Chinese BART model without any modification.

**EBGEC** is also a Seq2Seq model built upon Transformer. It incorporates a KNN module to retrieve the most similar example from a data-store and predict tokens by fusing the distribution from KNN and distribution from vanilla Transformer, which enhances the interpretability of the basic model.

We use public source codes of the aforementioned benchmark models, keep their official hyper-parameters unchanged, and conduct experiments with different settings, which are illustrated in great detail in the following.

For GECToR-Chinese, we employ the StructBert as its encoder and train the model with the Adam optimizer. We set batch size as $16$ and learning rate as $1e-5$ for training. The maximum training epoch number is set as $40$ for all evaluated datasets. In addition, we setup a warm-up procedure, where the model is first trained for $2$ cold epochs with a learning rate of $1e-3$.

For Chinese BART, we leverage Chinese-BART-Large as the pre-trained model, and train the model with the Adam optimizer. We set the learning rate as $3e-6$, and adjust it with the learning rate scheduler of Polynomial. The maximum training epoch number is set as $10$ for all evaluated datasets. 

For EBGEC, Transformer-big is employed as the encoder and the beam search with a beam size of $5$ is utilized as decoding strategy. We also train the model with the Adam optimizer. We set the learning rate as $5e-4$ for FlaCGEC and $5e-5$ for the other two datasets.