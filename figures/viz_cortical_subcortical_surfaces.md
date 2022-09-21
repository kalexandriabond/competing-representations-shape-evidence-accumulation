
Instructions for visualizing the cortical / thalamic / striatal surfaces using [SurfIce](https://www.nitrc.org/projects/surfice/).

To visualize surfaces using pre-existing meshes and statistical maps: 
1) open atlas —> BrainMesh_ICBM152.mz3. set render to Default or Gouraud (what these renders look like depends on version of surfice/OS). 
2) add overlay (starting with the average map, ‘avg_enc_weights_z_space_MNI152.nii.gz’) twice. apply the winter map to one and hot map to the other. 
3) set the darkest/brightest threshold for winter to (-.001, -1) and hot (.001, 1). or flip the thresholds for these colormaps for viz. purposes if needed. 
4) view -> left or right. 
5) in preferences, set bitmap zoom factor to 6. save bitmap as png lossless with the following format: avg_enc_cortex_surface_L or {type}_enc_{structure}_surface_{direction}.png. in the case of subjects, type = sub-{n}, e.g. sub-001_enc_cortex_surface_R.png. 

For thalamus and striatum, use mean_lh+rh+thal.obj and mean_lh+rh+striatum.obj atlases. these are surfaces generated from mean volumes acquired during t1 scans.  

If you want to generate surfaces from a t1 volume:
1) go to advanced -> convert voxelwise volume to mesh. 
2) select the volume (*.nii.gz).
3) set the threshold to 2 voxels, min cluster size to 1, and decimation to 80 (chosen for the tradeoff between precision and a manageable file size.) 
4) save as multiple objects (as .obj). this is a common file type for meshes. 
5) success! now you can overlay statistical maps on the surface of this volume. 
