#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve LLAMA3 model..."
#/bin/ollama pull qwen:0.5b-chat
for model in llama3.2:1b nomic-embed-text:latest; do ollama pull $model; done
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid