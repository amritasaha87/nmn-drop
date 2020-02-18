#allennlp predict \
#    --output-file output/dev/drop_answer_dev.jsonl \
#    --predictor drop_demo_predictor \
#    --include-package semqa \
#    --silent \
#    --batch-size 1 \ 
#    resources/iclr_cameraready/ckpt/model.tar.gz resources/iclr_cameraready/iclr_drop_data/jsonl/drop_dataset_dev.jsonl

allennlp predict \
    --output-file test/output.jsonl \
    --predictor drop_demo_predictor \
    --include-package semqa \
    --silent \
    --batch-size 1 \ 
    resources/iclr_cameraready/ckpt/model.tar.gz test/input.jsonl
