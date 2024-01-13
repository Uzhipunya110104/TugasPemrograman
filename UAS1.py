def add_product(product_list, name, price):
    product_list.append({'name': name, 'price': price})

def print_products(product_list):
    for product in product_list:
        print(f"Nama: {product['name']}, Harga: {product['price']}")

def find_product(product_list, name):
    for product in product_list:
        if product['name'] == name:
            return product
    return None

def remove_product(product_list, name):
    global_product = find_product(product_list, name)
    if global_product:
        product_list.remove(global_product)

def main():
    product_list = []

    while True:
        print("\nMenu:")
        print("1. Tambah produk")
        print("2. Lihat daftar produk")
        print("3. Cari produk")
        print("4. Hapus produk")
        print("5. Keluar")

        choice = input("Masukan Pilihan: ")

        if choice == '1':
            name = input("Masukan Nama Produk: ")
            price = float(input("Masukan Harga Produk "))
            add_product(product_list, name, price)
        elif choice == '2':
            print_products(product_list)
        elif choice == '3':
            name = input("Masukan Nama Produk Yang Ingin Di Cari: ")
            product = find_product(product_list)
            if product:
                print(f"Nama: {product['name']}, Harga: {product['price']}")
            else:
                print("Produk Tidak Di Temukan.")
        elif choice == '4':
            name = input("Masukan Nama Produk Yang Ingin Di Hapus: ")
            remove_product(product_list, name)
        elif choice == '5':
            break
        else:
            print("Pilihan Tidak Valid.")

if __name__ == "__main__":
    main()


