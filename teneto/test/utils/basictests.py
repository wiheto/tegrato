
import teneto
import numpy as np
import matplotlib.pyplot as plt

def test_graphletconversion():
    # For reproduceability
    np.random.seed(2018) 
    # Number of nodes
    N = 3
    # Number of timepoints
    T = 5
    # Probability of edge activation
    p0to1 = 0.2
    p1to1 = .9
    G = teneto.generatenetwork.rand_binomial([N,N,T],[p0to1, p1to1],'graphlet','bu')
    C = teneto.utils.graphlet2contact(G)
    G2 = teneto.utils.contact2graphlet(C)
    assert G.all() == G2.all()

def test_networkmeasures_tdc(): 
    # Make simple network
    G = np.zeros([3,3,4])
    G[0,1,[0,2,3]] = 1
    G[0,2,1] = 1
    G[1,2,3] = 1
    G += G.transpose([1,0,2]) 
    G = teneto.utils.set_diagonal(G,1)
    # Call different instances of temporal_degree_centrality 
    C1 = teneto.networkmeasures.temporal_degree_centrality(G)
    C2 = teneto.networkmeasures.temporal_degree_centrality(G,axis=1)
    C3 = teneto.networkmeasures.temporal_degree_centrality(G,axis=1,calc='time')
    C4 = teneto.networkmeasures.temporal_degree_centrality(G,axis=1,calc='time',decay=0.5)
    tC4 = np.array(C3)
    for n in range(1,tC4.shape[-1]): 
        tC4[:,n] = tC4[:,n] + tC4[:,n-1] * np.exp(-0.5)
    assert (C1 == G.sum(axis=2).sum(axis=1)).all()    
    assert (C2 == G.sum(axis=2).sum(axis=0)).all()
    assert C3.shape == (3,4)
    assert (C3 == G.sum(axis=1)).all()
    assert (C3 == G.sum(axis=1)).all()
    assert (C4 == tC4).all()
    
def test_networkmeasures_stp(): 
    # Make simple network
    G = np.zeros([3,3,4])
    G[0,1,[0,2,3]] = 1
    G[0,2,1] = 1
    G[1,2,3] = 1
    G += G.transpose([1,0,2]) 
    G = teneto.utils.set_diagonal(G,1)
    sp = teneto.networkmeasures.shortest_temporal_path(G)
    sp['paths'] = teneto.utils.set_diagonal(sp['paths'],0)
    paths_true = np.zeros(sp['paths'].shape)
    #reminder dimord is from,to
    paths_true[0,1,0] = 1
    paths_true[0,2,0] = 2
    paths_true[1,0,0] = 1
    paths_true[1,2,0] = 2
    paths_true[2,1,0] = 3
    paths_true[2,0,0] = 2
    paths_true[0,1,1] = 2
    paths_true[0,2,1] = 1
    paths_true[1,0,1] = 2
    paths_true[1,2,1] = 3
    paths_true[2,1,1] = 2
    paths_true[2,0,1] = 1
    paths_true[0,1,2] = 1
    paths_true[0,2,2] = 2
    paths_true[1,0,2] = 1
    paths_true[1,2,2] = 2
    paths_true[2,1,2] = 2
    paths_true[2,0,2] = 2
    paths_true[0,1,3] = 1
    paths_true[0,2,3] = 1
    paths_true[1,0,3] = 1
    paths_true[1,2,3] = 1
    paths_true[2,1,3] = 1
    paths_true[2,0,3] = 1
    assert (sp['paths'] == paths_true).all()
    #fig,ax = plt.subplots(1)
    #ax = teneto.plot.slice_plot(G,ax)