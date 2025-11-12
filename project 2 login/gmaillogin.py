import os
# अगर file नहीं है तो बना दें ताकि read में error न आए
if not os.path.exists('password.txt'):
    open('password.txt', 'w').close()

def find_record_by_mobile(gmail):
    """
    password.txt में हर line को ',' से विभाजित करके check करेगा।
    हम मान रहे हैं किgmail field 5th है (index 4, 0-based).
    अगर मिले तो पूरी parts list return करेगा, नहीं तो None।
    """
    with open('password.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # line में extra spaces हटाएँ और फिर comma से split करें
            parts = [p.strip() for p in line.strip().split(',')]
            # सुनिश्चित करें कि कम से कम 5 fields मौजूद हों (gmail index 4)
            if len(parts) >= 6 and parts[5] == gmail:
                return parts   # example: ["ravi","kushwaha","45","male","8109358746","ravikush081@gmail.com","passwodj"]
    return None

# --- LOGIN LOOP: तब तक पूछेगा जब तक registered gmail न मिल जाए ---
while True:
    gmail = input("Login - Enter your Gmail : ").strip()

    # basic validation: 10 digits होना चाहिए
    if not(gmail.lower().endswith("@gmail.com"))and(len(gmail)>10):
        print("Invalid input! Please enter a gmail gmail.")
        continue

    record = find_record_by_mobile(gmail)
    if record is None:
        print(" This Gmail is not registered. Please enter a registered gmail.")
        # IMPORTANT: continue -> वही loop फिर से चलेगा और user से नया gmail मांगेगा
        continue
    else:
        stored_password = record[6] if len(record) >= 7 else ""
        if stored_password:
            attempts = 0
            while attempts < 3:
                pw = input("Enter your password: ").strip()
                if pw == stored_password:
                    print("Login successful! Welcome,", record[0])
                    break
                else:
                    attempts += 1
                    print(f"Incorrect password. Attempts left: {3-attempts}")
            else:
                print("Too many wrong attempts. Login failed.")
            # अगर password match हुआ तो break outer loop (login success)
            if attempts < 3 and pw == stored_password:
                break
            else:
                # password fail पर आप चाहें तो फिर से gmail माँगना चाहेंगे या exit कर दें
                # नीचे हम फिर से gmail माँगने के लिए continue कर रहे हैं
                continue
        else:
            # अगर file में password नहीं है तो सीधे login मान लें
            print("Login (Gmail-only) successful. Welcome,", record[0])
            break

# # आगे: user logged in — यहाँ dashboard या आगे की processing कर सकते हैं
# print("End of login flow.")