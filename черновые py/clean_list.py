import numpy as np
my_list1 = ['Abstract:', 'Infections', 'in', 'childhood', 'play', 'an', 'essential', 'role', 'in', 'the', 'pathogenesis', 'of', 'cognitive', 'and', 'psycho-emotional', 'disorders.', 'One', 'of', 'the', 'possible', 'mechanisms', 'of', 'these', 'impairments', 'is', 'changes', 'in', 'the', 'functional', 'properties', 'of', 'NMDA', 'and', 'AMPA', 'glutamate', 'receptors', 'in', 'the', 'brain.', 'We', 'suggest', 'that', 'bacterial', 'infections', 'during', 'the', 'early', 'life', 'period,', 'which', 'is', 'critical', 'for', 'excitatory', 'synapse', 'maturation,', 'can', 'affect', 'the', 'subunit', 'composition', 'of', 'NMDA', 'and', 'AMPA', 'receptors.', 'In', 'the', 'present', 'study,', 'we', 'investigated', 'the', 'effect', 'of', 'repetitive', 'lipopolysaccharide', '(LPS)', 'intraperitoneal', '(i.p.)', 'administration', '(25\xa0μg/kg/day', 'on', 'P14,', '16,', 'and', '18),', 'mimicking', 'an', 'infectious', 'disease,', 'on', 'the', 'expression', 'of', 'subunits', 'of', 'NMDA', 'and', 'AMPA', 'receptors', 'in', 'young', 'rats.', 'We', 'revealed', 'a', 'substantial', 'decrease', 'of', 'GluN2B', 'subunit', 'expression', 'in', 'the', 'hippocampus', 'at', 'P23', 'using', 'Western', 'blot', 'analysis', 'and', 'real-time', 'polymerase', 'chain', 'reaction', 'assay.', 'Moderate', 'changes', 'were', 'also', 'found', 'in', 'GluN1,', 'GluN2A,', 'and', 'GluA1', 'mRNA', 'expression.', 'The', 'LPS-treated', 'rats', 'exhibited', 'decreased', 'exploratory', 'and', 'locomotor', 'activity', 'in', 'the', 'open', 'field', 'test', 'and', 'the', 'impairment', 'of', 'spatial', 'learning', 'in', 'the', 'Morris', 'water', 'maze.', 'Behavioral', 'impairments', 'were', 'accompanied', 'by', 'a', 'significant', 'reduction', 'in', 'long-term', 'hippocampal', 'synaptic', 'potentiation.', 'Our', 'data', 'indicate', 'that', 'LPS-treatment', 'in', 'the', 'critical', 'period', 'for', 'excitatory', 'synapse', 'maturation', 'alters', 'ionotropic', 'glutamate', 'receptor', 'gene', 'expression,', 'disturbs', 'synaptic', 'plasticity,', 'and', 'alters', 'behavior.\n', 'Abstract:', 'Prolonged', 'exposure', 'to', 'manganese', '(Mn)', 'may', 'lead', 'to', 'toxic', 'effects', 'on', 'the', 'central', 'nervous', 'system', '(CNS).', 'The', 'mechanisms', 'underlying', 'neuronal', 'death', 'from', 'exposure', 'to', 'Mn', 'are', 'not', 'well', 'understood', 'but', 'undoubtedly', 'involve', 'inflammatory', 'processes.', 'The', 'aim', 'of', 'this', 'study', 'was', 'to', 'explore', 'the', 'effects', 'of', 'long-lasting', 'intranasal', 'Mn', 'exposure', 'in', 'rats', 'focusing', 'on', 'inflammatory', 'processes', 'and', 'catecholamine', '(dopamine,', 'norepinephrine)', 'levels', 'in', 'the', 'striatum', 'and', 'hippocampus.', 'It', 'was', 'found', 'that', 'intranasal', 'administration', 'by', 'instillation', 'of', 'MnCl2', 'solution', 'once', 'a', 'day', 'for', '90', 'days', 'leads', 'to', 'impaired', 'movement', 'and', 'gait.', 'We', 'also', 'observed', 'that', 'Mn', 'concentration', 'increased', 'in', 'the', 'hippocampus', '(by', '30', '%)', 'and', 'in', 'the', 'striatum', '(by', '220', '%),', 'dopamine', '(24', '%)', 'and', 'DOPAC', '(35', '%)', 'were', 'reduced', 'in', 'the', 'striatum,', 'and', 'dopamine', '(190', '%)', 'and', 'DOPAC', '(220', '%)', 'levels', 'increased', 'with', 'simultaneously', 'norepinephrine', 'reduction', '(30', '%)', 'in', 'the', 'hippocampus.', 'Observation', 'of', 'cytokine', 'mRNA', 'revealed', 'increased', 'expression', 'of', 'both', 'assayed', 'cytokines', '(IL-1β', 'and', 'TNF-α)', 'in', 'the', 'hippocampus.', 'There', 'was', 'a', '3-fold', 'increase', 'in', 'the', 'expression', 'of', 'IBA-1', 'mRNA,', '2-fold', 'increase', 'in', 'NFκB', 'mRNA,', 'and', 'dramatic', 'reduction', 'in', 'IkB', 'mRNA', 'in', 'the', 'striatum.', 'Taken', 'together,', 'intranasal', 'exposure', 'to', 'a', 'high', 'dose', 'of', 'MnCl2', 'induces', 'neuroinﬂammation', 'and', 'neurotransmission', 'disturbance,', 'but', 'the', 'effects', 'are', 'specific', 'for', 'each', 'studied', 'brain', 'region.\n', 'Abstract:', 'Shortly', 'after', 'syphilis', 'appeared', 'in', 'Europe', 'at', 'the', 'time', 'of', 'Columbus’', 'voyage', 'to', 'the', 'New', 'World,', 'the', 'big', 'pox,', 'as', 'it', 'was', 'often', 'known,', 'became', 'a', 'serious', 'issue', 'in', 'Russia', 'for', 'diagnosis,', 'treatment,', 'and', 'prevention.', 'Members', 'of', 'the', 'Russian', 'royal', 'family', 'were', 'made', 'aware', 'of', 'the', 'disease', 'from', 'adolescence', 'onward.', 'Czar', 'Peter', 'the', 'Great', 'had', 'many', 'sexual', 'contacts', 'and', 'could', 'have', 'contracted', 'any', 'number', 'of', 'sexually', 'transmitted', 'diseases', '(STDs)', 'that', 'were', 'quite', 'common', 'in', 'his', 'era.', 'Nevertheless,', 'contributions', 'analyzed', 'from', 'available', 'sources', 'by', 'his', 'contemporary', 'doctors,', 'and', 'later', 'from', 'medical', 'analyses,', 'reveal', 'no', 'evidence', 'that', 'he', 'had', 'contracted', 'syphilis', 'or', 'any', 'other', 'STD.', 'Most', 'likely,', 'he', 'died', 'from', 'acute', 'renal', 'failure', 'due', 'to', 'urinary', 'tract', 'obstruction.\n', 'Abstract:', 'Upper', 'respiratory', 'tract', 'infections', 'are', ]

my_ndarray1 = np.array(my_list1)
print( type(my_ndarray1) ,"содержит:", my_ndarray1.dtype)
print(my_ndarray1, "\n")

#очистить слова от символов
#https://www.educative.io/answers/what-is-the-numpychartranslate-function-in-python
#https://www.w3resource.com/numpy/string-operations/index.php

my_dict1 = {":" : "" ,
            "." : "" ,
            "," : "" ,
            "(" : "" ,
            ")" : "" ,
            "\n" : "" ,
            #"%" : "" ,
            "[" : "" ,
            "]" : "" ,
            "±" : "" ,
            ">" : "" ,
            "<" : "" ,
            " " : "" ,
            "=" : "" ,
            "±" : "" ,
            ";" : "" ,
            "+" : "" ,
            "“" : "" ,
            "”" : "" ,
            #"'s" : "" ,
            "~" : "" ,
            "{" : "" ,
            "}" : "" ,
            "&" : "" , }

my_table1 = "monkey".maketrans(my_dict1)

my_ndarray1_cl = np.char.translate(my_ndarray1, my_table1, deletechars=None)
print(type(my_ndarray1_cl),"содержит:", my_ndarray1_cl.dtype)
print(my_ndarray1_cl, "\n")

#сделать все буквы маленькими
my_ndarray1_cl_lo = np.char.lower(my_ndarray1_cl)
print(type(my_ndarray1_cl_lo),"содержит:", my_ndarray1_cl_lo.dtype)
print(my_ndarray1_cl_lo)

#как разделить на два слова если есть символ: / -


abstracts_AND_titles_words = my_ndarray1_cl_lo

from collections import Counter
words_repeat1 = dict(Counter(abstracts_AND_titles_words))
print(words_repeat1)








