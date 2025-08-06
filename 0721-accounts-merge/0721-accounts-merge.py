class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def findParent(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DisjointSet(n)
        mail_to_index = {}

        for i in range(n):
            for mail in accounts[i][1:]:
                if mail in mail_to_index:
                    dsu.unionBySize(i, mail_to_index[mail])
                else:
                    mail_to_index[mail] = i

        merged_mails = defaultdict(list)
        for mail, idx in mail_to_index.items():
            parent = dsu.findParent(idx)
            merged_mails[parent].append(mail)

        
        ans = []
        for parent, mails in merged_mails.items():
            name = accounts[parent][0]
            ans.append([name] + sorted(mails))

        return ans
