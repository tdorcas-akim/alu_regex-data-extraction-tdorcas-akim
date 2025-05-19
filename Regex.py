import re 
def extract_email_addresses(text):
    """Extract email addresses from text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_urls(text):
    """Extract URLs from text."""
    url_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[/\w.-]*'
    return re.findall(url_pattern, text)

def extract_time_formats(text):
    """Extract time formats (12h and 24h) from text."""
    # 24-hour format (00:00 to 23:59)
    hour24_pattern = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b'
    
    # 12-hour format with AM/PM
    hour12_pattern = r'\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)\b'
    
    return re.findall(hour24_pattern, text) + re.findall(hour12_pattern, text)

def extract_currency_amounts(text):
    """Extract currency amounts from text."""
    currency_pattern = r'[$€£¥]\d+(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)

def extract_hashtags(text):
    """Extract hashtags from text."""
    hashtag_pattern = r'#[a-zA-Z0-9_]+'
    return re.findall(hashtag_pattern, text)

def extract_all_data(text):
    """Extract all types of data from text and return as dictionary."""
    return {
        "Emails": extract_email_addresses(text),
        "URLs": extract_urls(text),
        "Time Formats": extract_time_formats(text),
        "Currency Amounts": extract_currency_amounts(text),
        "Hashtags": extract_hashtags(text)
    }

def print_results(results):
    """Print extracted data in a nice format."""
    print("\n✨ EXTRACTION RESULTS ✨")
    print("=" * 40)
    
    for data_type, items in results.items():
        print(f"\n {data_type}: {len(items)} found")
        if items:
            for item in items:
                print(f"  • {item}")
        else:
            print("  • None found")

# Example text to demonstrate functionality
example_text = """
Check out my website at https://www.coolsite.com or email me at 
john.doe@example.com. I'm available from 9:30 AM to 17:45 daily.

The product costs $19.99, but premium users pay $9.99. 
European price: €15.50.

Follow us with #CoolProject and #RegexIsFun!
Meeting at 3:45 PM tomorrow. Budget: $1,234.56.
"""

# Show the example
print("\n EXAMPLE TEXT:")
print("-" * 40)
print(example_text)
print("-" * 40)

# Extract and display results
results = extract_all_data(example_text)
print_results(results)

# Simple user interaction
print("\n Try it yourself!")
print("Enter some text (press Enter twice to finish):")

user_lines = []
while True:
    line = input()
    if line == "":
        break
    user_lines.append(line)

if user_lines:
    user_text = "\n".join(user_lines)
    user_results = extract_all_data(user_text)
    print_results(user_results)
else:
    print("No input provided. Bye Bye!")