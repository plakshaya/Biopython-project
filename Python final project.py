print("DNA & Protein Analysis")

choice = input("Enter 1 for manual input or 2 for FASTA file: ")

if choice == "1":
    dna = input("Enter DNA sequence: ")
    
elif choice == "2":
    filename = input("Enter FASTA file name: ")
    
    file = open(filename, "r")
    dna = ""
    
    for line in file:
        if line.startswith(">"):
            continue
        dna = dna + line.strip()
    
    file.close()

else:
    print("Invalid choice")
    exit()


dna = dna.upper()
dna = dna.replace(" ", "")

print("Processed DNA sequence:", dna)


valid_bases = "ATGC"
is_valid = True

for base in dna:
    if base not in valid_bases:
        is_valid = False
        print("Invalid character found:", base)
        break


if is_valid:
    print("Valid DNA sequence")

    length = len(dna)
    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    if length > 0:
        gc_content = ((G + C) / length) * 100
    else:
        gc_content = 0

    print("DNA ANALYSIS")
    print("Length:", length)
    print("A:", A, "T:", T, "G:", G, "C:", C)
    print("GC Content:", round(gc_content, 2))


    complement = ""
    for base in dna:
        if base == "A": complement += "T"
        elif base == "T": complement += "A"
        elif base == "G": complement += "C"
        elif base == "C": complement += "G"

    reverse_complement = complement[::-1]
    print("reverse:", reverse_complement)


    rna = dna.replace("T", "U")

    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V',
        'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A',
        'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D',
        'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G',
        'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }

    protein = ""

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, "XYZ")
        if amino_acid == "STOP":
            break
        protein += amino_acid

    print("RNA:", rna)
    print("Protein:", protein)


    motif = input("\nEnter motif to search: ")
    positions = []

    for i in range(len(dna) - len(motif) + 1):
        if dna[i:i+len(motif)] == motif:
            positions.append(i)

    print("\nMOTIF SEARCH")
    print("Motif found", len(positions), "times")
    print("Positions:", positions)


    dna2 = input("\nEnter second DNA sequence: ")
    dna2 = dna2.upper().replace(" ", "")

    mutations = [] 

    min_len = min(len(dna), len(dna2))

    for i in range(min_len):
        if dna[i] != dna2[i]:
            mutations.append((i, dna[i], dna2[i]))

    print("\nMUTATION DETECTION")
    print("Total mutations:", len(mutations))

    for m in mutations:
        print("Position:", m[0], m[1], m[2])

    f = open("result.txt", "w")

    f.write("DNA Sequence: " + dna + "\n")
    f.write("Length: " + str(length) + "\n")
    f.write("GC Content: " + str(round(gc_content, 2)) + "%\n")
    f.write("Reverse Complement: " + reverse_complement + "\n")
    f.write("RNA: " + rna + "\n")
    f.write("Protein: " + protein + "\n")

    for m in mutations:
        f.write("Position " + str(m[0]) + ": " + m[1] + " -> " + m[2] + "\n")

    f.close()

else:
    print("Sequence is invalid. Please check input.")
    exit()