import pyinputplus as pyip
import random

def main() -> int:
    items = (
        'wheat white sourdough chicken turkey ham tofu '
        'cheddar swiss mozzarella mayo mustard lettuce '
        'tomato'
    ).split()

    item_prices = {item: random.random() * 10.0 for item in items}
    items_added = []

    bread_type = pyip.inputMenu('wheat white sourdough'.split())
    items_added.append(bread_type)

    protein_type = pyip.inputMenu('chicken turkey ham tofu'.split())
    items_added.append(protein_type)

    cheesed_required = pyip.inputYesNo('Would you like to add cheese? ')
    if cheesed_required == 'yes':
        cheese = pyip.inputMenu('cheddar swiss mozzarella'.split())
        items_added.append(cheese)

    misc_items_required = pyip.inputYesNo(
        'Would you like mayo, mustard, lettuce or tomato? '
    )
    if misc_items_required == 'yes':
        misc_item = pyip.inputMenu('mayo mustard lettuce tomato'.split())
        items_added.append(misc_item)

    total_sandwiches = pyip.inputInt(
        'How many sandwiches would you like? ', greaterThan=0
    )

    print('Summary'.center(40, '-'))
    print('Items added:')
    for item in items_added:
        print(f'    * {item} (${item_prices[item]:.2f})')

    sandwich_price = sum(item_prices[item] for item in items_added)
    print(f'\nSandwich price: ${sandwich_price:.2f}')
    print(f'Total number of sanwiches: {total_sandwiches}')
    print(f'Total cost: ${total_sandwiches * sandwich_price:.2f}')
    return 0


if __name__ == '__main__':
    exit(main())
