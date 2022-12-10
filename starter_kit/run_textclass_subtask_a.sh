PROJECT_DIR=$(dirname "$(pwd)")
FORMATTED_TRAIN_DATA_DIR="$PROJECT_DIR/SubtaskA/train/formatted-train-data"

CACHE_DIR="$PROJECT_DIR/data/cache"
mkdir -p "$CACHE_DIR"

for language_code_train_data in "$FORMATTED_TRAIN_DATA_DIR"/*
do
  language_code=$(basename "$language_code_train_data")
  run_dir="$PROJECT_DIR/data/runs/$language_code-sentiment"
  if [[ -d "$run_dir" ]]; then
    echo "Run dir. for \"$language_code\" already exists, skip language code"
    continue
  fi

  logs_dir="$run_dir/logs"
  state_dir="$run_dir/state"
  mkdir -p "$run_dir" "$logs_dir" "$state_dir"

  echo "Run training for \"$language_code\" language code..."

  # Run training without evaluation
  CUDA_VISIBLE_DEVICES=0 python run_textclass.py \
    --model_name_or_path "Davlan/afro-xlmr-mini" \
    --do_train \
    --per_device_train_batch_size 32 \
    --learning_rate 5e-5 \
    --num_train_epochs 1.0 \
    --max_seq_length 128 \
    --data_dir "$language_code_train_data" \
    --logging_dir "$logs_dir" \
    --logging_steps 32 \
    --log_level info \
    --output_dir "$state_dir" \
    --save_steps -1 \
    --cache_dir "$CACHE_DIR"
done
