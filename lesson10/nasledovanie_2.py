class A:
    def genre(self):
        return ["Blues"]

    def artist(self):
        return []


class B(A):
    def genre(self):
        return ["Electric Blues"] + super().genre()


class C(A):
    def artist(self):
        return ["B.B.King"] + super().artist()


class D(A): pass


class E(B):
    def genre(self):
        return ["Soul Blues"] + super().genre()


class F(B):
    def genre(self):
        return ["Blues Rock"] + super().genre()

    def artist(self):
        return ["Eric Clapton"] + super().artist()


class G(C, D): pass


class H(E, F, G):
    def genre(self):
        return ["Boogie Rock"] + super().genre()


if __name__ == "__main__":
    H = H()

    print("List of artists: ")
    for artist in H.artist():
        print(" - " + artist)

    print("List of linked genres: ")
    for genre in H.genre():
        print(" - " + genre)

