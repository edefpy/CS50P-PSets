import emoji

emoji_name = input("Input: ").strip()
print(f"Output: {emoji.emojize(emoji_name, language = 'alias')}")
