import libpry
import libqtile.utils as utils


class utranslateMasks(libpry.AutoTree):
    def test_one(self):
        assert utils.translateMasks(["shift", "control"])
        assert utils.translateMasks([]) == 0


class uLRUCache(libpry.AutoTree):
    def test_one(self):
        class Foo:
            ran = False
            @utils.LRUCache(2)
            def one(self, x):
                self.ran = True
                return x

        f = Foo()
        assert f.one(1) == 1
        assert f.ran
        f.ran = False
        assert f.one(1) == 1
        assert not f.ran

        f.ran = False
        assert f.one(1) == 1
        assert not f.ran
        assert f.one(2) == 2
        assert f.one(3) == 3
        assert f.ran

        f.ran = False
        assert f.one(1) == 1
        assert f.ran

        assert len(f._cached_one) == 2
        assert len(f._cachelist_one) == 2


tests = [
    utranslateMasks(),
    uLRUCache()
]

