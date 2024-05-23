from icecream import ic


def findRelativeRanks(score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        rank = []
        pos = []
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        new_score = sorted(score, reverse=True)

        for idx, item in enumerate(new_score):
            if idx < 3:
                
                pos.append(score.index(item))
                rank.append(medals[idx])

        for idx, item in enumerate(new_score):
            if not idx < 3:
                rank.append(str(len(rank) + 1))
                pos.append(score.index(item))

        for idx, item in enumerate(pos):
             score[item] = rank[idx]
        

        return rank, pos, score


score = [10,3,8,9,4]

ic(findRelativeRanks(score))