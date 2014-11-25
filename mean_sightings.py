import matplotlib.mlab as ml
import numpy as np

def get_sightings(filename,ani):
  
  #Loading table
  tab=ml.csv2rec(filename)
  #ani=ani.capatalize()

  #Find total number of records for animal and calculate mean sightings
  isfocus=(tab['animal'] == ani)
  total_rec=np.sum(isfocus)
  meancount=np.mean(tab['count'][isfocus])

  #Return number of records and animals
  return total_rec,meancount


