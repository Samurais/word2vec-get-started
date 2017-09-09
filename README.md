# word2vec-get-started
![](https://camo.githubusercontent.com/ae91a5698ad80d3fe8e0eb5a4c6ee7170e088a7d/687474703a2f2f37786b6571692e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f61692f53637265656e25323053686f74253230323031372d30342d30342532306174253230382e32302e3437253230504d2e706e67)

# Welcome
Fit language model tasks with [word2vec](https://code.google.com/archive/p/word2vec) and [insuranceqa-corpus](https://github.com/Samurais/insuranceqa-corpus-zh).


## Install
```
scripts/compile.sh # verified on Ubuntu 16.04
source ./env.sh
word2vec # for verify
```

## Train
```
cp localrc.sample localrc # modify keys
scripts/train.sh
```

## Get similarities
Post training, a model file is generated in ```tmp```, use ```distance``` to get similarities for words.

```
$ src/distance tmp/iqa.w2v.20170909113039.bin1.neg1.cbow0.win5.iter30.embed100.thr30
Enter word or sentence (EXIT to break): 家庭

Word: 家庭  Position in vocabulary: 83

                                              Word       Cosine distance
------------------------------------------------------------------------
                                            日托                0.648058
                                            住房                0.645767
                                            初创                0.631415
                                            宝石                0.621161
                                            家务                0.612938
                                            家中                0.603859
                                            还为                0.593459
                                            牧场                0.589468
                                            家居                0.585816
                                            居所                0.585174
```

# License
[Apache 2.0](./LICENSE)

# Trouble Shooting

1. compile error on Ubuntu
install build essentials
```
sudo apt-get install build-essential
```
