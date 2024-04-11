import os

# Run the command and store its output
output = os.popen("timeout 2 nc mercury.picoctf.net 22342").read()

# Write the ordinal numbers output to a file
with open("results.txt", "w") as file:
    file.write("Ordinal Numbers to Be Converted to ASCII:\n")
    file.write(output)

# Convert the ordinal numbers to ASCII and print the flag
ascii_text = ''.join(chr(int(x)) for x in output.split())
print(ascii_text)
