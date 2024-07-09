friends: int = int(input("How many friends came to Danny's home? "));
slices: int = int(input("How many slices of pizza were ordered? "));

print(f"\nEach friend got {slices//friends} slices, and {slices%friends} slices remained on the tray. \nBon Appetit!")