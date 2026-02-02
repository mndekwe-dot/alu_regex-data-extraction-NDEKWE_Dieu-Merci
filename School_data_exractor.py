import re
import json

# SECURITY CONFIGURATION

max_input_size = 50000

dangerous_patterns = [
    "<script",
    "javascript:",
    "eval(",
    "DROP TABLE",
    "../"
]

# REGEX PATTERNS (REAL-WORLD FORMATS)

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
URL_PATTERN = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*'
PHONE_PATTERN = r'^07[2389]\d{7}$'
CARD_PATTERN = r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'
TIME_12H_PATTERN = r'\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)'
TIME_24H_PATTERN = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b'
HASHTAG_PATTERN = r'#[a-zA-Z0-9_]+'
CURRENCY_PATTERN = r'(?i)(?:RWF|RF)\s?\d+(?:,\d{3})*(?:\.\d{2})?'

# SECURITY CHECK (DEFENSIVE PROGRAMMING)

def is_safe_input(text):
    if not text or len(text.strip()) == 0:
        return False

    if len(text) > max_input_size:
        return False

    for bad in dangerous_patterns :
        if bad.lower() in text.lower():
            return False

    return True

# DATA MASKING FUNCTIONS(Hiding sensitive data)
def mask_email(email):
    name, domain = email.split("@")
    return f"{name[:2]}***@{domain}"

def mask_card(card):
    digits = card.replace(" ", "").replace("-", "")
    return f"****-****-****-{digits[-4:]}"

def process_line(line, store):
    if not is_safe_input(line):
        return  # unsafe input is ignored immediately

    store["emails"].extend(re.findall(EMAIL_PATTERN, line))
    store["urls"].extend(re.findall(URL_PATTERN, line))
    store["phones"].extend(re.findall(PHONE_PATTERN, line))
    store["credit_cards"].extend(re.findall(CARD_PATTERN, line))
    store["times"].extend(
        re.findall(TIME_12H_PATTERN, line) +
        re.findall(TIME_24H_PATTERN, line)
    )
    store["hashtags"].extend(re.findall(HASHTAG_PATTERN, line))
    store["currency"].extend(re.findall(CURRENCY_PATTERN, line))

# MAIN PROGRAM
def main():
    print("=" * 70)
    print("REGEX-BASED RAW TEXT DATA EXTRACTION For School SYSTEM")
    print("Paste raw text below. Type END to finish.")
    print("=" * 70)

    extracted = {
        "emails": [],
        "urls": [],
        "phones": [],
        "credit_cards": [],
        "times": [],
        "hashtags": [],
        "currency": []
    }

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        process_line(line, extracted)

    # Remove duplicates & mask sensitive data
    extracted["emails"] = list(set(mask_email(e) for e in extracted["emails"]))
    extracted["credit_cards"] = list(set(mask_card(c) for c in extracted["credit_cards"]))

    for key in extracted:
        extracted[key] = list(set(extracted[key]))

    result = {
        "status": "SUCCESS",
        "data": extracted,
        "total_found": sum(len(v) for v in extracted.values())
    }

    print("\nEXTRACTION RESULT:\n")
    print(json.dumps(result, indent=2))

    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

    print("\nResults saved to output.json")

if __name__ == "__main__":
    main()
