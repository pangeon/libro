#!/bin/bash
DIRECTORY="data/"
DIRECTORY_COPY="data/copy"


for directory in "$DIRECTORY_COPY" "$DIRECTORY"; do
  if [ -d "$directory" ]; then
    echo "Folder $directory is exist."
  else
    echo "Folder $directory does not exist, creating..."
    mkdir -p "$directory"
  fi
done

files=("books.json" "magazines.json" "boxed_games.json" "digital_games.json" "movies.json")

for file in "${files[@]}"; do
  filepath="$DIRECTORY/$file"
  
  if [ ! -s "$filepath" ]; then
    echo "[]" > "$filepath"
    echo "- Created/initialized file $filepath with content []"
  else
    echo "File $filepath already exists and contains data."
  fi
done

echo "All files checked and initialized..."
echo ""

python3 main.py
