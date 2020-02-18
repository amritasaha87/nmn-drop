import os
import json
qtypes = set([])

def func(dir):
    for file in os.listdir(dir):
        if file.endswith('.json'):
            d = json.load(open(os.path.join(dir, file)))
            for k in d:
                qas = d[k]['qa_pairs']
                for qa in qas:
                    if 'qtype' in qa:
                        qtypes.add(qa['qtype'])
                        if qa['qtype'].startswith('year'):
                            print (qa['qtype'], ':::', qa['question'])
                    if ''        
                    #else:
                    #    print ('qa does not have type ::::', qa.keys())
                        
func('resources/iclr_cameraready/iclr_drop_data')
func('resources/iclr_cameraready/iclr_drop_data/questype_datasets')

for t in sorted(list(qtypes)):
    print (t)