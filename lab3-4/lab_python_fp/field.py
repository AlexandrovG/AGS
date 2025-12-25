def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        field_name = args[0]
        for item in items:
            if field_name in item and item[field_name] is not None:
                yield item[field_name]
    else:
        for item in items:
            result = {}
            has_valid_fields = False
            
            for field_name in args:
                if field_name in item and item[field_name] is not None:
                    result[field_name] = item[field_name]
                    has_valid_fields = True
            
            if has_valid_fields:
                yield result
if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 3000, 'color': 'white'},
    ]
    
    print("Test 1:")
    for item in field(goods, 'title'):
        print(item)
    
    print("\nTest 2:")
    for item in field(goods, 'title', 'price'):
        print(item)