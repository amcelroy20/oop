import RetailItemClass as r

def main():
    Item1 = r.RetailItem('Item #1')
    Item2 = r.RetailItem('Item #2')
    Item3 = r.RetailItem('Item #3')

    Item1.set_values()
    Item2.set_values()
    Item3.set_values()

    Item1.print_values()
    Item2.print_values()
    Item3.print_values()

main()