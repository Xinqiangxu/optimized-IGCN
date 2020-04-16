from numpy import *
import numpy as np
import sklearn
from sklearn.manifold import  TSNE
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import matplotlib.cm as cm
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})
tsne=TSNE(perplexity=30,n_components=2,init='pca',n_iter=5000)
plot_only=1000
file=open('./labels.txt')
filelist=file.readlines()
lenghth=len(filelist)
lab=zeros((lenghth, 1))
index=0
file=open('./labels.txt')
for data in file.readlines():
    data=data.strip('\n')
    nums=data.split(" ")
    nums=[float(x) for x in nums]
    lab[index, :]= nums[:]
    index+=1
file=open('./embeddings.txt')
filelist=file.readlines()
lenghth=len(filelist)
emb=zeros((lenghth, 7))
index=0
file=open('./embeddings.txt')
for data in file.readlines():
    data=data.strip('\n')
    nums=data.split(" ")
    nums=[float(x) for x in nums]
    emb[index, :]= nums[:]
    index+=1
low_dim_emb=tsne.fit_transform(emb[:plot_only, :])
labels=lab[0:plot_only,:]

def scatter(x, colors):
    # We choose a color palette with seaborn.
    palette = np.array(sns.color_palette("hls", 10))
    # We create a scatter plot.
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
                    c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

    # We add the labels for each digit.
    txts = []
    for i in range(10):
        # Position of each label.
        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()])
        txts.append(txt)
    return f, ax, sc, txts

def plot_with_labels(lowDWeights, labels):
    plt.cla()
    # 降到二维了，分别给x和y
    X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    # 遍历每个点以及对应标签
    for x, y, s in zip(X, Y, labels):
        c = cm.rainbow(int(255/9 * s))     # 为了使得颜色有区分度，把0-255颜色区间分为9分,然后把标签映射到一个区间
        plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(X.min(), X.max())
    plt.ylim(Y.min(), Y.max())
    plt.savefig('visualize.png', dpi=600)
    plt.rcParams['figure.dpi']=600
    plt.show()

plot_with_labels(low_dim_emb,labels)



