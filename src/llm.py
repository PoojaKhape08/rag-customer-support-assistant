def generate_answer(docs, query):
    if not docs:
        return "No relevant answer found."

    context = "\n".join([doc.page_content for doc in docs])

    lines = context.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip()

        if line == "" or "---" in line or "Fee Structure" in line:
            continue

        clean_lines.append(line)

    clean_lines = list(dict.fromkeys(clean_lines))
    final = "\n".join(clean_lines[:10])

    return final.strip()
