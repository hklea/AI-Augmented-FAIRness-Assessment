from pathlib import Path

path = Path("data/ground_truth/Ouranosinc_xclim/README.md")
text = path.read_text(encoding="utf-8", errors="ignore")

print("Total length:", len(text))

print("\n--- Last 800 characters BEFORE cutoff ---")
print(text[11200:12000])

print("\n--- First 1500 characters CUT after cutoff ---")
print(text[12000:13500])