def print_menu():
    """
    Prints the Enigma project manual
    """
    print('''Enigma Manual
                Run options: [-h | -e | -d] {CipherName} {FileName} {EncryptionKey}
                   -h : displays this menu; other arguments are ignored.
                   -e : encrypt and display
                   -d : decrypt and display
                       CipherName      : cipher to use when encrypting/decrypting; [rot13, rail-fence, morse]
                       FileName        : path to file to encrypt/decrypt
                       EncryptionKey   : Optional -> must be provided if cipher requires a key''')
