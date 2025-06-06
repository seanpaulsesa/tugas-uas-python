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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tampilkan_list(self):
        current = self.head
        if not current:
            print("List kosong!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def hapus_node(self, key):
        current = self.head
        prev = None
        if current and current.data == key:
            self.head = current.next
            return
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Node tidak ditemukan!")
            return
        prev.next = current.next

    def cari_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                print("Node ditemukan!")
                return
            current = current.next
        print("Node tidak ditemukan!")

    def sisip_setelah(self, key, data):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            print("Node tidak ditemukan!")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def sisip_sebelum(self, key, data):
        if not self.head:
            print("List kosong!")
            return
        if self.head.data == key:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        prev = None
        current = self.head
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Node tidak ditemukan!")
            return
        new_node = Node(data)
        prev.next = new_node
        new_node.next = current

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
            data = input("Masukkan data node: ")
            llist.tambah_node(data)
        elif pilihan == '2':
            key = input("Masukkan nilai setelah node: ")
            data = input("Masukkan data yang akan disisipkan: ")
            llist.sisip_setelah(key, data)
        elif pilihan == '3':
            key = input("Masukkan nilai sebelum node: ")
            data = input("Masukkan data yang akan disisipkan: ")
            llist.sisip_sebelum(key, data)
        elif pilihan == '4':
            key = input("Masukkan nilai yang ingin dihapus: ")
            llist.hapus_node(key)
        elif pilihan == '5':
            llist.tampilkan_list()
        elif pilihan == '6':
            key = input("Masukkan nilai yang dicari: ")
            llist.cari_node(key)
        elif pilihan == '7':
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    menu()
