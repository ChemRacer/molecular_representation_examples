import gudhi
import matplotlib.pyplot as plt

# Import your dataset.
pt_cloud_x = [3,3.5,2,1,2,1,3,4.5,6.5,8,8,7,8,7,
                5,8,8,7.5,9,10,11,12,9,11,11.5]
pt_cloud_y = [1,2,2,4,5,6,8,1,1,2,3.5,4,6,7,7,8,
                10,9,7.5,7,8,8.5,11,11,10]
pt_cloud = zip(pt_cloud_x,pt_cloud_y)

#Use GUDHI to generate the corresponding Rips complex,
rips_complex = gudhi.RipsComplex(points=pt_cloud, max_edge_length=20)
# simplex tree,
simplex_tree = rips_complex.create_simplex_tree(max_dimension=3)
# and persistence data from the point cloud
diag = simplex_tree.persistence(min_persistence=0.4)

# Generate the persistence barcode.
pb = gudhi.plot_persistence_barcode(diag, max_intervals=0,
                                        alpha=1.0,legend=True)
# Generate the persistence diagram.
pd = gudhi.plot_persistence_diagram(diag, max_intervals=0,
                                        alpha=1.0,legend=True)

# Plot the barcode and diagram
plt.show()
