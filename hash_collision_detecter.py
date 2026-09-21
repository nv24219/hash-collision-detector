hash1 = input("Enter MD5 hash 1: ").strip().lower()
hash2 = input("Enter MD5 hash 2: ").strip().lower()

if len(hash1) != 32 or len(hash2) != 32:
    print("Invalid MD5 hash. MD5 must have 32 characters.")
elif hash1 == hash2:
    print("[!] Same MD5 hash detected")
    print("[!] This may indicate an MD5 collision if the original data is different.")
else:
    print("[-] MD5 hashes are different")
    print("[-] No collision detected")