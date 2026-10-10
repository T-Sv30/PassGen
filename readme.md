# PassGen

PassGen generates candidate password lists offline using common character
substitutions and optional numeric suffixes. It does not test passwords
against websites or perform HTTP login requests. Use generated lists only
for authorized security work.

## Requirements

- Python 3
- `pyperclip` for clipboard output

Install dependencies:

```sh
python -m pip install -r requirements.txt
```

## Usage

Generate candidates:

```sh
python passgen.py smith
```

Append numeric suffixes:

```sh
python passgen.py -n smith
```

Generate the full substitution list:

```sh
python passgen.py -f smith
```

Write candidates to a file:

```sh
python passgen.py -o output.txt smith
```

Copy candidates to the clipboard (requires a working clipboard backend):

```sh
python passgen.py -c smith
```

Use `python passgen.py --help` to see all supported options. Full lists can
consume substantial memory; use them only with inputs of manageable length.
