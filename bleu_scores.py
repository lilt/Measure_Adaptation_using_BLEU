#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sacrebleu.metrics import BLEU

# Initialize sacrebleu
bleu = BLEU()

# Define functions
def spacy_similarity(reference_translation,hypothesis):
    try:
        ref = nlp(reference_translation)
        hyp = nlp(hypothesis)
        score = hyp.similarity(ref)
        return score
    except:
        pass

def bleuscore(reference_translation,hypothesis):
    try:
        ref1 = []
        ref1.append(reference_translation)
        ref2 = []
        ref2.append(ref1)
        ref3 = []
        ref3.append(ref2)    
        hyp1 = []
        hyp1.append(hypothesis)
        hyp2 = []
        hyp2.append(hyp1)    
        result = bleu.corpus_score(hyp2[0], ref3[0])
        return result.score
    except:
        pass

# Load data
df = pd.read_excel("TICO-19input.xlsx", sheet_name="250")

df['Lilt_Base_BLEU'] = df.apply(lambda row: bleuscore(row['Lilt_base'], row['Reference_Translation']), axis=1)
df['Lilt_Adapted_BLEU'] = df.apply(lambda row: bleuscore(row['Lilt_adapted (250)'], row['Reference_Translation']), axis=1)

df.to_excel("TICO-19output.xlsx", sheet_name="250")


# In[ ]:





# In[ ]:





# In[ ]:




