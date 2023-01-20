"""
input-> "python in the best"



output text-> "python in the Best"
"""
text = input("enter text:")

symbol1 = input("enter symbol:")

if symbol1 in text:  # провиряем

    symbol2 = input("enter symbol2:")

    count = int(input("Enter count:"))

    format_text = text.replace(symbol1, symbol2, count)
    to_upper = input("Change all symbolls to UPPER? yes/no :").lower().strip()

    if to_upper == "yes":
        format_text = format_text.upper()
    print(format_text)
else:
    print("symbol1 not in", text)
