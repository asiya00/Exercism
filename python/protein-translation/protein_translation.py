def proteins(strand):
    di = {"Methionine": "AUG","Phenylalanine": ("UUU","UUC"), "Leucine": ("UUA","UUG"), "Serine": ("UCU", "UCC", "UCA", "UCG"), "Tyrosine": ("UAU", "UAC"), "Cysteine": ("UGU", "UGC"), "Tryptophan": "UGG", "STOP": ("UAA", "UAG", "UGA")}
    li = []
    for i in range(0,len(strand),3):
        codons = str(strand[i:i+3])
        for key,value in di.items():
            if codons in di[key]:
                if key=="STOP":
                    return(li)
                li.append(key)                    
    return(li)
        




