# Biopython-project
Analysing unknown biological sequence, validating its quality, identifying homologous sequences and predicting its biological functions using computational analysis
Step 1- Retrieved hypothetical protein from NCBI
Step 2- Finding length and the record id.
Step 3- Analysed the protein using ProtParam to find the percentage of each amino acid in the protein in dictionary format(key:value).Also identified protein weight and GRAVY score(Grand Average of Hydropathecity) to understand if the protein is soluble or not.GRAVY score less than zero indicates soluble and cytoplasmic protein , if more than zero it indicates non-soluble protein. Here I found that the molecular weight was 79259.4248 and the gravy score was -0.4660844250363901 which indicated that the protein is soluble and cytoplasmic.From the amino acid percentage calculation, I saw that there is no low-quality contents in this sequence.
Step 4- Homology BLAST analysis
i)The E value as 0
ii)Percentage identification to be 75-99% , where the top 3 was more than 90%
iii) UniProt annotations of homologous proteins describe β-galactosidase activity involved in carbohydrate metabolism.

Tools & Libraries Used
Biopython (SeqIO, ProtParam, NCBIWWW, NCBIXML)
Python standard libraries (collections)
