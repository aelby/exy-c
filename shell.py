import exyc

while True:
    text = input("exy c >> ")
    result, error = exyc.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)