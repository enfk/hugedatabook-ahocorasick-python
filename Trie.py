
# http://en.wikipedia.org/wiki/Trie
# http://www.youtube.com/watch?v=BXeIu54mUg0

from collections import defaultdict

class Trie:
    def __init__(self, terms = {}):
        self.root = defaultdict(Trie)
        self.value = None
        for k, v in terms.iteritems():
            self.add(k, v)

    def __str__(self, headkey = ""):
        ret = ""
        for x, y in self.root.iteritems():
            fullkey = headkey + x
            lspace = " " * len(headkey)
            ret += lspace + fullkey + " / " + str(y.value) + "\n"
            if len(y.root) > 0:
                ret += y.__str__(fullkey)
        return ret

    def add(self, s, value):
        """Add the string `s` to the 
        `Trie` and map it to the given value."""
        head, tail = s[0], s[1:]
        cur_node = self.root[head]
        if not tail:
            cur_node.value = value
            return  # No further recursion
        self.root[head].add(tail, value)

    def lookup(self, s, default=None):
        """Look up the value corresponding to 
        the string `s`. Expand the trie to cache the search."""
        head, tail = s[0], s[1:]
        node = self.root[head]
        if tail:
            return node.lookup(tail)
        return node.value or default

    def remove(self, s):
        """Remove the string s from the Trie. 
        Returns *True* if the string was a member."""
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        if tail:
            return node.remove(tail)
        else:
            del node
            return True

    def prefix(self, s):
        """Check whether the string `s` is a prefix 
        of some member. Don't expand the trie on negatives (cf.lookup)"""
        if not s:
            return True
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False  # Not contained
        node = self.root[head]
        return node.prefix(tail)

    def items(self):
        """Return an iterator over the items of the `Trie`."""
        for char, node in self.root.iteritems():
            if node.value is None:
                yield node.items
            else:
                yield node

class Trie_X:
    def __init__(self):
        pass

    # insert key into trie and put value into key's bucket
    def insert_key(key, value, trie):
        pass

    # true if trie has key, false otherwise
    def has_key(key, trie):
        pass

    # retrieves the value from key's bucket
    def retrieve_val(key, trie):
        pass

    # return the list of all keys that begin with the prefix
    # where prefix is a string of at least one charactor
    def start_with_prefix(prefix, trie):
        pass

if __name__ == '__main__':
    tr = Trie({'to': 7, 'tea': 3, 'ted': 4, 'ten': 12})
#    tr.add("to", 7)
#    tr.add("tea", 3)
#    tr.add("ted", 4)
#    tr.add("ten", 12)
    tr.add("A", 15)
    tr.add("i", 11)
    tr.add("in", 5)
    tr.add("inn", 9)
    print tr
    print tr.prefix("t")
    print tr.lookup("te")
    assert tr.prefix("to") == True
    assert tr.prefix("trump") == False
    assert tr.lookup("ted") == 4
    # print tr.start_with_prefix("te")
    # assert tr.start_with_prefix("t") == ["to", "tea", "ted", "ten"]
