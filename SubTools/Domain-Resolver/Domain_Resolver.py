import sys
import subprocess

def resolve_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()

        for domain in domains:
            domain = domain.strip()
            try:
                result = subprocess.run(["dig", "+short", domain], capture_output=True, text=True)
                output = result.stdout.strip()
                print(f"{domain} --> {output}")
            except Exception as e:
                print(f"{domain} --> Error: {e}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '-p':
        print("Usage: python3 code.py -p <file_path>")
        sys.exit(1)  

    file_path = sys.argv[2]
    resolve_domains(file_path)

if __name__ == "__main__":
    main()
