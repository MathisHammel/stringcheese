# StringCheese

![StringCheese logo](https://raw.githubusercontent.com/MathisHammel/stringcheese/main/logo.png)

StringCheese is a script written in Python to extract CTF flags (or any other pattern with a prefix) automatically.

It works like a simple `strings | grep` command, but can detect many encodings (like base64, XOR, rot13) and works on file formats other than plaintext.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install StringCheese.

```bash
sudo pip install stringcheese
```

## Usage

StringCheese only needs to know the flag prefix to work. You can pass it the input file using the `--file` option or through stdin.

```bash
stringcheese FLAG{ --file input.txt
cat  input.txt | stringcheese FLAG{
```

## How it works

StringCheese generates strings which encode the flag prefix in various ways.

Those strings are then searched in several transformed version of the input file : one in two bytes, reversed, etc.

When the encoded flag prefix is found somewhere, the corresponding decoder is called to regenerate the flag.

![how it works](https://raw.githubusercontent.com/MathisHammel/stringcheese/main/howitworks.png)

## Authors and contributors
- [Mathis HAMMEL](https://twitter.com/MathisHammel)
- Anso
- [Podalirius](https://twitter.com/podalirius_)
- [Hedroed](https://twitter.com/hedroed)
- [You ?](https://github.com/MathisHammel/stringcheese/pulls)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPL 2.0](https://choosealicense.com/licenses/gpl-2.0/)
