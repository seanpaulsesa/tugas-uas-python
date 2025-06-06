class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Node '{data}' berhasil ditambahkan.")

    def tampilkan_list(self):
        if not self.head:
            print("List kosong.")
            return
        current = self.head
        print("Isi list: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def hapus_node(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"Node '{key}' tidak ditemukan.")
            return
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Node '{key}' berhasil dihapus.")

    def cari_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"Node '{key}' ditemukan!")
                return
            current = current.next
        print(f"Node '{key}' tidak ditemukan.")

    def sisip_setelah(self, key, data):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            print(f"Node '{key}' tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        print(f"Node '{data}' berhasil disisipkan setelah '{key}'.")

    def sisip_sebelum(self, key, data):
        if not self.head:
            print("List kosong.")
            return
        if self.head.data == key:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"Node '{data}' berhasil disisipkan sebelum '{key}'.")
            return
        prev = None
        current = self.head
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"Node '{key}' tidak ditemukan.")
            return
        new_node = Node(data)
        new_node.next = current
        prev.next = new_node
        print(f"Node '{data}' berhasil disisipkan sebelum '{key}'.")

def menu():
    llist = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Tambah node baru")
        print("2. Menyisipkan node setelah nilai tertentu")
        print("3. Menyisipkan node sebelum nilai tertentu")
        print("4. Menghapus node")
        print("5. Menampilkan isi List")
        print("6. Mencari nilai")
        print("7. Keluar")
        pilihan = input("Masukkan pilihan Anda (1-7): ")

        if pilihan == '1':
            data = input("Masukkan data node baru: ")
            llist.tambah_node(data)
        elif pilihan == '2':
            key = input("Masukkan nilai setelah node: ")
            data = input("Masukkan data node baru: ")
            llist.sisip_setelah(key, data)
        elif pilihan == '3':
            key = input("Masukkan nilai sebelum node: ")
            data = input("Masukkan data node baru: ")
            llist.sisip_sebelum(key, data)
        elif pilihan == '4':
            key = input("Masukkan data node yang akan dihapus: ")
            llist.hapus_node(key)
        elif pilihan == '5':
            llist.tampilkan_list()
        elif pilihan == '6':
            key = input("Masukkan nilai yang dicari: ")
            llist.cari_node(key)
        elif pilihan == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
