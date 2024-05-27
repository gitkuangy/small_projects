# Caesar Cipher Project

This is a simple Caesar Cipher project implemented in Python. The Caesar Cipher is one of the earliest and simplest methods of encryption technique. It’s a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet.

## Features

- **Encrypt**: Encode a message by shifting the letters of the alphabet.
- **Decrypt**: Decode a message by shifting the letters of the alphabet back.
- **Handles Non-alphabet Characters**: Non-alphabet characters (numbers, symbols, spaces) remain unchanged.
- **Repeated Use**: Allows the user to encrypt or decrypt multiple messages in one session.
- **Shift Modulus**: Handles shift values greater than the length of the alphabet.

## Usage

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/gitkuangy/small_projects.git
    cd caesar-cipher
    ```

2. Make sure you have Python installed on your machine.

3. Run the script:
    ```sh
    python caesar_cipher.py
    ```

4. Follow the prompts to encode or decode a message.

## Example

```plaintext
$ python caesar_cipher.py
  ___ ___
 /   |   \_____    ______ ______  ______
/    ~    \__  \  /  ___//  ___/ /  ___/
/____|__  / __ \_\___ \ \___ \  \___ \
        \/____  /____  >____  >/____  >
             \/     \/     \/      \/
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here's the encoded result: mjqqt btwqi

Do you want to continue?
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
Here's the decoded result: hello world
Do you want to continue?
no

