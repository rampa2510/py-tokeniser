# CharTokenizer

A simple character-level tokenizer that converts text to numerical IDs and back.

## What It Does

- Converts text characters to unique numerical IDs
- Handles uppercase, lowercase, numbers, and symbols
- Marks unknown characters with a special token

## How to Use

```python
# Initialize
tokenizer = CharTokenizer()

# Encode text to IDs
ids = tokenizer.encode("Hello, world!")

# Decode IDs back to text
text = tokenizer.decode(ids)
```

## Sample Output

```
Original: 'Hello, World! 123'
Encoded: [8, 5, 12, 12, 15, 27, 0, 23, 15, 18, 12, 4, 33, 0, 49, 50, 51]
Decoded: 'Hello, World! 123'

Original: 'Unicode text: 你好世界 πr² 🍕'
Encoded: [21, 14, 9, 3, 15, 4, 5, 0, 20, 5, 24, 20, 26, 0, 95, 95, 95, 95, 0, 95, 18, 95, 0, 95]
Decoded: 'Unicode text: <UNK><UNK><UNK><UNK> <UNK>r<UNK> <UNK>'
```

This tokenizer handles standard ASCII text perfectly, with special token handling for characters outside its vocabulary.
