import jsonlines
import sys
import json

infile = sys.argv[1]
out_datafile = sys.argv[2]
out_ansfile = sys.argv[3]
data = json.load(open(infile))
data_l = []
ans_l = []
for key, value in data.items():
    passage = value['passage']
    for qa in value['qa_pairs']:
        question = qa['question']
        qid = qa['query_id']
        answer = qa['answer']
        data_l.append({'passage': passage, 'question': question, 'qid': qid})
        ans_l.append({'qid': qid, 'answer': answer})
with jsonlines.open(out_datafile, 'w') as writer:
    writer.write_all(data_l)
with jsonlines.open(out_ansfile, 'w') as writer:
    writer.write_all(ans_l)
                