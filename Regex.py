import re 
def getemail(text):
    #Get email addresses from text.
    emailpattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(emailpattern, text)

def geturls(text):
    #Get URLs from text.
    urlpattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[/\w.-]*'
    return re.findall(urlpattern, text)

def gettime(text):
    #Extract time formats (12h and 24h) from text.
    # 12-hour format with AM/PM
    hour12_pattern = r'\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)\b'
    
    # 24-hour format (00:00 to 23:59)
    hour24_pattern = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b'
    return re.findall(hour24_pattern, text) + re.findall(hour12_pattern, text)

def getcurrency(text):
    #Get currency amounts from text.
    currencypattern = r'[$€£¥]|BIF|RWF)\d+(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currencypattern, text)

def gethashtags(text):
    #Get all the hashtags from text.
    hashtagpattern = r'#[a-zA-Z0-9_]+'
    return re.findall(hashtagpattern, text)

def getalldata(text):
    #Get all types of data from text in form of dictionary.
    return {"Emails": getemail(text),
        "URLs": geturls(text),
        "Time Formats": gettime(text),
        "Currency": getcurrency(text),
        "Hashtags": gethashtags(text)}

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

The product costs 35000BIF, but premium users pay 25000BIF. 
#European price: €15.50.

Follow us with #CoolProject and #RegexIsFun!
Meeting at 3:45 PM tomorrow. Budget: $1,234.56.
"""

# Show the example
print("\n EXAMPLE TEXT:")
print("-" * 40)
print(example_text)
print("-" * 40)

# Extract and display results
results = getalldata(example_text)
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
    user_results = getalldata(user_text)
    print_results(user_results)
else:
    print("No input provided. Bye Bye!")