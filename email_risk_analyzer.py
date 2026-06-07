import re

def analyze_email(email_text):
    risk_score = 0
    reasons = []

    urgent_words = ["urgent", "verify your account",
                    "click here", "immediately"]

    for word in urgent_words:
        if word.lower() in email_text.lower():
            risk_score += 2
            reasons.append(word)

    urls = re.findall(r'https?://\S+|www\.\S+', email_text)

    if urls:
        risk_score += 3
        reasons.append("Contains external link")

    sensitive_words = ["password", "otp", "credit card", "pin"]

    for word in sensitive_words:
        if word.lower() in email_text.lower():
            risk_score += 4
            reasons.append(word)

    if risk_score >= 6:
        status = "Suspicious Email"
    else:
        status = "Safe Email"

    return status, reasons

email = input("Enter email content: ")

status, reasons = analyze_email(email)

print("\nResult:", status)
print("Reasons:")
for reason in reasons:
    print("-", reason)
