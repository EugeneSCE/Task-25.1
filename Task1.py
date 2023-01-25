import unittest


def lenCheck(products, productPrices, productSold, soldPrice):
    max_len_for_prod = 99
    min_len_for_prod = 1

    if not(min_len_for_prod <= len(products) <= max_len_for_prod):
        raise ValueError("Wrong products length")

    elif not(min_len_for_prod <= len(productSold) <= max_len_for_prod):
        raise ValueError("Wrong productPrices length")

    elif len(products) != len(productPrices):
        raise ValueError("'products' and 'productPrices' length aren't equal")

    elif len(productSold) != len(soldPrice):
        raise ValueError("'productSold' and 'soldPrice' length aren't equal")

    return products, productPrices, productSold, soldPrice


def typeCheck(products, productPrices, productSold, soldPrice):
    max_price = 100000.00
    min_price = 1.00

    for prod in products:
        if not type(prod) is str:
            raise TypeError("The 'products' array should only contain strings")

    for prod_price in productPrices:
        if not type(prod_price) is float:
            raise TypeError("The 'productPrices' array should only contain floats")
        elif not(min_price <= prod_price <= max_price):
            raise ValueError("The prices in 'productPrices' array should be between 1.00 and 100000.00")

    for prod_sold in productSold:
        if not type(prod_sold) is str:
            raise TypeError("The 'productSold' array should only contain strings")

    for sold_price in soldPrice:
        if not type(sold_price) is float:
            raise TypeError("The 'soldPrice' array should only contain floats")
        elif not(min_price <= sold_price <= max_price):
            raise ValueError("The prices in 'soldPrice' array should be between 1.00 and 100000.00")

    return products, productPrices, productSold, soldPrice


def priceCheck(products, productPrices, productSold, soldPrice):
    lenCheck(products, productPrices, productSold, soldPrice)
    typeCheck(products, productPrices, productSold, soldPrice)

    error_count = 0
    for sold_product_index in range(len(productSold)):
        try:
            act_prod_index = products.index(productSold[sold_product_index])
            if productPrices[act_prod_index] != soldPrice[act_prod_index]:
                error_count += 1
        except:
            raise ValueError(productSold[sold_product_index] + " does not appear in products array")

    return error_count


#################  TEST    #################

def output_test():
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 2

def type_test(type,row):

    products = ['eggs']
    productPrices = [2.89]
    productSold = ['eggs']
    soldPrice = [2.89]
    data = [products, productPrices, productSold, soldPrice]

    if type == "int":
        data[row] = 55
    elif type == "float":
        if row == 1 or row == 3:
            return True
        data[row] = 55.55
    elif type == "str":
        if row == 0 or row == 2:
            return True
        data[row] = []
        data[row].append("STRING")
    elif type == "list":
        data[row] = []
        data[row].append([1,2,3])
    elif type == "tuple":
        data[row] = []
        data[row].append((1, 2, 3))
    elif type == "range":
        data[row] = []
        data[row].append(range(1,5))
    elif type == "dict":
        data[row] = []
        data[row].append({1: 2, "String": True})
    elif type == "bool":
        data[row] = []
        data[row].append(True)
    else:
        print("error")
        pass


    try:
        priceCheck(data[0], data[1], data[2], data[3])
        return False
    except TypeError:
        return True
    except Exception:
        return False

def max_len_test(num):

    products = ['eggs']
    productPrices = [2.89]
    productSold = ['eggs']
    soldPrice = [2.89]

    data = [products, productPrices, productSold, soldPrice]

    data[num] = data[num] * 100
    try:
        priceCheck(data[num], data[num], data[num], data[num])
        return False
    except ValueError:
        return True
    except Exception:
        return False

def min_len_test(num):
    products = ['eggs']
    productPrices = [2.89]
    productSold = ['eggs']
    soldPrice = [2.89]

    data = [products, productPrices, productSold, soldPrice]

    data[num] = []
    try:
        priceCheck(data[num], data[num], data[num], data[num])
        return False
    except ValueError:
        return True
    except Exception:
        return False

def price_test(min_max,sold_product):
    products = ['eggs']
    productPrices = [2.89]
    productSold = ['eggs']
    soldPrice = [2.89]

    data = [products, productPrices, productSold, soldPrice]

    if min_max == "min":
        val = 0.99
    elif min_max == "max":
        val = 100000.01
    if sold_product == "sold":
        data[3].append(val)
    elif sold_product == "product":
        data[1].append(val)

    try:
        priceCheck(data[0], data[1], data[2], data[3])
        return False
    except ValueError:
        return True
    except Exception:
        priceCheck(data[0], data[1], data[2], data[3])
        return False




def runAllTests():
    type = ["int", "float", "str", "list", "tuple", "range", "dict", "bool"]

    test_dict = {"True": 0, "False": 0}

    for num in range(4):
        for t in type:
            test_dict[str(type_test(t, num))] += 1
        test_dict[str(max_len_test(num))] += 1
        test_dict[str(min_len_test(num))] += 1
        test_dict[str(min_len_test(num))] += 1
        test_dict[str(price_test("min", "sold"))] += 1
        test_dict[str(price_test("min", "product"))] += 1
        test_dict[str(price_test("max", "sold"))] += 1
        test_dict[str(price_test("max", "product"))] += 1
        return test_dict

if __name__ == '__main__':
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]

    print(priceCheck(products, productPrices, productSold, soldPrice))
    print(runAllTests())

