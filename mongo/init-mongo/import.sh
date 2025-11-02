#!/bin/bash
echo "🔁 Starting MongoDB data import..."

for file in /data/import/*; do
  filename=$(basename -- "$file")
  extension="${filename##*.}"
  name="${filename%.*}"

  db="${name%%-*}db"
  collection="${name#*-}"

  echo "📁 Importing $filename into database '$db', collection '$collection'"

  case "$extension" in
    json)
      if grep -q '^\[' "$file"; then
        mongoimport --username admin --password admin123 --authenticationDatabase admin --db "$db" --collection "$collection" --file "$file" --jsonArray
      else
        mongoimport --username admin --password admin123 --authenticationDatabase admin --db "$db" --collection "$collection" --file "$file"
      fi
      ;;
    csv)
      mongoimport --username admin --password admin123 --authenticationDatabase admin --db "$db" --collection "$collection" --type csv --headerline --file "$file"
      ;;
    *)
      echo "⚠️ Skipping unsupported file type: $filename"
      ;;
  esac
done

echo "✅ Import completed."
