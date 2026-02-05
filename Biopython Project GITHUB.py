from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

record = SeqIO.read("result.fasta", "fasta")

from Bio.SeqUtils import ProtParam

analysis = ProtParam.ProteinAnalysis(str(record.seq))
print(analysis.amino_acids_percent)

print("MW:",analysis.molecular_weight())
print("GRAVY:",analysis.gravy())
print("pI:", analysis.isoelectric_point())

from collections import Counter

counts = Counter(record.seq)
most_common = counts.most_common(1)
print("Most frequent residue:", most_common)

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
)


with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())


with open("blast_result.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)


for alignment in blast_record.alignments[:5]:
    for hsp in alignment.hsps:
        print("Protein:", alignment.title)
        print("Length:", alignment.length)
        print("E-value:", hsp.expect)
        print("Identity (%):", (hsp.identities / hsp.align_length) * 100)
        print("-" * 50)


print(record.id)
print(len(record.seq))
print("Contains stop codon:", "*" in record.seq)
seq = str(record.seq)

if "*" in seq[:-1]:
    print("Internal stop codon present (invalid protein)")
else:
    print("No internal stop codons")
