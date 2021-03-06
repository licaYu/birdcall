# AUTOGENERATED! DO NOT EDIT! File to edit: 02g_train_on_melspectrograms_pytorch_lme_pool_frontend.ipynb (unless otherwise specified).

__all__ = ['lme_pool']

# Cell
import torch

def lme_pool(x, alpha=1.0): # log-mean-exp pool
    '''alpha -> approximates maxpool, alpha -> 0 approximates mean pool'''
    T = x.shape[1]
    mult_log = torch.log(torch.tensor(1/T))
    return 1/alpha * (mult_log + torch.logsumexp((alpha * x), dim=1))