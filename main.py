import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI argument parser')
    parser.add_argument('-n', '--name', type=str, help='Name')
    parser.add_argument('-a', '--age', type=int, help='Age')
    parser.add_argument('-c', '--city', type=str, help='City')

    args = parser.parse_args()

    if args.name:
        print(f"Name: {args.name}")
    if args.age:
        print(f"Age: {args.age}")
    if args.city:
        print(f"City: {args.city}")

if __name__ == "__main__":
    main()
```

```bash
python script.py -n John -a 30 -c New York
```

```bash
Name: John
Age: 30
City: New York
