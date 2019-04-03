def proteins(strand):
	protein_map = {
		'AUG': 'Methionine',
		'UUU': 'Phenylalanine',
		'UUC': 'Phenylalanine',
		'UUA': 'Leucine',
		'UUG': 'Leucine',
		'UCU': 'Serine',
		'UCC': 'Serine',
		'UCA': 'Serine',
		'UCG': 'Serine',
		'UAU': 'Tyrosine',
		'UAC': 'Tyrosine',
		'UGU': 'Cysteine',
		'UGC': 'Cysteine',
		'UGG': 'Tryptophan',
		'UAA': 'STOP',
		'UAG': 'STOP',
		'UGA': 'STOP'
	}

	codons = [strand[i: i+3] for i in range(0, len(strand), 3)]
	protein_list = list()
	for codon in codons:
		if codon in protein_map:
			protein = protein_map[codon]
			if protein != 'STOP':
				protein_list.append(protein)
			else:
				break
	return protein_list
