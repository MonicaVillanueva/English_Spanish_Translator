python translate.py  --data_dir ../data --train_dir ../temp  --size=512 --num_layers=3 --from_vocab_size=20000 --to_vocab_size=20000 --steps_per_checkpoint=1000  
python translate.py  --data_dir ../data --train_dir ../network_4_256_10K_tokenizer1  --size=256 --num_layers=4 --steps_per_checkpoint=500

salloc -t 16:0:0 -A edu17.DT2119 --gres=gpu:K80:2


#python translate.py --decode --data_dir ../data --train_dir ../temp2 --size=256 --num_layers=4


salloc -t 16:0:0 -A edu17.DT2119 --gres=gpu:K80:2


