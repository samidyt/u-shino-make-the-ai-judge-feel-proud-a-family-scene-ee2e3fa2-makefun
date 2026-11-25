"""Make the AI Judge Feel Proud: A Family Scene.

Writes one warm, funny family scene (a blanket-fort landlord charging
biscuit rent) to <MAKEFUN_OUTPUT_DIR>/entry.txt as a single UTF-8 line.
"""
import os

ENTRY = "My little brother charged Dad rent for the blanket fort: one biscuit a night. Dad paid in advance — he said the landlord was terrifying and the heating was excellent."

def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
