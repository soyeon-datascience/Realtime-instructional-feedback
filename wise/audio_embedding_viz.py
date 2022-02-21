# AUTOGENERATED! DO NOT EDIT! File to edit: 44-wav-embedding-experiments-dev.ipynb (unless otherwise specified).

__all__ = ['get_umap_fit', 'show_umap_dims', 'get_kmeans_clusters']

# Cell
#data science packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#umap
import umap
import umap.plot

#scikit learn helpers
from sklearn.cluster import KMeans

#other python packages
import os.path
import glob
import string
import re
import ast

# Cell
def get_umap_fit(data_df, fit=None, n_neighbors=15, min_dist=0.1, n_components=3,
                 metric='euclidean', random_state=1234,
                 show_plots='2d', color_by='all', figsize=(14,6)):
    '''
    Function get_umap_fit: performs dimensionality reduction on embeddings using UMAP and optionally plots first 3 dimensions and/or 3d plot colored by labels of interest
        data_df: dataframe with minimally columns 'label', 'teacher', 'length', and 'last_hidden_state_mean'
        fit (default None): UMAP fit object; used if a new computation isn't necessary and only the plots are desired
        n_neighbors (default 15): integer for number of neighbors for UMAP
        min_dist (default 0.1): float of minimum separation for UMAP
        n_components (default 3): minimum number of components allowed for UMAP dimensionality reduction
        metric (default 'euclidean'): string of distance measure for UMAP
        random_state (default 1234): random number generator setting for reproducibility
        show_plots (default '2d'): string of types of plots to show - can be any one of '2d', '3d', or 'all'
        color_by (default 'all'): string of column name for columns to show.  Currently accepts 'label', 'teacher', 'length', or 'all'
        figsize (default (14,6)): tuple of width, height of individual figure

        Returns: UMAP fit object

    '''

    if fit is None:
        # Create the data as numpy array
        data = np.array(data_df['last_hidden_state_mean'].tolist())

        # Make UMAP specifications
        fit_spec = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            n_components=n_components,
            metric=metric,
            random_state=random_state
        )

        # Generate the fit
        fit = fit_spec.fit(data)

    # Determine plots to be made
    if color_by == 'all':
        color_by_list = ['label', 'teacher', 'length']
    else:
        color_by_list = [color_by]

    # Show plots if desired
    if show_plots is not None:

        if show_plots == '2d' or show_plots == 'all':
            [show_umap_dims(fit, data_df, color_by, plot_3d=False, figsize=figsize) for color_by in color_by_list]

        if show_plots == '3d' or show_plots=='all':
            [show_umap_dims(fit, data_df, color_by, plot_3d=True, figsize=figsize) for color_by in color_by_list]

    # Return fit
    return fit

# Cell
def show_umap_dims(fit, data_df, color_by='label', plot_3d=False, figsize=(12,4)):
    '''
    Function show_umap_dims: Generates three 2D plots for first 3 dimensions or a 3d plot with points colored based on color_by
        fit: UMAP fit object
        data_df: dataframe with minimally column names 'label', 'length in seconds', 'id'
        color_by (default 'label'): string of column to color points by. Accepted values are 'label', 'length', and 'teacher'
        plot_3d (default False): boolean of whether to plot the 3d plot
        figsize (default (12,4)): tuple of size of plots

        Returns: nothing; shows three 2D plots or a 3D plot, colored by column 'color_by'
    '''

    # Determine display
    kwargs = {'cmap':'tab10'}
    if color_by == 'label':

        # Generate a color mapping dictionary
        label_list = ['PRS', 'REP', 'NEU', 'OTR', 'OT']
        int_list = [0, 1, 2, 3, 3]
        color_dict = dict(zip(label_list, int_list))

        # Determine color
        color = data_df['label'].replace(color_dict)

    elif color_by == 'length':
        color = data_df['length in seconds']
        label_list = None
        kwargs = {'cmap':'viridis', 'vmin':0, 'vmax':10}

    elif color_by == 'teacher':
        teach_ids = data_df['id'].apply(lambda x: x.split('-')[0])

        # Anonymize teacher IDs
        label_ids = teach_ids.unique().tolist()
        int_list = list(range(len(label_ids)))
        label_list = list(string.ascii_uppercase)[:len(int_list)]
        anon_ids_list = dict(zip(label_ids, label_list))
        print(anon_ids_list)

        #determine color
        color_dict = dict(zip(label_ids, int_list))
        color = teach_ids.replace(color_dict)
    else:
        ValueError("Whoops!  The input for color_by is not allowed.")

    # Do the plotting
    fig = plt.figure(figsize=figsize)
    fig.suptitle('Audio samples colored by {0} on UMAP principal dimensions'.format(color_by),
            fontsize=18)

    if not plot_3d:
        #setup for subplot values (ind 0) and axes to plot (ind 1 and 2)
        plt_dims = [[1,0,1], [2,2,1], [3,2,0]]

        [_umap_plt_displays(fit.embedding_, color_by, color, label_list, plt_dims=plt_dim, **kwargs)
         for plt_dim in plt_dims]

    else:
        _umap_plt_displays(fit.embedding_, color_by, color, label_list, plot_3d=True, **kwargs)

# Cell
def _umap_plt_displays(embeds, color_by, color, label_list, plt_dims=None, plot_3d=False, **kwargs):
    '''
    Function _umap_plt_displays: plots any individual 2D subplot of the 3 dimensions or a single 3D plot. Not to be called directly.
        embeds: numpy arrays of embeddings generated by umap fit
        color_by: string of field to color the points by
        color: list of colors to be passed to plotting function
        label_list: list of categorical names corresponding to colors of points (e.g., teacher id number)
        plt_dims (default None): used only in sets of 2D plots; these correspond to the subplot number, and the x,y,or z (1,2,3) axes to be plotted
        plot_3d (default False): True if a 3D plot is desired, otherwise a 2D plot is generated
        kwargs: other values to be passed to scatter or scatter3D plotting functions; mostly for correct settings of colorbar

        Returns: nothing, shows a single subplot of the desired subplots
    '''

    # Do the plot using the passed in dimensions
    if plot_3d:
        ax = plt.axes(projection='3d')
        emb_plt = ax.scatter3D(embeds[:,0], embeds[:,1], embeds[:,2],
                              c=color, **kwargs);
        dim1, dim2 = (1,2)
        ax.set_zlabel('UMAP Dimension 3');
    else:
        plt.subplot(1,3, plt_dims[0], aspect='equal')
        emb_plt = plt.scatter(embeds[:,plt_dims[1]], embeds[:,plt_dims[2]],
                              c=color, **kwargs);
        dim1, dim2 = plt_dims[1]+1, plt_dims[2]+1
        plt.axis('equal')

    # Setup subplot labels
    plt.xlabel('UMAP dimension {0}'.format(dim1));
    plt.ylabel('UMAP dimension {0}'.format(dim2));

    # Setup subplot legend
    if color_by == 'length':
        plt.colorbar(emb_plt)
    else:
        plt.legend(emb_plt.legend_elements()[0], label_list[:len(emb_plt.legend_elements()[0])],
                   title = color_by);

# Cell
def get_kmeans_clusters(data_df, cluster_data, k, show_plots=False):
    '''
    Function get_kmeans_clusters: performs k means clustering on data and returns model and data
        data_df: dataframe containing original data in same order as cluster_data
        cluster_data: numpy arrays with dimension samples x features to be clustered
        k: integer target number of clusters
        show_plots (default False): boolean of whether to show plots of the clusters along 1st and 2nd dimensions

        Returns scikit_learn kmeans model, copy of data_df with labels appended as the last column
    '''

    #define model specs
    kmeans_model = KMeans(n_clusters=k)

    #do the clustering
    kmeans_model.fit(cluster_data)

    #visualize clusters
    if show_plots:
        fig = plt.figure()
        emb_plt = plt.scatter(cluster_data[:,0], cluster_data[:,1], c=kmeans_model.labels_);
        plt.legend(*emb_plt.legend_elements());
        plt.xlabel('UMAP dimension 1');
        plt.ylabel('UMAP dimension 2');
        plt.title('Clustering of kmeans embeddings for k={}'.format(k), fontsize=18);
        plt.axis('equal')
        plt.gca().set_aspect('equal')

    #copy and append data
    ret_df = data_df.copy()
    ret_df['pred_cls'] = kmeans_model.labels_

    #return model
    return kmeans_model, ret_df