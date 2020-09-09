import sys
import copy

def main() -> int:
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)

    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(stuff, dragon_loot)
    display_inventory(inv)
    return 0

def display_inventory(inventory: dict) -> None:
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print(f'Total number of items: {item_total}')
    print('-' * 40)

def add_to_inventory(
        inventory: dict,
        added_items: list
) -> dict:
    """ Returns a new inventory dict. Does
    not modify the passed in dict in place."""

    inventory_copy = copy.copy(inventory)
    for item in added_items:
        inventory_copy.setdefault(item, 0)
        inventory_copy[item] += 1
    return inventory_copy

if __name__ == '__main__':
    sys.exit(main())
