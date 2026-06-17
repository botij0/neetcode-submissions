class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image: List[List[int]], sr: int, sc: int, color: int, initialColor: int):
            if (min(sr,sc) < 0 or 
                sr >= len(image) or 
                sc >= len(image[0]) or 
                image[sr][sc] != initialColor or
                image[sr][sc] == color):

                return
            
            image[sr][sc] = color
            dfs(image, sr - 1, sc, color, initialColor)
            dfs(image, sr + 1, sc, color, initialColor)
            dfs(image, sr, sc - 1, color, initialColor)
            dfs(image, sr, sc + 1, color, initialColor)
        
        dfs(image,sr,sc,color,image[sr][sc])
        return image