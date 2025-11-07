from typing import List, Dict


def process_data(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data)}


if __name__ == "__main__":
    direct = process_data([4, 5, 6])
    # Example usage
    print(process_data([1, 2, 3]))
    print(f"{direct}")
