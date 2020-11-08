import numpy as np
import matplotlib.pyplot as plt


#dataset
def bin_emb(up):
    return (format(i, '0300b') for i in range(up))

def pos_enc(word_emb,pos):
    
    word_pos,word_emb = [],np.array([i for i in word_emb],dtype=np.float64)

    for i in range(len(word_emb)):
        k = 2*i / len(word_emb)
        if i%2 == 0:
            word_pos.append(np.sin(pos/(10000**k)))
        else:
            word_pos.append(np.cos(pos/(10000**k)))
    
    return word_emb + word_pos


if __name__ == "__main__":

    size = 200
    bin_pos = np.array([pos_enc(num,i) for i,num in enumerate(bin_emb(size))])
    
    plt.imshow(bin_pos,interpolation='nearest')
    plt.show()


