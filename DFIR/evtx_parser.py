import pandas as pd

def main():
    # Change the filename if your CSV has a different name
    csv_file = 'evtx_data.csv'

    try:
        print(f"[+] Loading CSV: {csv_file} ...")
        df = pd.read_csv(csv_file)

        print("[+] File loaded successfully. First 5 rows:")
        print(df.head())  # Display the first 5 rows

        # Save a copy as parsed output
        df.to_csv("security_parsed.csv", index=False)
        print(f"[+] Parsed {len(df)} rows. Saved to: security_parsed.csv")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
