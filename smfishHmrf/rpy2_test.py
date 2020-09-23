#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:17:31 2020

@author: haotian teng
"""
import rpy2.robjects.numpy2ri
from rpy2.robjects.packages import importr
import numpy as np
rpy2.robjects.numpy2ri.activate()
importr("smfishHmrf")


gene_n = 100
sample_n = 1500
maxnei = 40

expression = np.random.normal(size = (sample_n,gene_n))
multi = robjects.r("smfishHmrf.hmrfem.multi")
rc = multi(y=expression, neighbors=adjacency, beta=beta, numnei=numnei, 
              blocks=block, mu=mu, sigma=cov, verbose=True, 
              err=1e-7, maxit=0)