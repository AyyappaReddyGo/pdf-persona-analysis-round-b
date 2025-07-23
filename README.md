# PDF Outline Extractor (Round 1A - Adobe Connecting the Dots Challenge)

## Overview
This tool extracts structured outlines (Title, H1, H2, H3) from PDF documents and outputs them in JSON format.

## Features
- Extracts document title from the first page
- Detects H1, H2, and H3 headings based on font size hierarchy
- Outputs JSON per PDF with page numbers and heading levels

## How to Build and Run

### Build the Docker Image
```bash
docker build --platform linux/amd64 -t heading-extractor:yourname .
```

### Run the Container
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none heading-extractor:yourname
```

## Output Format
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Intro", "page": 1 },
    { "level": "H2", "text": "Sub-topic", "page": 2 }
  ]
}
```

## Notes
- No external network calls
- All processing is CPU-based
- Handles PDFs up to 50 pages under 10 seconds