from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
from transformers import EarlyStoppingCallback
import torch

# Load pre-trained model and tokenizer
model_name = "meta-llama/Llama-3.1-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load dataset from Hugging Face Hub
dataset = load_dataset("osunlp/TravelPlanner")


# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(
        examples["text"], padding="max_length", truncation=True, max_length=512
    )


tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Split dataset into train and validation
train_dataset = tokenized_datasets["train"]
eval_dataset = tokenized_datasets["validation"]

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",  # Perform evaluation at the end of each epoch
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    weight_decay=0.01,
    logging_dir="./logs",  # Store logs
    logging_steps=200,  # Log every 200 steps
    save_steps=500,  # Save checkpoint every 500 steps
    save_total_limit=2,  # Keep only the last 2 saved checkpoints
    num_train_epochs=3,  # Number of training epochs
    fp16=True,  # Use mixed precision for faster training (if supported)
    load_best_model_at_end=True,  # Save the best model during training
    metric_for_best_model="eval_loss",  # Evaluate based on the validation loss
    greater_is_better=False,  # Lower loss is better
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    callbacks=[
        EarlyStoppingCallback(early_stopping_patience=2)
    ],  # Early stopping after 2 epochs of no improvement
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

# Optional: Evaluate the model
eval_results = trainer.evaluate()
print(f"Evaluation results: {eval_results}")
