# Molecular Representations for Machine Learning Examples
In this GitHub repository, we provide code examples from the ACS In Focus "Molecular Representations for Machine Learning" by Grier M. Jones, Brittany Story, Vasileios Maroulas, and Konstantinos D. Vogiatzis.

!!! ADD LICENSE !!!

# Citation
```
ADD BIBTEX here
```

## Setup
These examples require multiple conda env and kernels...

1. Install conda using [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
                                                                                                                                                                    
3. Clone repository
```
git clone https://github.com/ChemRacer/DDQC_Demo.git
```
4. Install conda environment named ddqc_demo
```
cd DDQC_Demo/conda-envs
conda env create -f ddqc_demo.yml
```

5. Link conda environment to jupyter kernel
```
conda activate ddqc_demo
ipython kernel install --user --name=ddqc_demo
conda deactivate
```
