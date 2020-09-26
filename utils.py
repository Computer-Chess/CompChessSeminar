import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale = 1.2)

def get_coordinates(file_rank):
    if len(file_rank) != 2:
        raise ValueError('WRONG FILE-RANK LENGTH! EXPECTED 2, GOT {length}.'.format(length=len(file_rank)))
    
    file = file_rank[0]

    try:
        rank = int(file_rank[1])
    except Exception as ex:
        print('ERROR WHILE TRYING TO PARSE RANK. NOT A VALID INTEGER: {}'.format(file_rank[1]))
        print(ex)
        return
    
    if not ('a' <= file <= 'h') or not (1 <= rank <= 8):
        raise ValueError('FILE {file} OR RANK {rank} NOT VALID!'.format(file=file, rank=rank))
    
    return (ord(file) - ord('a'), rank - 1)

def get_control_heatmap(cls, nRows, nCols):
    '''
    Returns a matrix nRows x nCols
    whose values h[i,j] (i < nRows, j < nCols)
    indicate the NUMBER of squares over which the piece of type cls
    has control if put at square h[i,j].
    '''
    heatmap = np.flip(np.array([[cls.get_possible_moves(i,j,nRows,nCols).sum()\
                                 for j in range(nCols)] for i in range(nRows)]))
    return heatmap

def plot_heatmap(heatmap, title=None, fname=None, **kwargs):
    fig, ax = plt.subplots(figsize=kwargs.pop('figsize', (5, 5)))
    
    nrows, ncols = heatmap.shape
    x_lbls = [chr(ord('a') + i) for i in range(nrows)]
    y_lbls = [str(j+1) for j in range(ncols)][::-1]

    ax.set_title(label=title)

    hm = sns.heatmap(data=heatmap, annot=heatmap, ax=ax,
                     xticklabels=x_lbls, yticklabels=y_lbls, **kwargs)
    sns.despine(ax=ax, top=True, bottom=True, left=True, right=True)

    hm.set_yticklabels(hm.get_yticklabels(),rotation=0)
    ax.axis('equal')
    if fname is None:
        plt.show()
    else:
        fig.savefig(fname)
