class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popularity = defaultdict(int)
        best_video = {}

        n = len(views)
        max_views = float("-inf")
        for i in range(n):
            creator, id, view = creators[i], ids[i], views[i]
            popularity[creator] += view
            max_views = max(max_views, popularity[creator])

            if not creator in best_video:
                best_video[creator] = (id, view)
            else:
                best_id, best_view = best_video[creator]
                if view > best_view or (view == best_view and id < best_id):
                    best_video[creator] = (id, view)
        
        res = []
        for name, total_views in popularity.items():
            if total_views == max_views:
                res.append([name, best_video[name][0]])
        return res