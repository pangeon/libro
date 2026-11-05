#!/bin/bash
DIRECTORY="data/copy"

if [ -d "$DIRECTORY" ]; then
  echo "Folder $DIRECTORY is exist."
else
  echo "Folder $DIRECTORY does not exist, creating..."
  mkdir -p "$DIRECTORY"
fi

files=("book.json" "magazines.json" "boxed_games.json" "digital_games.json" "movies.json")

for file in "${files[@]}"; do
  filepath="$DIRECTORY/$file"
  
  if [ ! -s "$filepath" ]; then
    echo "[]" > "$filepath"
    echo "Created/initialized file $filepath with content []"
  else
    echo "File $filepath already exists and contains data."
  fi
done

echo "All files checked and initialized..."
echo ""

python3 main.py
