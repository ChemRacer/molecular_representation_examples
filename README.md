# Molecular Representations for Machine Learning Examples
In this GitHub repository, we provide code examples from the ACS In Focus "Molecular Representations for Machine Learning" by Grier M. Jones, Brittany Story, Vasileios Maroulas, and Konstantinos D. Vogiatzis.



# Citation
```
ADD BIBTEX here
```

## Setup
These examples require multiple conda env and kernels...

1. Open `Gen_Directories.ipynb` in Google Colab, which will launch in a Google Drive folder called Colab Notebooks.
2. Generate a personal access token in GitHub. Steps: GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
3. Once you have launched the `Gen_Directories.ipynb`, there will be an empty cell with `token=''` copy your personal access token into the parenthesis
4. The cell containing `!git clone https://{token}@github.com/ChemRacer/molecular_representation_examples.git` will pull the repo to the directory /content/drive/MyDrive/Colab Notebooks/Molecular_representations/
5. The last cell will generate paths to each example:
```
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.ipynb') and 'Chapter_' in root and '.ipynb_checkpoints' not in root:
          if os.path.exists(os.path.join(root,file)):
              print(file.split('.')[0], "https://colab.research.google.com/drive/"+get_id(os.path.join(root,file)))
```
