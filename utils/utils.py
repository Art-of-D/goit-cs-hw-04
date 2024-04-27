import logging

# Searching keywords
def search_keywords(i, file_path, keywords, results):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                amount = 0
                if keyword in content:
                    amount += content.count(keyword)
                    results.append(f"Process {i} found {keyword} in {file_path}: {amount} times")
    except Exception as e:
        logging.error(f"Processing {file_path}: {str(e)}")
        