class CharTokenizer:
    def __init__(self):
        # Standard character set including common printable characters
        self.chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?;:'\"()[]{}-_=+@#$%^&*<>/\\`~"

        # Special token for unknown characters
        self.unknown_char = "<UNK>"
        self.unknown_id = len(self.chars)

        # Create mappings
        self.char_to_id = {char: i for i, char in enumerate(self.chars)}
        self.id_to_char = {i: char for i, char in enumerate(self.chars)}

        # Add unknown token to mappings
        self.char_to_id[self.unknown_char] = self.unknown_id
        self.id_to_char[self.unknown_id] = self.unknown_char

    def encode(self, text):
        """Convert input text to token IDs"""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        return [self.char_to_id.get(char, self.unknown_id) for char in text]

    def decode(self, ids):
        """Convert token IDs back to text"""
        if not isinstance(ids, list):
            raise TypeError("Input must be a list of integer IDs")

        return "".join(self.id_to_char.get(id, self.unknown_char) for id in ids)

    def get_vocab_size(self):
        """Return the vocabulary size including special tokens"""
        return len(self.char_to_id)


# Testing the tokenizer
tokenizer = CharTokenizer()

# Test basic text
text1 = "Hello, World! 123"
encoded1 = tokenizer.encode(text1)
print(f"Original: '{text1}'")
print(f"Encoded: {encoded1}")
print(f"Decoded: '{tokenizer.decode(encoded1)}'")

# Test with unicode characters
text2 = "Unicode text: 你好世界 πr² ñáéíóú 🍕"
encoded2 = tokenizer.encode(text2)
print(f"\nOriginal: '{text2}'")
print(f"Encoded: {encoded2}")
print(f"Decoded: '{tokenizer.decode(encoded2)}'")

# Test edge cases
edge_cases = ["", "   ", "!@#$%^&*()"]
for case in edge_cases:
    encoded = tokenizer.encode(case)
    decoded = tokenizer.decode(encoded)
    print(f"\nOriginal: '{case}'")
    print(f"Encoded: {encoded}")
    print(f"Decoded: '{decoded}'")

print(f"\nVocabulary size: {tokenizer.get_vocab_size()}")

