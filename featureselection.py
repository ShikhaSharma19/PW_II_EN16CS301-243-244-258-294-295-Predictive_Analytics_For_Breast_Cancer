#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__( self, feature_names ):
        self._feature_names = feature_names 

    def transform(self, X, *_):
        return X[ self._feature_names ] 

    def fit(self, *_):
        return self


# In[ ]:




