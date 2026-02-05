class RestictionEnzyme():
    
    def __init__(self, name, recognition_site, cut_position):
        self.name = name
        self.recognition_site = recognition_site
        self.cut_position = cut_position

    #This method finds the sites at which the enzyme cuts the sequence and collects them.  
    def find_sites(self, dna_sequence):
        start_positions = []
        for x in range(0, len(dna_sequence) - len(self.recognition_site) + 1):              #Scans for x in the dna_sequence until the last logical possibility
            if dna_sequence[x : x + len(self.recognition_site)] == self.recognition_site:   #This compares the dna_sequence from x -> known length to the known site 
                start_positions.append(x)
        return start_positions
    
    #This method cuts the DNA sequence at the target sequence and collects the resulting DNA fragments
    def cut(self, dna_sequence):
        dna_fragments = []
        cut_positions = [0]

        #This first loop is for the cutting positions
        for x in range(0, len(dna_sequence) - len(self.recognition_site) + 1):              #Same logic as per find_sites()
            if dna_sequence[x : x + len(self.recognition_site)] == self.recognition_site:    
               cut_positions.append(x + self.cut_position)                                  #You append the cutting position + the index
        cut_positions.append(len(dna_sequence))

        #The second loop collect the DNA fragments by cutting the input sequence at the collected indices
        for i in range(len(cut_positions) -1):
            slice = dna_sequence[cut_positions[i] : cut_positions[i + 1]]
            dna_fragments.append(slice)
        return dna_fragments
    
    #This method simply returs the informations about the enzyme as a string
    def __str__(self):
        return f"{self.name} ({self.recognition_site}), cuts after position: {self.cut_position}"
    

#Some predefined restriction enzymes
restriction_enzymes = {
    "EcoRI":    {"recognition_site": "GAATTC",   "cut_position": 1},
    "BamHI":    {"recognition_site": "GGATCC",   "cut_position": 1},
    "HindIII":  {"recognition_site": "AAGCTT",   "cut_position": 1},
    "NotI":     {"recognition_site": "GCGGCCGC", "cut_position": 2},
    "XhoI":     {"recognition_site": "CTCGAG",   "cut_position": 1}
}

#Valid DNA inputs
valid_seq_inputs = {"A", "T", "C", "G"}

inp    = input("Enter your restriction enzyme: ")
inp2   = input("Enter your DNA sequence: ")
length = len(inp2)
seq    = str.upper(inp2)

valid_seq = True

#Check for input validity
if length == 0:
    valid_seq = False 
else:
    for a in range(0, length):
        if seq[a] not in valid_seq_inputs:
            valid_seq = False
            break

#Returns all the information
if valid_seq:
    seq1 = RestictionEnzyme(inp,
                             restriction_enzymes[inp]["recognition_site"],
                             restriction_enzymes[inp]["cut_position"]
    )
    print(f'''
          {seq1.__str__()}
          Entered Sequence: {seq}
          Generated Fragments: {seq1.cut(seq)}
          Sites of interest fount at position(s): {seq1.find_sites(seq)}
          ''')
else:
    print("Please enter a valid sequence!")                                 