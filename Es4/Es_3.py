import requests
import threading

class Translator(threading.Thread):
    Nucleotides = ['A', 'T', 'C', 'G']

    codonDict = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'STOP', 'TGG': 'W',
        }
        translated=[]
        def __init__(self, protein, threadLock):
            threading.Thread.__init__(self)
            self.protein=protein
            self.threadLock=threadLock
        def run(self):
            codons=[self.protein[i:i+3] for i in range(0, len(self.protein), 3)]
            translated_protein=""
            for codon in codons:
                translated_protein+=Translator.codonDict[codon.upper()]
            self.threadLock.acquire()
            Translator.translated.append(translated_protein)
            self.threadLock.release()
        
