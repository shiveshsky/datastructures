class Node:
    val = None
    freq = 0
    is_finished = False
    children = {}


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        proper = A
        reverse_A = [word[::-1] for word in A]
        proper_trie = None
        for word in proper:
            if proper_trie is None:
                proper_trie = self.make_trie(proper_trie, word)
            else:
                self.make_trie(proper_trie, word)
        reverse_trie = None
        for word in reverse_A:
            if reverse_trie is None:
                reverse_trie = self.make_trie(reverse_trie, word)
            else:
                self.make_trie(reverse_trie, word)
        ans = []
        for fix in B:
            pre_freq = self.search_fix(proper_trie, fix)
            post_freq = self.search_fix(reverse_trie, fix[::-1])
            ans.append(min(pre_freq, post_freq))
        return ans

    def make_trie(self, parent, word):
        if len(word) == 0:
            parent.is_finished = True
            return
        if parent is None:
            node = Node()
            node.val = ""
            node.freq = 1
            node.children = dict()
            self.make_trie(node, word)
            return node
        ch = word[0]
        rem = word[1:]
        child = parent.children.get(ch)
        if child is None:
            child = Node()
            child.val = ch
            child.children = dict()
            parent.children[ch] = child
        child.freq += 1
        self.make_trie(child, rem)

    def search_fix(self, parent, word):
        if len(word) == 0:
            return parent.freq
        ch = word[0]
        rem = word[1:]
        child = parent.children.get(ch)
        if child is None:
            return 0
        else:
            return self.search_fix(child, rem)


if __name__ == "__main__":
    print(
        Solution().solve(
            [
                "neeykoablpjdtnpoatbuurdccglmkreweneeykoablpjdtnpoatbuurdccglmkrewe",
                "ssxluuecvgvdoaqbrxcwfxedhtooqyzpp",
                "fpngosdnrdjijsmrswmcifcbukhaaigjn",
                "ssxluuecvgvdoaqbrxcwfxedhtooqyzpp",
                "fkomzosoteuqmucialkjkuifmvvrhykrsfkomzosoteuqmucialkjkuifmvvrhykrseqfkomzosoteuqmucialkjkuifmvvrhykrs",
                "dxrolxryxuqozpaurndypowkoimdzmsqp",
                "ncsrxbpwbfrsrhhljqxckzckrngczonfn",
                "uedpkmciocjevgdjezhetesjaxobcvaokjaf",
                "lespxyuovgeirugkoguihsvezpdykpibglespxyuovgeirugkoguihsvezpdykpibglespxyuovgeirugkoguihsvezpdykpibg",
                "rrkoanirbonypawzomczbsdcdlezxghojrrkoanirbonypawzomczbsdcdlezxghoj",
                "fypvbzzjsnsrztbqklmfcpuulbfhbppgmfypvbzzjsnsrztbqklmfcpuulbfhbppgm",
                "inzpvwdtcxewiuoqvjzhfwufcemsysbovinzpvwdtcxewiuoqvjzhfwufcemsysbovfinzpvwdtcxewiuoqvjzhfwufcemsysbov",
                "ofxhaelccslytdjvdzzimibzrefukrjwdruihoswkifofxhaelccslytdjvdzzimibzrefukrjwd",
                "ssxluuecvgvdoaqbrxcwfxedhtooqyzpphgau",
                "lgwajfzlwkjwcnoqrplpbfoukcugkretpyjfjnhhlgwajfzlwkjwcnoqrplpbfoukcugkretp",
                "xmxpwnowyggueuofmmvbchnedhrsygjnlxmxpwnowyggueuofmmvbchnedhrsygjnlxmxpwnowyggueuofmmvbchnedhrsygjnl",
                "gwtbhujslxxnexxuwnfaggjzjrwozzxfyamdcjbprhtngwtbhujslxxnexxuwnfaggjzjrwozzxfy",
                "fgsbjiqzvedzoppykqsmcroyfldmlfrssfgsbjiqzvedzoppykqsmcroyfldmlfrsstgo",
                "zmzwttfnshczbmbliowxjxuzodxyyxcpwtvjsjbaoiojlw",
                "fpngosdnrdjijsmrswmcifcbukhaaigjnfpngosdnrdjijsmrswmcifcbukhaaigjn",
            ],
            [
                "fkomzosoteuqmucialkjkuifmvvrhykrs",
                "fpngosdnrdjijsmrswmcifcbukhaaigjn",
                "hrncndygwplhezppepcctmqifwywyzvvs",
                "inzpvwdtcxewiuoqvjzhfwufcemsysbov",
                "lgwajfzlwkjwcnoqrplpbfoukcugkretp",
                "ofxhaelccslytdjvdzzimibzrefukrjwd",
                "qqfvcmvhmedrnlariqobcwzulehwaaaiu",
                "utioqkhulxjbeqphxnjwbbfskihkqikhq",
                "vycywktddoexibdnbaoivrnktykgkkjgu",
                "yravmjaatmgksmtpzhxresurqtcdqydvo",
            ],
        )
    )
