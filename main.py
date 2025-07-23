import os, json, fitz

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    title = ""
    font_sizes = set()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    size = span["size"]
                    text = span["text"].strip()
                    font_sizes.add(size)
                    if page_num == 1 and size > 20 and not title:
                        title = text
                    if len(text.split()) > 2 and len(text) < 100:
                        headings.append({
                            "text": text,
                            "size": size,
                            "page": page_num
                        })

    sizes = sorted(list(font_sizes), reverse=True)
    size_to_level = {}
    if len(sizes) >= 3:
        size_to_level = {sizes[0]: "H1", sizes[1]: "H2", sizes[2]: "H3"}

    outline = []
    for h in headings:
        level = size_to_level.get(h["size"])
        if level:
            outline.append({
                "level": level,
                "text": h["text"],
                "page": h["page"]
            })

    return { "title": title, "outline": outline }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            in_path = os.path.join(input_dir, filename)
            out_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            result = extract_outline(in_path)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()