import re

def validate_label(label):
    if re.search(r"[0-9]|[(<\[\]&*{]", label) is not None:
        return None

    label = label.lower()
    label = label.strip()
    label = label.replace("à", "a")
    label = label.replace("è", "e")
    label = label.replace("é", "e")
    label = label.replace("í", "i")
    label = label.replace("ò", "o")
    label = label.replace("ó", "o")
    label = label.replace("ú", "u")
    label = label.replace("_", " ")
    label = label.replace("@", " ")
    label = re.sub("[ ]{2,}", " ", label)
    label = label.replace(".", "")
    label = label.replace(",", "")
    label = label.replace(";", "")
    label = label.replace("¿", "")
    label = label.replace("?", "")
    label = label.replace("¡", "")
    label = label.replace("!", "")
    label = label.replace("–", "")
    label = label.replace("—", "")
    label = label.replace(":", "")
    label = label.replace("\"", "")
    label = label.replace("“", "")
    label = label.replace("”", "")
    label = label.replace("’", "'")
    label = label.replace("«", "")
    label = label.replace("»", "")
    label = label.replace("+", "")
    label = label.replace("…", "")
    label = label.replace("\"", "")

    return label if label else None