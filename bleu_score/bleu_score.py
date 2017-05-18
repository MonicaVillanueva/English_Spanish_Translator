from os import system
import subprocess
import os
import numpy as np
import re


# Change the file paths
ref_path= os.path.join(os.getcwd(),'ref.txt')
output_path = os.path.join(os.getcwd(),'output.txt')
# Regular expressions used to tokenize.
_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")
TOKENIZER = 0




def basic_tokenizer(sentence):
  """Very basic tokenizer: split the sentence into a list of tokens."""
  words = []
  for space_separated_fragment in sentence.strip().split():
    words.extend(_WORD_SPLIT.split(space_separated_fragment))
  return [w for w in words if w]



## Main
if __name__ == "__main__":

    if TOKENIZER == 1:
        with open(ref_path, 'r') as ref:    # close the file immediately
            ref_content = ref.read()
        with open(output_path, 'r') as out:
            out_content = out.read()

        # Separate in lines
        ref_content = ref_content.split('\n')
        out_content = out_content.split('\n')

        if len(ref_content) != len(out_content):
            print 'ERROR: number of sentences to compare do not match'
            exit(-1)

        ref_aux = open('ref', 'w')
        ref_path = os.path.join(os.getcwd(),'ref')
        output_aux = open('output', 'w')
        output_path = os.path.join(os.getcwd(), 'output')

        c = 0
        r = 0
        for i in range(len(ref_content)):
            ref_seq = basic_tokenizer(ref_content[i])   # Change by the desired tokenizer
            out_seq = basic_tokenizer(out_content[i])

            sentence = ' '.join(ref_seq)
            r = r + len(sentence)
            ref_aux.write(sentence)
            ref_aux.write('\n')

            sentence = ' '.join(out_seq)
            c = c + len(sentence)
            output_aux.write(sentence)
            output_aux.write('\n')

        ref_aux.close()
        output_aux.close()

    # Apply BLEU score
    command = './multi-bleu.perl -lc' + str(ref_path) + ' < ' + str(output_path)    # -lc = lower case
    text = subprocess.check_output(command, shell=True)     # Example: BLEU = 75.0/66.1/54.7/45.0 (BP=1.000, ratio=1.000, hyp_len=16, ref_len=16)

    sp = text.split()
    scores = sp[2].split('/')
    penalty = sp[3].split('=')[1]
    penalty = float(penalty[0:len(penalty)-1])

    N = len(scores)
    glob_precision = map(float, scores)
    geom_avg = sum(1./N * np.log(glob_precision))

    final_score = penalty * np.exp(geom_avg)
    print final_score



