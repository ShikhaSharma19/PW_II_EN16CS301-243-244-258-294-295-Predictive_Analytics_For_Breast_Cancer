{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.base import BaseEstimator, TransformerMixin\n",
    "\n",
    "class FeatureSelector(BaseEstimator, TransformerMixin):\n",
    "    def __init__( self, feature_names ):\n",
    "        self._feature_names = feature_names \n",
    "\n",
    "    def transform(self, X, *_):\n",
    "        return X[ self._feature_names ] \n",
    "\n",
    "    def fit(self, *_):\n",
    "        return self\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
