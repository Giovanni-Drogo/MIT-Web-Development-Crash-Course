import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
import io
# Streamlit app title
st.title("Molecule 2D Visualization")
# Input for SMILES string
smiles = st.text_input("Enter a SMILES string:", "CCCCC[C@H](CC(=O)NO)C(=O)N[C@H](C(=O)N1CCC[C@H]1CO)C(C)C")
if smiles:
    try:
        # Generate RDKit molecule from SMILES
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            # Draw molecule to an image
            img = Draw.MolToImage(mol, size=(1000, 1000))
            # Display the image in Streamlit
            st.image(img, caption="2D Molecule Structure", use_container_width=True)
        else:
            st.error("Invalid SMILES string. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a SMILES string to visualize the molecule.")
