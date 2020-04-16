# Optimized-IGCN
This is a TensorFlow implementation of Graph Convolutional Networks
Installation
python setup.py install
Requirements
tensorflow (>0.12)
networkx
Run the demo
cd gcn
python train.py
Data
In order to use your own data, you have to provide

an N by N adjacency matrix (N is the number of nodes),
an N by D feature matrix (D is the number of features per node), and
an N by E binary label matrix (E is the number of classes).
Have a look at the load_data() function in utils.py for an example.

In this example, we load citation network data (Cora, Citeseer or Pubmed). The original datasets can be found here: http://www.cs.umd.edu/~sen/lbc-proj/LBC.html. In our version (see data folder) we use dataset splits provided by https://github.com/kimiyoung/planetoid (Zhilin Yang, William W. Cohen, Ruslan Salakhutdinov, Revisiting Semi-Supervised Learning with Graph Embeddings, ICML 2016).

You can specify a dataset as follows:

python train.py --dataset citeseer
(or by editing train.py)

